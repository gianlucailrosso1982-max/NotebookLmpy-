#!/usr/bin/env python3
"""
effetti.py — calcoli deterministici di efficacia reale.

Trasforma i numeri letti in una fonte in effetti assoluti confrontabili:
rischi nei due gruppi, RR, OR, differenza assoluta (ARR/ARI), NNT (NNTB/NNTH),
tutti con intervallo di confidenza al 95%. Serve a non fare aritmetica a mente
e a non ricalcolare in silenzio: ogni risultato mostra da quali numeri deriva.

Usa solo la libreria standard. Metodi classici: Wald su scala logaritmica per
RR e OR, Wald per la differenza di rischi, Altman (BMJ 1998) per l'IC dell'NNT
quando la differenza di rischi include lo zero.

Modalità
  table     da una tabella 2x2 (eventi/totale nei due gruppi) — studio singolo
  relative  da una misura relativa (RR, OR, HR) con IC e un rischio di base
            (è il modo in cui le tabelle Summary of Findings di GRADE ricavano
            gli effetti assoluti)
  nnt       da una differenza assoluta di rischio con IC
  smd       interpreta una differenza media standardizzata (d di Cohen / SMD)

Esempi
  python3 effetti.py table --ei 128 --ni 419 --ec 100 --nc 423
  python3 effetti.py relative --measure OR --value 0.31 --ci 0.20 0.48 --baseline 0.45
  python3 effetti.py relative --measure RR --value 0.97 --ci 0.94 1.00 --baseline 0.60
  python3 effetti.py nnt --arr 0.15 --ci 0.05 0.25
  python3 effetti.py smd --value 0.45
  Aggiungi --json per un output leggibile da macchina.

Avvertenza importante: la modalità table vale per UN singolo studio o per una
tabella 2x2 già aggregata dagli autori. Sommare gli eventi di più studi e
calcolare RR/OR sui totali NON riproduce una meta-analisi (le stime pooled
pesano gli studi e possono differire anche molto: paradosso di Simpson).
"""

import argparse
import json
import math
import sys

Z95 = 1.959964


def _ci_log(point, se):
    return math.exp(math.log(point) - Z95 * se), math.exp(math.log(point) + Z95 * se)


def _nnt_from_diff(diff, lo, hi):
    """Restituisce (nnt_point, descrizione_ic) secondo Altman 1998.

    diff, lo, hi sono differenze di rischio (intervento - controllo).
    """
    if diff == 0:
        return None, "differenza nulla: NNT non definito (infinito)"
    nnt = 1.0 / abs(diff)
    if (lo > 0 and hi > 0) or (lo < 0 and hi < 0):
        bounds = sorted([1 / abs(lo), 1 / abs(hi)])
        return nnt, f"da {bounds[0]:.1f} a {bounds[1]:.1f}"
    # l'IC della differenza include lo zero: l'IC dell'NNT passa per l'infinito
    parts = []
    if hi > 0:
        parts.append(f"NNT(evento aumentato) {1/hi:.1f}")
    if lo < 0:
        parts.append(f"NNT(evento ridotto) {1/abs(lo):.1f}")
    return nnt, "l'IC della differenza include lo zero: IC dell'NNT = " + " → ∞ → ".join(parts) + \
        " (Altman 1998). Il beneficio/danno non è statisticamente distinguibile dal nulla."


def _label_direction(diff, event):
    """Spiega cosa significa il segno della differenza a seconda che l'evento
    sia indesiderato (default: morte, ricaduta, effetto avverso, fallimento)
    o desiderato (guarigione, risposta)."""
    if diff == 0:
        return "nessuna differenza"
    reduces = diff < 0
    if event == "undesirable":
        return ("l'intervento RIDUCE l'evento → beneficio, NNTB" if reduces
                else "l'intervento AUMENTA l'evento → danno, NNTH")
    return ("l'intervento RIDUCE l'evento desiderato → danno, NNTH" if reduces
            else "l'intervento AUMENTA l'evento desiderato → beneficio, NNTB")


def mode_table(args):
    ei, ni, ec, nc = args.ei, args.ni, args.ec, args.nc
    if ei > ni or ec > nc or min(ni, nc) <= 0:
        sys.exit("Errore: eventi > totale o totale nullo.")
    warnings = []
    a, b, c, d = ei, ni - ei, ec, nc - ec
    if min(a, b, c, d) < 5:
        warnings.append("Almeno una cella ha meno di 5 osservazioni: per RR e OR è stata "
                        "aggiunta la correzione di continuità 0,5; le stime sono instabili.")
    if min(a, b, c, d) == 0 or min(a, b, c, d) < 5:
        a2, b2, c2, d2 = a + 0.5, b + 0.5, c + 0.5, d + 0.5
    else:
        a2, b2, c2, d2 = a, b, c, d
    ri, rc = ei / ni, ec / nc
    diff = ri - rc
    se_diff = math.sqrt(ri * (1 - ri) / ni + rc * (1 - rc) / nc)
    d_lo, d_hi = diff - Z95 * se_diff, diff + Z95 * se_diff
    rr = (a2 / (a2 + b2)) / (c2 / (c2 + d2))
    se_lnrr = math.sqrt(1 / a2 - 1 / (a2 + b2) + 1 / c2 - 1 / (c2 + d2))
    rr_lo, rr_hi = _ci_log(rr, se_lnrr)
    orr = (a2 * d2) / (b2 * c2)
    se_lnor = math.sqrt(1 / a2 + 1 / b2 + 1 / c2 + 1 / d2)
    or_lo, or_hi = _ci_log(orr, se_lnor)
    nnt, nnt_ci = _nnt_from_diff(diff, d_lo, d_hi)
    out = {
        "input": {"eventi_intervento": ei, "n_intervento": ni, "eventi_controllo": ec, "n_controllo": nc,
                  "evento": args.event},
        "rischio_intervento": ri, "rischio_controllo": rc,
        "differenza_assoluta": diff, "differenza_ic95": [d_lo, d_hi],
        "differenza_per_1000": diff * 1000,
        "RR": rr, "RR_ic95": [rr_lo, rr_hi],
        "OR": orr, "OR_ic95": [or_lo, or_hi],
        "NNT": nnt, "NNT_ic95": nnt_ci,
        "direzione": _label_direction(diff, args.event),
        "avvertenze": warnings + [
            "Valido per un singolo studio o una 2x2 già aggregata dagli autori: non sommare studi diversi."],
    }
    return out


def _risk_from_relative(measure, value, p0):
    if measure == "RR":
        return p0 * value
    if measure == "OR":
        return (value * p0) / (1 - p0 + value * p0)
    if measure == "HR":
        return 1 - (1 - p0) ** value
    raise ValueError(measure)


def mode_relative(args):
    p0 = args.baseline
    if not 0 < p0 < 1:
        sys.exit("Errore: --baseline è una proporzione tra 0 e 1 (es. 0.45 per 45%).")
    lo, hi = args.ci if args.ci else (None, None)
    p1 = _risk_from_relative(args.measure, args.value, p0)
    diff = p1 - p0
    res = {
        "input": {"misura": args.measure, "valore": args.value, "ic95": args.ci, "rischio_base": p0,
                  "evento": args.event},
        "rischio_controllo": p0, "rischio_intervento": p1,
        "differenza_assoluta": diff, "differenza_per_1000": diff * 1000,
        "direzione": _label_direction(diff, args.event),
    }
    if lo is not None:
        p1_lo, p1_hi = _risk_from_relative(args.measure, lo, p0), _risk_from_relative(args.measure, hi, p0)
        d_lo, d_hi = min(p1_lo, p1_hi) - p0, max(p1_lo, p1_hi) - p0
        res["differenza_ic95"] = [d_lo, d_hi]
        nnt, nnt_ci = _nnt_from_diff(diff, d_lo, d_hi)
        res["NNT"], res["NNT_ic95"] = nnt, nnt_ci
    else:
        res["NNT"] = (1 / abs(diff)) if diff else None
        res["NNT_ic95"] = "IC non calcolabile senza l'IC della misura relativa"
    res["avvertenze"] = [
        "Il rischio di base determina l'effetto assoluto: dichiara sempre da dove viene "
        "(gruppo di controllo della revisione, registro, popolazione dell'utente).",
        "Con HR l'approssimazione assume rischi proporzionali e un orizzonte temporale definito.",
        "Con OR e rischi di base alti (> 20%) l'OR sovrastima il RR: non leggerlo come rischio relativo.",
    ]
    return res


def mode_nnt(args):
    arr = args.arr
    lo, hi = args.ci if args.ci else (arr, arr)
    nnt, nnt_ci = _nnt_from_diff(arr, lo, hi)
    return {"input": {"differenza_assoluta": arr, "ic95": args.ci},
            "NNT": nnt, "NNT_ic95": nnt_ci,
            "avvertenze": ["Nel testo l'NNT è un numero di persone: riportalo intero. Convenzione prudente: "
                           "arrotonda per eccesso (6,7 → 7)."]}


def mode_smd(args):
    d = args.value
    ad = abs(d)
    if ad < 0.2:
        size = "trascurabile (< 0,2)"
    elif ad < 0.5:
        size = "piccolo (0,2–0,5)"
    elif ad < 0.8:
        size = "medio (0,5–0,8)"
    else:
        size = "grande (≥ 0,8)"
    # Chinn 2000: ln(OR) ≈ d·π/√3 ; probabilità di superiorità = Φ(d/√2)
    ln_or = d * math.pi / math.sqrt(3)
    cles = 0.5 * (1 + math.erf(d / math.sqrt(2) / math.sqrt(2)))
    return {"input": {"SMD": d},
            "grandezza_convenzionale": size,
            "OR_equivalente_approssimato": math.exp(ln_or),
            "probabilita_di_superiorita": cles,
            "avvertenze": [
                "Le soglie di Cohen (0,2/0,5/0,8) sono convenzioni generiche: in molti campi un SMD di 0,3 "
                "è già rilevante, in altri 0,5 non supera la MCID. Riporta l'SMD accanto alla MCID "
                "dell'outcome, se nota.",
                "Probabilità di superiorità = probabilità che una persona presa a caso nel gruppo "
                "intervento abbia un esito migliore di una presa a caso nel gruppo controllo.",
            ]}


def _pct(x):
    return f"{x*100:.1f}%"


def print_human(res, mode):
    print("=" * 72)
    print(f"effetti.py — modalità {mode}")
    print("=" * 72)
    print("Input:", json.dumps(res["input"], ensure_ascii=False))
    print("-" * 72)
    if "rischio_controllo" in res:
        print(f"Rischio nel controllo   : {_pct(res['rischio_controllo'])}")
        print(f"Rischio nell'intervento : {_pct(res['rischio_intervento'])}")
        d = res["differenza_assoluta"]
        line = f"Differenza assoluta     : {d*100:+.1f} punti percentuali ({d*1000:+.0f} per 1000)"
        if "differenza_ic95" in res:
            lo, hi = res["differenza_ic95"]
            line += f"  IC95% [{lo*100:+.1f}; {hi*100:+.1f}] pp"
        print(line)
    if "RR" in res:
        print(f"RR                      : {res['RR']:.3f}  IC95% [{res['RR_ic95'][0]:.3f}; {res['RR_ic95'][1]:.3f}]")
        print(f"OR                      : {res['OR']:.3f}  IC95% [{res['OR_ic95'][0]:.3f}; {res['OR_ic95'][1]:.3f}]")
    if "NNT" in res:
        n = res["NNT"]
        ntxt = f"{n:.1f} (nel testo: {round(n)}; per prudenza si arrotonda per eccesso: {math.ceil(n)})" if n else "non definito"
        print(f"NNT                     : {ntxt}")
        print(f"IC95% dell'NNT          : {res['NNT_ic95']}")
    if "direzione" in res:
        print(f"Lettura                 : {res['direzione']}")
    if "grandezza_convenzionale" in res:
        print(f"Grandezza convenzionale : {res['grandezza_convenzionale']}")
        print(f"OR equivalente (approx) : {res['OR_equivalente_approssimato']:.2f}")
        print(f"Prob. di superiorità    : {_pct(res['probabilita_di_superiorita'])}")
    print("-" * 72)
    for w in res.get("avvertenze", []):
        print("! " + w)


def main():
    p = argparse.ArgumentParser(description="Calcoli deterministici di efficacia reale (vedi docstring).")
    sub = p.add_subparsers(dest="mode", required=True)

    t = sub.add_parser("table", help="tabella 2x2 di un singolo studio")
    t.add_argument("--ei", type=int, required=True, help="eventi nel gruppo intervento")
    t.add_argument("--ni", type=int, required=True, help="totale nel gruppo intervento")
    t.add_argument("--ec", type=int, required=True, help="eventi nel gruppo controllo")
    t.add_argument("--nc", type=int, required=True, help="totale nel gruppo controllo")
    t.add_argument("--event", choices=["undesirable", "desirable"], default="undesirable",
                   help="l'evento contato è indesiderato (default) o desiderato")

    r = sub.add_parser("relative", help="da RR/OR/HR + rischio di base")
    r.add_argument("--measure", choices=["RR", "OR", "HR"], required=True)
    r.add_argument("--value", type=float, required=True)
    r.add_argument("--ci", type=float, nargs=2, metavar=("LO", "HI"))
    r.add_argument("--baseline", type=float, required=True, help="rischio nel gruppo di controllo (0-1)")
    r.add_argument("--event", choices=["undesirable", "desirable"], default="undesirable")

    n = sub.add_parser("nnt", help="da una differenza assoluta di rischio")
    n.add_argument("--arr", type=float, required=True, help="differenza assoluta (intervento - controllo), es. -0.15")
    n.add_argument("--ci", type=float, nargs=2, metavar=("LO", "HI"))

    s = sub.add_parser("smd", help="interpreta una differenza media standardizzata")
    s.add_argument("--value", type=float, required=True)

    p.add_argument("--json", action="store_true", help="output JSON")
    args = p.parse_args()

    fn = {"table": mode_table, "relative": mode_relative, "nnt": mode_nnt, "smd": mode_smd}[args.mode]
    res = fn(args)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print_human(res, args.mode)


if __name__ == "__main__":
    main()

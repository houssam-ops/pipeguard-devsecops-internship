# Recovered execution-guide excerpt; see docs/source-provenance.md.
import json
from statistics import mean
from datetime import datetime

def load_kpi_log(path="kpi_log.json"):
    with open(path) as f:
        return json.load(f)

def compute_mttd_mttr(entries):
    mttd_values, mttr_values = [], []
    for e in entries:
        if e.get("t_attack") and e.get("t_alert"):
            t_attack = datetime.fromisoformat(e["t_attack"])
            t_alert = datetime.fromisoformat(e["t_alert"])
            mttd_values.append((t_alert - t_attack).total_seconds())
        if e.get("t_alert") and e.get("t_remediation"):
            t_alert = datetime.fromisoformat(e["t_alert"])
            t_remediation = datetime.fromisoformat(e["t_remediation"])
            mttr_values.append((t_remediation - t_alert).total_seconds())
    return {
        "mttd_moyen_s": round(mean(mttd_values), 2) if mttd_values else None,
        "mttr_moyen_s": round(mean(mttr_values), 2) if mttr_values else None,
        "n_scenarios": len(entries),
    }

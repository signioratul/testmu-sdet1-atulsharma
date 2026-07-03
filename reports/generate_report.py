import json
from datetime import datetime
from pathlib import Path

report = {
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

files = {
    "login_testcases": "reports/login_testcases.json",
    "ui_validation": "reports/ui_validation.json",
    "api_validation": "reports/api_validation.json"
}

for key, file in files.items():
    path = Path(file)
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            report[key] = json.load(f)
    else:
        report[key] = "Not Generated"

with open("reports/final_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)

print("Final report created.")
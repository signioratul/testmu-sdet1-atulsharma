import json
from datetime import datetime
from pathlib import Path

report = {
    "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
}

# Read generated files
files = {
    "generated_testcases": "reports/login_testcases.json",
    "ui_validation": "reports/ui_validation.json",
    "api_validation": "reports/api_validation.json"
}

for key, file in files.items():
    path = Path(file)

    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            report[key] = json.load(f)
    else:
        report[key] = None

# Check screenshots
dashboard_exists = Path("screenshots/dashboard.png").exists()
dashboard_navigation_exists = Path(
    "screenshots/dashboard_navigation.png"
).exists()

report["artifacts"] = {
    "dashboard.png": dashboard_exists,
    "dashboard_navigation.png": dashboard_navigation_exists
}

# Pipeline status
report["pipeline"] = {
    "login_test": "PASS" if dashboard_exists else "FAIL",
    "dashboard_test": "PASS" if dashboard_navigation_exists else "FAIL",
    "ui_validation": (
        report["ui_validation"]["status"]
        if report["ui_validation"]
        else "FAIL"
    ),
    "api_validation": (
        report["api_validation"]["status"]
        if report["api_validation"]
        else "FAIL"
    )
}

# Overall status
if all(value == "PASS" for value in report["pipeline"].values()):
    report["overall_status"] = "PASS"
else:
    report["overall_status"] = "FAIL"

# Save report
with open("reports/final_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, indent=4)

print("Final report created successfully.")
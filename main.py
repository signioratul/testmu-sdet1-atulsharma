import subprocess
import sys
from datetime import datetime
import time

start = time.time()

python = sys.executable

steps = [
    ("Generate Test Cases",
     [python, "-m", "ai.generate_tests"]),

    # ("Generate Playwright Test",
    #  [python, "-m", "ai.generate_playwright"]),

    # ("Generate Dashboard Playwright",
    #  [python, "-m", "ai.generate_dashboard"]),

    ("Execute Generated Login Test",
     [python, "-m", "pytest", "tests/generated_login.py", "-v"]),

    ("Execute Generated Dashboard Test",
     [python, "-m", "pytest", "tests/generated_dashboard.py", "-v"]),

    ("Validate UI",
     [python, "-m", "ai.validate_ui"]),

    ("Validate API",
     [python, "-m", "ai.validate_api"]),

    ("Generate Final Report",
     [python, "-m", "reports.generate_report"])
]

completed = []
failed_step = None

print("=" * 70)
print("AI QA AUTOMATION PIPELINE")
print("=" * 70)

for title, command in steps:

    print(f"\n[{datetime.now().strftime('%H:%M:%S')}] {title}")
    print("-" * 70)
    print("Running:", " ".join(command))

    try:
        subprocess.run(command, check=True)

        print(f"✓ {title} completed.")
        completed.append(title)

    except subprocess.CalledProcessError as e:

        failed_step = title
        print(f"✗ {title} failed.")
        print(f"Exit Code: {e.returncode}")
        break

print("\n" + "=" * 70)
print("PIPELINE SUMMARY")
print("=" * 70)

for step in completed:
    print(f"✓ {step}")

if failed_step:
    print(f"\n✗ Failed Step: {failed_step}")
    print("Pipeline terminated.")
else:
    print("\n✓ AI QA Pipeline completed successfully!")

end = time.time()
print(f"\nExecution Time: {end - start:.2f} seconds")
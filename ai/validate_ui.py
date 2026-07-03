# ============================================================================
# Task 3 - Option A: Failure Explainer
#
# This implementation uses an LLM to analyze the captured UI screenshot and
# generate a structured PASS/FAIL assessment with detected issues.
#
# Option A was selected because it provides immediate, human-readable feedback
# that helps QA engineers quickly understand UI failures without manually
# inspecting screenshots.
# ============================================================================

from PIL import Image
from utils.gemini_client import client
import json

image = Image.open("screenshots/dashboard.png")

prompt = """
You are a QA Engineer.

Inspect this dashboard screenshot.

Verify

- Dashboard heading
- Left menu
- Search box
- User profile
- No visible error messages

Return JSON only.

Return ONLY JSON

{
"status":"",
"issues":[]
}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        prompt,
        image
    ]
)

text = response.text.replace("```json","").replace("```","").strip()

data = json.loads(text)

with open("reports/ui_validation.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(json.dumps(data, indent=4))
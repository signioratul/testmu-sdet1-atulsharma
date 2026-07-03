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
    model="gemini-flash-latest",
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
import requests
import json
from utils.gemini_client import client

response = requests.get(
    "https://jsonplaceholder.typicode.com/users/1"
)

prompt = f"""
Validate this API response.

Expected

id

name

email

Response

{json.dumps(response.json(), indent=2)}

Return ONLY JSON

{{
  "status": "PASS",
  "missing_fields": [],
  "warnings": [],
  "summary": ""
}}
"""

reply = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

text = reply.text.replace("```json", "").replace("```", "").strip()

data = json.loads(text)

with open("reports/api_validation.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print(json.dumps(data, indent=4))
from utils.gemini_client import client

for model in client.models.list():
    if "generateContent" in model.supported_actions:
        print(model.name)
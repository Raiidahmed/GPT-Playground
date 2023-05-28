import openai
openai.api_key = "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"  # supply your API key however you choose

image_resp = openai.Image.create(prompt="Raiid Ahmed", n=4, size="512x512")

print(image_resp)
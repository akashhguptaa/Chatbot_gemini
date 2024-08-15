import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.environ.get("API_KEY"))

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config
)

chat_session = model.start_chat(
  history=[
  ]
)

def gemini_data(prompt):
  response = chat_session.send_message(prompt, stream=True)
  for chunks in response:
    data  = chunks.text.replace("*", "")
    # print(data)
  return response.text.replace("*", "")



import google.generativeai as genai

# Configure API key
genai.configure(api_key="..........")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session
chat = model.start_chat()

# Send a message
response = chat.send_message("What is programming?")

# Print response
print(response.text)

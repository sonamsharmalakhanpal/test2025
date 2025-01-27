import google.generativeai as genai

genai.configure(api_key="AIzaSyCLd9uiYyaHuvB3NKkUASYNngEIyuhOBFg")
model = genai.GenerativeModel("gemini-1.5-flash")
# response = model.generate_content("Explain how AI works")
response = model.generate_content("Write Python code using Selenium to Open Naukri.com.")
print("Calling the model...")
print(response.text)
print("End of response.")
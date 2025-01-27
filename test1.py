from transformers import pipeline

def generate_code(prompt):
    try:
        # Load the Hugging Face text generation pipeline
        code_generator = pipeline("text-generation", model="gpt2")
        result = code_generator(prompt, max_length=200, truncation=True, num_return_sequences=1)
        return result[0]["generated_text"]
    except Exception as e:
        return f"An error occurred: {e}"

# Define the task
prompt = """
Write Python code using Selenium to:
1. Open Naukri.com.
"""
generated_code = generate_code(prompt)
print("Generated Code:\n", generated_code)

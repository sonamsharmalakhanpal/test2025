# This is a sample Python script.
from transformers import pipeline

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def generate_code(prompt):
    # Load the Hugging Face text generation pipeline
    code_generator = pipeline("text-generation", model="gpt2")
    result = code_generator(prompt, max_length=200, num_return_sequences=1)
    return result[0]["generated_text"]

# Define the task
prompt = """
Write Python code using Selenium to:
1. Open Naukri.com.
"""
generated_code = generate_code(prompt)
print("Generated Code:\n", generated_code)
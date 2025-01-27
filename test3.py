from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Load the model and tokenizer
model_name = "openai/gpt-3.5-turbo"  # Use a code-generation model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Step 2: Define the prompt
prompt = "Write Python code to log in to Naukri.com using Selenium:\n\n"

# Step 3: Tokenize the input prompt
inputs = tokenizer(prompt, return_tensors="pt")

# Step 4: Generate the code
outputs = model.generate(inputs["input_ids"],num_return_sequences=1, temperature=0.7, max_length=2000)

# Step 5: Decode the generated text
generated_code = tokenizer.decode(outputs[0], skip_special_tokens=True)

print("Generated Code:\n")
print(generated_code)

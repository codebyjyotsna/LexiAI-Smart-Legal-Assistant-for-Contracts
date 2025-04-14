from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load T5 model and tokenizer
model_name = "t5-small"  # Change to "t5-large" or "google/t5-v1_1-large" for better accuracy
model = T5ForConditionalGeneration.from_pretrained(model_name)
tokenizer = T5Tokenizer.from_pretrained(model_name)

def process_contract(content):
    text = content.decode('utf-8')  # Decode bytes to string
    input_text = "summarize: " + text

    # Tokenize input
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)

    # Generate summary
    outputs = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return summary

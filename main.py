from transformers import pipeline

genearator = pipeline('text-generation', model='distilgpt2')

result = genearator(
    "Ai is the future because", 
    max_length=50,
    num_return_sequences=1
)

print(result[0]['generated_text'])
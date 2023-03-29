# ! pip3 install transformers
# or
# ! pip install transformers
from transformers import pipeline
generator = pipeline('text-generation', model='openai-gpt')
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
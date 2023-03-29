# Learning about [Hugging Face](https://huggingface.co/)

Try out [ML](https://github.com/hchiam/learning-ml) models quickly with existing models, datasets, spaces (spaces are interactive demos), and more: https://huggingface.co

Just one of the things I'm learning. https://github.com/hchiam/learning

## Quick minimal example of using a model

You can get started quickly with a model you find on Hugging Face, like this model: https://huggingface.co/openai-gpt#how-to-get-started-with-the-model

Consider copying the following code into a Google Colab to run on the cloud instead of on your computer: https://colab.research.google.com

```py
! pip install transformers
from transformers import pipeline
generator = pipeline('text-generation', model='openai-gpt')
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
```

## More examples

```py
# install dependencies:
! pip install transformers
from transformers import pipeline

# download models:
generator_gpt2 = pipeline('text-generation', model='gpt2') # https://huggingface.co/gpt2
generator_openai = pipeline('text-generation', model='openai-gpt') # https://huggingface.co/openai-gpt
classifier = pipeline("sentiment-analysis")

# actually use models:
print(generator_gpt2("Hello, I'm a language model,", max_length=30, num_return_sequences=5))
print(generator_openai("Hello, I'm a language model,", max_length=30, num_return_sequences=5))
print(classifier("We are very happy to show you the 🤗 Transformers library."))
```

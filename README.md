# Learning about [Hugging Face](https://huggingface.co/)

Just one of the things I'm learning. https://github.com/hchiam/learning

Try out [ML](https://github.com/hchiam/learning-ml) models quickly with existing models, datasets, spaces (spaces are interactive demos), and more: https://huggingface.co

- Live demos: https://huggingface.co/spaces 
   - For example: https://huggingface.co/spaces/DilshanKavinda/Comment_Analysis_App -> click on "Files" to see the files used to make the demo. 

## Quick minimal example of using a model

You can get started quickly with a model you find on Hugging Face, like this model: https://huggingface.co/openai-gpt#how-to-get-started-with-the-model

Consider copying the following code into a Google Colab to run on the cloud instead of on your computer: https://colab.research.google.com

```py
! pip install transformers torch tensorflow
from transformers import pipeline
generator = pipeline('text-generation', model='openai-gpt')
generator("Hello, I'm a language model,", max_length=30, num_return_sequences=5)
```

If you're doing this on your own computer, consider instead running `pip3 install transformers torch tensorflow`.

## More examples

```py
# install dependencies:
! pip install transformers torch tensorflow
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

## more stuff to try later

Multiple choice quiz to check your understanding of the Hugging Face docs on Transformers: https://huggingface.co/course/chapter1/10?fw=pt

Multiple choice quiz to check your understanding of the Hugging Face docs on NLP tasks: https://huggingface.co/course/chapter7/9?fw=pt

Extractive question answering from context/document - NLP task: https://huggingface.co/course/chapter7/7?fw=pt#using-the-fine-tuned-model

```sh
pip install huggingface_hub
huggingface-cli login
huggingface-cli repo create repo_name --type {model, dataset, space}

git lfs install
git clone https://huggingface.co/username/repo_name
git add .
git commit -m "commit from $USER"
git push
```

```py
tokenizer = AutoTokenizer.from_pretrained("username/repo_name")
model = AutoModel.from_pretrained("username/repo_name")
```

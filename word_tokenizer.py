import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

text = "Natural Language Processing is amazing."

tokens = word_tokenize(text)

print(tokens)
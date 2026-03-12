import nltk
from nltk.tokenize import sent_tokenize

nltk.download("punkt")

text = """
NLP is a part of AI.
It helps computers understand language.
"""

sentences = sent_tokenize(text)

print(sentences)
import re

def simple_tokenizer(text):
    
    text = text.lower()
    
    tokens = re.findall(r"\b\w+\b", text)
    
    return tokens


if __name__ == "__main__":
    
    sample = "NLP makes machines understand text."
    
    print(simple_tokenizer(sample))
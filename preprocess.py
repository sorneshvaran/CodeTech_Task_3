import spacy
import string
from spacy.lang.en.stop_words import STOP_WORDS

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading 'en_core_web_sm' model for spaCy as it is not found...")
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    clean_tokens = []
    for token in doc:
        if token.text not in string.punctuation and token.text.lower() not in STOP_WORDS:
            clean_tokens.append(token.lemma_.lower())
    return " ".join(clean_tokens)
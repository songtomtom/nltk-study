import sys

import nltk


def pos_tag_sentence(sentence):
    tokens = nltk.word_tokenize(sentence)
    tagged = nltk.pos_tag(tokens)
    return tagged

if __name__ == "__main__":
    if len(sys.argv) > 1:
        sentence = " ".join(sys.argv[1:])
        tagged_sentence = pos_tag_sentence(sentence)
        print("POS Tagging Result:")
        for word, tag in tagged_sentence:
            print(f"{word}: {tag}")
    else:
        print("Usage: python script_name.py Your sentence here.")
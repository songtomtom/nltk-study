import nltk
from nltk.corpus import wordnet as wn

# nltk의 wordnet을 사용하기 위해 필요한 리소스 다운로드
nltk.download('wordnet')

# Extract all unique lemma names (nouns) from WordNet
nouns = set(lemma.name() for synset in wn.all_synsets('n') for lemma in synset.lemmas())

irregular_plurals = []

# This is a simplistic check and won't cover all cases or nuances.
for noun in nouns:
    if not noun.endswith('s'):
        # We try to find a plural form in the lemma names.
        # This won't catch all irregular plurals, especially those that don't change form.
        assumed_plural = noun + 's'
        if assumed_plural not in nouns:
            assumed_plural_es = noun + 'es'
            if assumed_plural_es not in nouns:
                irregular_plurals.append(noun)

# Print a subset of the findings
print(irregular_plurals[:10])

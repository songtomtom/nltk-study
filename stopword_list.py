import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load stop words
stop_words = set(stopwords.words('english'))

# Sort stop words alphabetically
sorted_stop_words = sorted(stop_words)

# Calculate the number of stop words
num_stop_words = len(sorted_stop_words)

# Print the sorted stop words
for word in sorted_stop_words:
    print(word)

# Print the number of stop words
print("Number of stop words: ", num_stop_words)

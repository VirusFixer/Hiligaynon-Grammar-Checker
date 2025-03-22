import nltk
from nltk.tokenize import word_tokenize

# Sample list of Hiligaynon words and their associated POS tags
hiligaynon_vocab = {
    "balay": "NOUN",       # house
    "bata": "NOUN",        # child
    "magluto": "VERB",     # to cook
    "nagbakal": "VERB",    # bought
    "matahum": "ADJ",      # beautiful
    "daku": "ADJ",         # big
    "dali": "ADV",         # quickly
    "madamo": "ADV",       # a lot
    "ako": "PRON",         # I
    "ikaw": "PRON",        # you
    "sa": "PREP",          # in
    "kag": "CONJ",         # and
    "mag-": "PART",        # verb focus marker (future tense)
    "nag-": "PART",        # verb focus marker (past tense)
    "ma": "PART",          # veb focus marker (future tense)
    "-on": "PART",         # verb focus marker (object focus)
    "-an": "PART"          # verb focus marker (location focus)
}

# Step 2: Define a function to tag words based on the vocabulary
def hiligaynon_pos_tagging(text):
    # Tokenize the input text (split into words)
    tokens = word_tokenize(text)
    
    # Initialize an empty list to store the tagged words
    tagged_words = []
    
    # Tag each word based on the vocabulary dictionary
    for word in tokens:
        # Convert the word to lowercase to handle case variations
        word_lower = word.lower()
        
        # Check if the word exists in the predefined vocabulary and tag accordingly
        if word_lower in hiligaynon_vocab:
            tagged_words.append((word, hiligaynon_vocab[word_lower]))
            
        else:
            # If the word isn't found, mark it as unknown
            tagged_words.append((word, "UNK"))
    
    return tagged_words


sentence = "ma bakal"

tagged_output = hiligaynon_pos_tagging(sentence)
print(tagged_output)
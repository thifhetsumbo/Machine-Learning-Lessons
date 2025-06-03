# Compulsory Task 1
# Import the spaCy library
import spacy
# Load a pre-trained English NLP model
nlp = spacy.load('en_core_web_sm')

"""Find at least 2 garden path sentences from the web, or think up your own.

 "The horse raced past the barn fell."

 "We painted the wall with cracks."

Store the sentences you have identified or created in a list called garden path Sentences.
"""

# Store the garden path sentence to the list of garden path sentences
garden_path_sentences = [
    "The horse raced past the barn fell.",
   "We painted the wall with cracks."
]

"""Add the following sentences to your list:

Mary gave the child a Band-Aid.

That Jill is never here hurts.

The cotton clothing is made of grows in Mississippi.
"""

# New sentences to be added
additional_sentences = [
    "Mary gave the child a Band-Aid.",
    "That Jill is never here hurts.",
    "The cotton clothing is made of grows in Mississippi."
]
# Add the new sentences to the list
garden_path_sentences.extend(additional_sentences)

"""Tokenise each sentence in the list, and perform named entity recognition."""

# Iterate through each sentence in the list garden_path_sentences
for sentence in garden_path_sentences:
  # Display the current sentence being processed
    print(f"\nSentence: {sentence}")
    # Use the loaded nlp spaCy model
    doc = nlp(sentence)
    # Display tokenization header
    print("Tokens:")
    # Dispaly both the token content and its unique internal ID
    print([(token, token.orth_, token.orth) for token in doc])
    # Display the token text excluding punctuation and whitespace
    print([token.orth_ for token in doc if not token.is_punct | token.is_space])
    # Display blank line for cleaner output
    print("\n")
    # Display named entity recognition header
    print("Named Entity:")
    # Display entity text, string label and internal ID
    print([(i, i.label_, i.label) for i in doc.ents])

"""Examine how spaCy has categorised each sentence. Then, use spacy.explain to look up and print the meaning of entities that you don’t understand."""

entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

"""At the bottom of your file, write a comment about two entities that you looked up. For each entity answer the following questions:

What was the entity and its explanation that you looked up?

Did the entity make sense in terms of the word associated with it

Entity 1:

Mary is identified as a person, which makes sense. "Mary" is a proper name for an individual, so labelling it as a PERSON is entirely appropriate and expected. SpaCy correctly recognises it as a named entity referring to a human.

Entity 2:

Mississippi is categorised as a GPE, which stands for "Geopolitical Entity." SpaCy defines a GPE as encompassing countries, cities, and states. This classification is appropriate because, in the sentence, "The cotton clothing is made of cotton that grows in Mississippi," "Mississippi" refers to a U.S. state, which is indeed a geopolitical location. Thus, SpaCy correctly identifies it as a GPE.
"""
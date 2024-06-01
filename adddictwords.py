# Define an empty dictionary
custom_dictionary = {}

# Function to add a word and its meaning to the dictionary
def add_word(word, meaning):
    custom_dictionary[word] = meaning
    print(f"'{word}' added to the dictionary with meaning: '{meaning}'")

# Function to display the entire dictionary
def display_dictionary():
    print("Custom Dictionary:")
    for word, meaning in custom_dictionary.items():
        print(f"{word}: {meaning}")

# Add words and meanings to the dictionary
add_word("apple", "a round fruit with red or green skin and a whitish interior")
add_word("banana", "a long curved fruit that grows in clusters and has soft pulpy flesh and yellow skin when ripe")
add_word("orange", "a round juicy citrus fruit with a tough bright reddish-yellow rind")

# Display the dictionary
display_dictionary()

# Add more words dynamically
add_word("grape", "a small round juicy fruit with a smooth skin, typically green, purple, or red, growing in clusters on a grapevine")
add_word("pineapple", "a large juicy tropical fruit consisting of aromatic edible yellow flesh surrounded by a tough segmented skin and topped with a tuft of stiff leaves.")

# Display the updated dictionary
display_dictionary()

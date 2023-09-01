"""
Class: CIT 95
Name: Mark Edmunds
Assignment: GitHub classroom program two
August 31, 2023
"""

TEXT = "Python is an amazing programming language. It is versatile, easy to learn, and powerful."


# Strings
# Length Calculation
def calculate_length(text: str):
    print(f"The number of characters ins the string is: {len(text)}")
    return len(text)


calculate_length(TEXT)
# Uppercase and Lowercase Conversion
upper_lower = f"{TEXT.upper()} {TEXT.lower()}"
print(upper_lower)
# Word Count
word_count = len((TEXT.split()))
print(word_count)
# Substring Extraction:
string_length = len(TEXT)
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))
if start < end and end <= string_length - 1:
    print(TEXT[start:end: 1])
elif start > end and start <= string_length - 1:
    print(TEXT[start:end: -1])
else:
    print("out of range")
# Word Replacement
word_to_replace = input("What word would you like to replace?: ")
replacement_word = input(f"What would you like to replace '{word_to_replace}' with?: ")
print(TEXT.replace(word_to_replace, replacement_word))

# Whitespace Removal
print(TEXT.strip())


# Splitting into Sentences
def split_sentences(text):
    sentence_list = text.split(".")
    sentence_list.remove("")
    return sentence_list


print(split_sentences(TEXT))
# Word Reversal
for word in TEXT.split():
    newWord = word.replace(",", "")
    newWord = newWord.replace(".", "")
    print(newWord[::-1])

# Character Count
character_count = input("What character do you want to count?: ")
while len(character_count) > 1:
    character_count = input("Enter 1 character")
print(TEXT.count(character_count))
# Substring Count
sub_string = input("What substring do you want to count: ")
print(TEXT.count(sub_string))

# Lists
# List Creation
word_list = TEXT.split()
print(word_list)
# Appending
word_list.append("Pythonic")
print(word_list)
# Insertion
word_list.insert(0, "awesome")
print(word_list)
# Indexing and Slicing
print(word_list[2])
print(word_list[5:8:1])
# Removal
word_list.remove("amazing")
print(word_list)
# Sorting
sorted_list = word_list.copy()
sorted_list.sort(key=str.lower)
print(sorted_list)

# Counting
print(word_list.count("is"))
# Joining
new_sentence = ""
print(word_list)
for word in word_list:
    print(word)
    new_sentence += f" {word}"
print(new_sentence)
# Reversal
word_list.reverse()
# Copying
new_list = word_list.copy()
print(new_list)

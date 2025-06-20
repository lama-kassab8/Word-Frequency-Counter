import string

print("Welcome to the Word Frequency Counter program!\n")
text = input("Type the text you want to use this program on:\n").lower().split()


cleaned_text = []
for word in text:
    cleaned_word = word.strip(string.punctuation)
    cleaned_text.append(cleaned_word)

word_counts = {}
for word in cleaned_text:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


print("\nWord Frequencies:\n")
for word, count in word_counts.items():
    if count >1:
        print(f"{word}: {count}")
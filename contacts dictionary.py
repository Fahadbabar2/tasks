sentence = input("Enter a sentence: ")
with open("output.txt", "w") as file:
    file.write(sentence)
print("Sentence written to output.txt")

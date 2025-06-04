file_path = "output.txt"  

with open(file_path, "r") as file:
    text = file.read()

words = text.split()
print("Number of words:", len(words))

score = 0

a = input("Capital of Pakistan ").lower()
if a == "Islamabad":
    score += 1

b = input("43 + 71 = ")
if b == "114":
    score += 1

c = input("Red + white = ").lower()
if c == "pink":
    score += 1

print("Score:", score)

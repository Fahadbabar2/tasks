def register(username, password):
    with open("users.txt", "a") as file:
        file.write(username + "," + password + "\n")
    print("User registered successfully.")

def login(username, password):
    with open("users.txt", "r") as file:
        for line in file:
            user, passw = line.strip().split(",")
            if user == username and passw == password:
                print("Login successful.")
                return
    print("Invalid username or password.")

register("fahad", "1234")
login("fahad", "1234")
login("bash", "wrongpass")

contacts = {}

while True:
    name = input("Enter name or stop to finish")
    if name.lower() == 'stop':
        break
    phone = input("Enter phone number: ")
    contacts[name] = phone

print("Contacts:")
for name, phone in contacts.items():
    print(name + ":", phone)

print("Sign up")
name = input("Enter a username you would like to use: ")
password = input("Enter a password: ")

print()
print()
print()

print("Now sign in")

tries = 0

while tries < 3:
    name1 = input("Enter your username: ")
    password1 = input("Enter your password: ")
    if name == name1 and password == password1:
        print("Login successful!")
        break
    else:
        print("Wrong username or password. Please try again.")
        tries += 1
if tries == 3:
    print("Maximum number of login attempts reached.")

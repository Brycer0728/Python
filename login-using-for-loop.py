def login(username: str, password: str) -> bool:
    is_authenticated = False

    if username == "admin" and password == "1234":
        is_authenticated = True

    return is_authenticated

user = input("Username: ")
password = input("Password: ")

is_authenticated = False
# range is 4 because the "start" is defaulted to 0 since its not specified. 0, 1, 2, 3, 4 so 5 attempts
for attempt in range(4):
    if login(user, password) == True:
        is_authenticated = True
        break
    else:
        print("Login failed, re-enter your credentials.")
        user = input("Username: ")
        password = input("Password: ")

print("Login successful." if is_authenticated else "Your account has been temporarily locked.")

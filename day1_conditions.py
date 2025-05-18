# Example 1 - Basic if
age = 27
if age >= 18:
    print("You are an adult.")

# ---

# Example 2 - if, else
age = 27
if age >= 18:
    print("Access Granted.")
else:
    print("Access Denied.")

# ---

# Example 3 - if, elif, else

temperature = 18

if temperature > 30:
    print("It's hot!")
elif temperature > 20:
    print("Nice Weather.")
elif temperature > 10:
    print("A bit chilly.")
else:
    print("It's cold!")

# ---

# Example 4 - Logical Operators

is_logged_in = True
is_admin = False

if is_logged_in and is_admin:
    print("Welcome, admin!")
elif is_logged_in:
    print("Welcome, user.")
else:
    print("Please, log in.")

# ---

# Challenge - login and password

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Access granted.")
else:
    print("Access denied.")

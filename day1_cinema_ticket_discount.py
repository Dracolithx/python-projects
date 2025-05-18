print("Ticket Entry Checker")

age = int(input("How old are you?: "))
ticket = input("Do you have a ticket?: yes/no ").lower()
is_student = input("Are you a student? yes/no ").lower()
is_accompanied = input("Are you accompanied? yes/no ").lower()


if age >= 16 and ticket == "yes":
    print("Entry allowed.")
if is_student == "yes" or is_accompanied == "yes":
    print("Discount applied.")
else:
    print("Entry Denied.")
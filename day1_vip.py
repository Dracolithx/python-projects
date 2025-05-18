input("Ticket Entry Checker")

age = int(input("How old are you?: "))
has_ticket = input("Do you have a ticket? yes/no ").lower()
is_vip = input("Are you a VIP? yes/no ").lower()

if is_vip == "yes":   # yes has to be in " "
    print("Welcome VIP! Access granted")
elif has_ticket == "yes" and age >= 18:   # yes has to be in " "
    print("Access Granted. Enjoy the event!")
else:
    print("Acess Denied.")

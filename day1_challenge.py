age = int(input("What's your age "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if has_ticket.lower() == "yes":
    has_ticket = True
else:
    has_ticket = False

if  age >= 18 and has_ticket:
    print("Full Access Granted")
elif age >= 13 and has_ticket:
    print ("Limited Access Granted")
else:
    print ("Access Denied – Too young")
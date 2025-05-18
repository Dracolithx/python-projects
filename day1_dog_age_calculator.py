print("🐶 Dog Age to Human Age Calculator")

dog_age = input("How old is your dog? ")

# Convert to integer
dog_age = int(dog_age)

# Dogs mature quickly: first year = 15 human years
if dog_age == 1:
    human_age = 15
elif dog_age == 2:
    human_age = 24
else:
    human_age = 24 + (dog_age - 2) * 5

print(f"Your dog is {human_age} human years old 🐾")

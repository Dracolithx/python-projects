print("🐶 Kalkulator wieku psa w ludzkich latach")

dog_age = input("Ile lat ma Twój pies? ")

# Konwersja na liczbę całkowitą
dog_age = int(dog_age)

# Psy szybko dorastają, więc pierwszy rok = 15 ludzkich lat
if dog_age == 1:
    human_age = 15
elif dog_age == 2:
    human_age = 24
else:
    human_age = 24 + (dog_age - 2) * 5

print(f"Twój pies ma {human_age} ludzkich lat 🐾")

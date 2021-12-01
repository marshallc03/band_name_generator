import random


print("Welcome to the Band Name Generator.")

city = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
color = input("What's your favorite color?\n")
animal = input("Favorite animal?\n")
season = input("Pick a season:\n")
month = input("Pick a month:\n")


print("Here are some band name options: \n")
print(random.choice([city, pet, color, animal, season, month]) + " " + random.choice([city, pet, color, animal, season, month]))
print(random.choice([city, pet, color, animal, season, month]) +  " " + random.choice([city, pet, color, animal, season, month]))
print(random.choice([city, pet, color, animal, season, month]) + " " + random.choice([city, pet, color, animal, season, month]))
print(random.choice([city, pet, color, animal, season, month]) + " " + random.choice([city, pet, color, animal, season, month]))
print(random.choice([city, pet, color, animal, season, month]) + " " + random.choice([city, pet, color, animal, season, month]))
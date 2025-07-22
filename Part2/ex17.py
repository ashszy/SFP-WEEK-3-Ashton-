# TODO: Refer to the objective and sample output and figure out your own code!
# Time to graduate :p

#Insert your code here
#1
import random
name = input("What is your name?")

#2 , 3 , 4
adjective = ['unequaled','curvy','outrageous','wicked','green','mean']
animal = ['ewe','otter','hyena','wolverine','parakeet','marten']

#5
random_codename = random.choice(adjective) + " " + random.choice(animal)

#6
lucky_number = random.randint(1,99)
lucky_number = str(lucky_number)

#7
print("Hello " + name + ". Your codename is " + random_codename + "and your lucky number is " + lucky_number + "!")


# print out each name in a list:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# compose a message to each magician:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# any lines of code after the for loop that are not indented are executed once without repetition:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
# as the next line isn't indented, it's printed only once:
print("Thank you, everyone. That was a great magic show!")

# not indenting line 24:
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")
# because the final value associated with magician is 'carolina', she is the only one who receives the
# "looking forward to the next trick" message.




pizzas = ['cheese', 'pepperoni', 'hawaiian']
for pizza in pizzas:
    print(pizza)

pizzas = ['cheese', 'pepperoni', 'hawaiian']
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza!")

pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(f"A {pet.title()} would make a great pet!")

pets = ['dog', 'cat', 'rabbit']
for pet in pets:
    print(f"A {pet.title()} would make a great pet!")
print("Any of these animals would be so much fun to have as a pet!")

# slicing a list:
# to output the first three elements in a list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# if you want the second, third and fourth items, you would start the slice at index 1 and end at index 4:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])
# if you remove the first index in a slice, Python automatically starts at the beginning of the list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])
# similarly, you can remove the second index if you want a slice that includes the end of the list:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])
# printing the names of the last three players:
# would continue to work as the list of players changes in size:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])
# looping through only the first three names:
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# copying a list:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favourite foods are:")
print(my_foods)
print("\nMy friend's favourite foods are:")
print(friend_foods)

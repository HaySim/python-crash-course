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

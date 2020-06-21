# if value of car is 'bmw', then the value is printed in uppercase.
# if value is anything other than 'bmw', it's printed in title case:
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car== 'btw':
        print(car.upper())
    else:
        print(car.title())

print("")

# (!=) means two values are not equal:
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print("")

# checking if a value is not in a list:
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

print("")

# Boolean value is either True or False.
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru') 

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("")

age = 19
if age>= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

print("")

# if-elif-else syntax.
age = 12
if age <4:
    print("Your admission cost is £0.")
elif age < 18:
    print("Your admission cost is £25.")
else:
    print("Your admission cost is £40")

# a more concise way to set the price inside the if-elif-else chain:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is £{price}.")

# use as many elif blocks in your code as you like.
# let's say anyone 65 or older pays half the regular admission, or £20:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is £{price}.")

# Python does not require an else block at the end of an if-elif chain but sometimes an else block is useful.
# omitting the else block:
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is £{price}.")

print("")

# testing multiple conditions using a series of simple if statements with no elif or else blocks:
# Python doesn't run any tests beyond the first test that passes in an if-elif-else chain.
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

print("")

alien_colour = ['green', 'red', 'yellow', 'blue']
if 'green' in alien_colour:
    print("Player earned 5 points.")
print("\nYou win!")

colour = "green"
if "green" in colour:
    points = 10
if "red" in colour:
    points = 5
if "yellow" in colour:
    points = 1
if "blue" in colour:
    points = 1
print(f"You win {points} points!") 

print("")

colour = "green"
if "green" in colour:
    points = 10
elif "red" in colour:
    points = 5
else:
    points = 1
print(f"You win {points} points!") 

print("")

age = 10
if age < 2:
    message = "Person is a baby."
elif age >2 :
    message = "Person is a toddler." 
elif age > 4 : 
    message = "Person is a child."
elif age > 13:
    message =  "Person is a teenager."
else:
    message = "Person is an adult."
print(f"{message}")

print("")

# checking for special items:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

print("")

# checking that a list is not empty:
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

print("")

# using multiple lists:
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")


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
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0['colour'])
print(alien_0['points'])

print("")

# accessing values in a dictionary:
# will print 'green'.
alien_0 = {'colour': 'green'}
print(alien_0['colour'])

print("")

# you can have an unlimited number of key-value pairs in a dictionary.
alien_0 = {'colour': 'green', 'points': 5}

alien_0 = {'colour': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print("")

# adding new key-value pairs:
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# starting with an empty dictionary:
alien_0 = {}

alien_0['colour'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values in a dictionary:
alien_0 = {'colour': 'green'}
print(f"The alien is {alien_0['colour']}.")

alien_0['colour'] = 'yellow'
print(f"The alien is now {alien_0['colour']}.")

print("")

# a more interesting example tracking the position of an alien that can move at different speeds:
alien_0 = {'x_position': 0, 'y-position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# move alien to the right.
# determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # this must be a fast alien.
    x_increment = 3
# the new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

print("")

# removing key-value pairs:
alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)
del alien_0['points'] # be aware that the deleted key-value pair is removed permanently.
print(alien_0) 

print("")

# a dictionary is useful for storing the results of a simple poll:
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favourite_languages['sarah'].title()
print(f"Sarah's favourite language is {language}.")

print("")

# looping through all key-value pairs:
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print("")

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")

print("")

# looping through all the keys in a dictionary:
# keys() method is useful when you don't need to work with all the values in a dictionary.
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in favourite_languages.keys():
    print(name.title()) # the output shows the names of everyone.

print("")
 
friends = ['phil', 'sarah']
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("")

# we can find out if a particular person didn't take the poll:

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

print("")

# looping through a dictionary's keys in a particular order:
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("")

# looping through all values in a dictionary:
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

print("")

# pulling all the values from the dictionary without checking for repeats:
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title())

print("")



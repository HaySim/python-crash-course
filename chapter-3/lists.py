#A list is a collection of items in a particular order.
#In Python, square brackets ([]) indicate a list.
#Individual elements are separated by commas.



bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)



#Accessing Elements in a list:
#Index positions start at 0, not 1.



#Will return 'trek' without square brackets:
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles[0])



#'Trek' will be capitalised:
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles[0].title())



bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles[1])
print(bicycles[3])


#Returning the last item in the list:#
#(bicycles[-2]) would return the second item from the end of the list.
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles[-1])



#Using individual values from a list:
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

cars = ['tesla', 'bmw', 'hyundai', 'ford']
message = f"I would like to own a {cars[0].title()} Model S."
print(message)


#Modifying Elements in a list:
cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)
cars[0] = 'suzuki'
print(cars)



#Adding Elements to the end of a list:
#When you append an item to a list, the new element is added to the end of the list.
cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)
cars.append('fiat')
print(cars)

#Or:
cars = []

cars.append('tesla')
cars.append('bmw')
cars.append('hyundai')

print(cars)



#Inserting Elements at any position in the list and will shift every other value in the list one position to the right:
cars = ['tesla', 'bmw', 'hyundai', 'ford']

cars.insert(2, 'fiat')
print(cars) #['tesla', 'bmw', 'fiat', 'hyundai', 'ford']



#Removing Elements from a list:

#Using the del statement if you know the position of the item you want to remove:
cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)

del cars[3]
print(cars)

#Using the pop() method:
#The pop() method removes the last item in the list but it lets you work with that item after removing it.
cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)



last_owned = cars.pop()
print(f"The last car I owned was a {last_owned.title()}.")

#Popping items from any position in a list:
cars = ['tesla', 'bmw', 'hyundai', 'ford']
last_owned = cars.pop(2)
print(f"The last car I owned was a {last_owned.title()}.")



#Removing an item by value:
#Note: The remove() method deletes only the first occurrence of the value you specify.
#If the value appears more than once in the list, you'll need to use a loop to make sure all occurrences are removed.
cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)
cars.remove('bmw')
print(cars)

cars = ['tesla', 'bmw', 'hyundai', 'ford']
print(cars)

wrong_colour = 'tesla'
cars.remove(wrong_colour)
print(cars)
print(f"\nThe {wrong_colour.title()} is not available in red.")




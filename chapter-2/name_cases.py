message = "Hello Eric, would you like to learn some Python today?"
print(message)

name = "hayley simmons"
print(name.title())

name = "hayley simmons"
print(name.upper())
print(name.lower())

first_name = "hayley"
last_name = "simmons"
full_name = f"{first_name} {last_name}"
print(full_name)

first_name = "hayley"
last_name = "simmons"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

first_name = "hayley"
last_name = "simmons"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

message = "Michelle Obama once said, “When they go low, we go high.”"
print(message)

famous_person = "When they go low, we go high."
print(famous_person)

#\n is a newline:
name = "Michelle Obama"
print("Michelle \nObama")

#\t is a tab:
name = "Michelle Obama"
print("Michelle \tObama")

#\r Carriage return - takes the cursor to the beginning of the line. Will print as Obamalle:
name = "Michelle Obama"
print("Michelle \rObama")

#The Python lstrip() method removes the leading spaces from the left side of the string:
name = "Michelle Obama"
print(name.lstrip('Michelle '))

#The Python rstrip() method removes the leading spaces from the right side of the string:
name = "Michelle Obamalll"
print(name.rstrip('l'))

#The strip() method removes characters from both left and right:
name = "Michelle Obama"
print(name.strip('Obama'))

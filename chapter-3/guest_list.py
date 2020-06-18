guests = ['mum', 'grandma josie', 'izunna']
print(guests)

guests = ['mum', 'grandma josie', 'izunna']
message = f"Dear {guests[0].title()}, would you like to come for dinner on Saturday?"
print(message)
message = f"Dear {guests[1].title()}, would you like to come for dinner on Saturday?"
print(message)
message = f"Dear {guests[2].title()}, would you like to come for dinner on Saturday?"
print(message)

guests = ['mum', 'grandma josie', 'izunna']
print(guests)
print("Grandma Josie can't make it.")
guests[1] = 'dad'
print(guests)

message = f"Dear {guests[0].title()}, you're invited to come for dinner on Saturday!"
print(message)
message = f"Dear {guests[1].title()}, you're invited to come for dinner on Saturday!"
print(message)
message = f"Dear {guests[2].title()}, you're invited to come for dinner on Saturday!"
print(message)

message = f"Hi {guests[0].title()}, I have found a bigger dinner table for more guests!"
print(message)
message = f"Hi {guests[1].title()}, I have found a bigger dinner table for more guests!"
print(message)
message = f"Hi {guests[2].title()}, I have found a bigger dinner table for more guests!"
print(message)

guests.insert(0, 'adam')
print(guests)

guests.insert(2, 'laura')
print(guests)

guests.append('jackie')
print(guests)

message = f"Dear {guests[0].title()}, would you like to come for dinner on Saturday?"
print(message)
message = f"Dear {guests[2].title()}, would you like to come for dinner on Saturday?"
print(message)
message = f"Dear {guests[-1].title()}, would you like to come for dinner on Saturday?"
print(message)

message = f"Hi {guests[0].title()}, change of plan, can you come for dinner on Sunday instead?"
print(message)
message = f"Hi {guests[2].title()}, change of plan, can you come for dinner on Sunday instead?"
print(message)
message = f"Hi {guests[-1].title()}, change of plan, can you come for dinner on Sunday instead?"
print(message)

guests = ['adam', 'mum', 'laura', 'dad', 'izunna', 'jackie']
print(guests)

message = f"Hi {guests[5].title()}, sorry to hear that you can't make it on Sunday."
print(message)

popped_guest = guests.pop(5)
print(guests)

message = f"Hi {guests[0].title()}, sorry to hear that you can't make it on Sunday."
print(message)

popped_guest = guests.pop(0)
print(guests)












#!/usr/bin/env python
# coding: utf-8

# 3-1. Names: Store the names of a few of your friends in a list called names. Print each person’s name by accessing each element in the list, one at a time.

# In[1]:


names = ['jill', 'tyler', 'anna']
print(names[0])
print(names[1])
print(names[2])


# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

# In[5]:


names = ['jill', 'tyler', 'anna']
message = f"Good morning, {names[0].title()}"
print(message)
message = f"Hello, {names[1].title()}"
print(message)
message = f"Good afternoon, {names[2].title()}"
print(message)


# 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”

# In[11]:


car = ['Mercedes', 'Toyota', 'Audi']
message = f"I would like to own a {car[0].title()} car"
print(message)
message = f"I want to have a {car[1].title()} car in the future"
print(message)
message = f"I want to drive {car[2].title()} car "
print(message)


# 3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.

# In[5]:


guests = ['jill', 'nhan', 'linh']
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)


# 3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.
# 
# Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it.
# Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# Print a second set of invitation messages, one for each person who is still in your list.

# In[17]:


guests = ['jill', 'nhan', 'linh']
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

cant_come = guests.pop(1)
message = cant_come.title() + " can't go for the dinner"
print(message)

guests.insert(0,'jina')
print(guests)
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)


# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# 
# - Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table.
# - Use insert() to add one new guest to the beginning of your list.
# - Use insert() to add one new guest to the middle of your list.
# - Use append() to add one new guest to the end of your list.
# - Print a new set of invitation messages, one for each person in your list.

# In[28]:


guests = ['jill', 'nhan', 'linh']
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

cant_come = guests.pop(1)
message = cant_come.title() + " can't go for the dinner"
print(message)

guests.insert(0,'jina')
print(guests)
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

# inform people that you found a bigger table
print("\nWe found a bigger table!")

guests.insert(0,'aoi')
guests.insert(2,'loan')
guests.append('hen')
print(guests)

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# can invite just only 2 people
print("\nSorry, we can only invite two people for the dinner")

guests_remove = guests.pop(0)
print("Sorry " + guests_remove.title() + ", can't invite to the dinner.")

guests_remove = guests.pop(1)
print("Sorry " + guests_remove.title() + ", can't invite to the dinner.")

guests_remove = guests.pop(2)
print("Sorry " + guests_remove.title() + ", can't invite to the dinner.")

print(guests)


# In[23]:


guests = ['jill', 'nhan', 'linh']
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

cant_come = guests.pop(1)
message = cant_come.title() + " can't go for the dinner"
print(message)

guests.insert(0,'jina')
print(guests)
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

# inform people that you found a bigger table
print("\nWe found a bigger table!")

guests.insert(0,'aoi')
guests.insert(2,'loan')
guests.append('hen')
print(guests)

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")


# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.
# 
# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# Print a message to each of the two people still on your list, letting them know they’re still invited.
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# In[16]:


guests = ['jill', 'nhan', 'linh']
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

cant_come = guests.pop(1)
message = cant_come.title() + " can't go for the dinner"
print(message)

guests.insert(0,'jina')
print(guests)
message = f"Would you want to eat dinner with me {guests[0].title()}?"
print(message)
message = f"Please come to the dinner with me, {guests[1].title()}"
print(message)
message = f"We are having dinner tonight. Would you want to join {guests[2].title()}?"
print(message)

# inform people that you found a bigger table
print("\nWe found a bigger table!")

guests.insert(0,'aoi')
guests.insert(2,'loan')
guests.append('hen')
print(guests)

name = guests[0].title()
print(name + ", please come to dinner.")

name = guests[1].title()
print(name + ", please come to dinner.")

name = guests[2].title()
print(name + ", please come to dinner.")

name = guests[3].title()
print(name + ", please come to dinner.")

name = guests[4].title()
print(name + ", please come to dinner.")

name = guests[5].title()
print(name + ", please come to dinner.")

# can invite only two people for the dinner
print("\nSorry, we can invite only two people for dinner")
guests_remove = guests.pop()
print("Sorry, " + guests_remove.title() + " we can invite only two people for dinner")

guests_remove = guests.pop()
print("Sorry, " + guests_remove.title() + " we can invite only two people for dinner")

guests_remove = guests.pop()
print("Sorry, " + guests_remove.title() + " we can invite only two people for dinner")

guests_remove = guests.pop()
print("Sorry, " + guests_remove.title() + " we can invite only two people for dinner")

# mesasge to two people still on the list
guests_on_list = guests[0].title()
print(guests_on_list + " , please come to dinner")

guests_on_list = guests[1].title()
print(guests_on_list + " , please come to dinner")

del guests[0]
print(guests)

del guests[0]
print(guests)


# 3-8. Seeing the World: Think of at least five places in the world you’d like to visit.
# 
# - Store the locations in a list. Make sure the list is not in alphabetical order.
# - Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
# - Use sorted() to print your list in alphabetical order without modifying the actual list.
# - Show that your list is still in its original order by printing it.
# - Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list.
# - Show that your list is still in its original order by printing it again.
# - Use reverse() to change the order of your list. Print the list to show that its order has changed.
# - Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
# - Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
# - Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed

# In[26]:


locations = ['tokyo', 'hanoi', 'new york', 'seoul', 'washington']
print("Original list:")
print(locations)

print("\nSorted list in alphabetic order:")
print(sorted(locations))

print("\nOriginal list:")
print(locations)

locations.reverse()
print("\nReverse order")
print(locations)

locations.reverse()
print("\nOriginal list:")
print(locations)

locations.sort()
print("\nAlphabetic order:")
print(locations)

locations.sort(reverse = True)
print("\nReverse-alphabetical order:")
print(locations)


# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4 through 3-7 (pages 41–42), use len() to print a message indicating the number of people you’re inviting to dinner.

# In[31]:


guests = ['jill', 'nhan', 'linh']
print("I will invite " + str(len(guests)) + " to dinner")


# 3-10. Every Function: Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.

# In[41]:


# make a list of mountains
mountains = ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu', 'Cho Oyu', 'Dhaulagiri', 'Manaslu', 'Nanga Parbat', 'Annapurna']

# accessing elements in a list
print(mountains[0])

# ask for the item at index  -1
print(mountains[-1])

# pull the first mountain from the list and compose a message 
message = f"I want to go to {mountains[0]}."
print(message)

# modifying elements in a list
mountains[0] = 'Denali'
print(mountains)

mountains.append('Vinson Massif')
print(mountains)

del mountains[0]
print(mountains)

print(mountains.pop())

print(sorted(mountains))


# In[ ]:





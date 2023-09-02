"""
This code will generate a thank you note.
It will take user inputs and add them into a paragraph
"""

print("Hello! Welcome to the Thank You Note Generator!")
print("To begin, please fill out the information below...")

#inputs

name = (input("Your Name: "))
giver = (input("Receiver's Name: "))
gift = (input("What you received: "))
verb = (input("Verb describing how you will use said gift (ex. play, use, etc..): "))
emotion = (input("How you feel about gift: "))

print (" Dear " + giver)
print("")
print("          Thank you so much for the " + gift + " I was so" + emotion + "to receive your kind gift! I am very excited to " + verb + " with my very new " + gift + "! " )
print("")
print("Thanks Again!")
print("Sincerely,")
print(name)


firstName = "James"
lastName = "Cagle"
# Personal Message
print("Hello " + firstName + ", would you like to learn some Python today?")
# Name Cases
fullName = "Jennifer Cagle"
print(".upper():\t" + fullName.upper() + "\n.lower():\t" + fullName.lower() + "\n.title():\t" + fullName.title())
# Famous Quote
print("Ralph Ellison once said, \"Life is to be lived, not controlled, and humanity is won by continuing to play in "
      "the face of certain defeat.\"")
# Famous Quote #2
famousPerson = "Ralph Ellison"
quote = "\"Life is to be lived, not controlled, and humanity is won by continuing to play in the face of certain " \
        "defeat.\""
print(famousPerson + " once said, " + quote)
# Stripping Names
myName = "     \n*\tJames Cagle    *\t  "
print(myName)
print(myName.strip())
print(myName.lstrip())
print(myName.rstrip())
print(myName.lstrip().rstrip())


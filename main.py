myName = "james"
herName = "jennifer"
print(".title()")
print(myName.title())
print(".upper()")
print(myName.upper())
print(".lower()")
print(myName.lower())
print(".casefold()")
print(myName.casefold())
print(".capitalize()")
print(myName.capitalize())
print(".isalnum()")
print(myName.isalnum())
ourName = myName.title() + " and " + herName.title()
print(ourName)
ourNameAsString = f"{myName.title()} and {herName.title()}"
print(ourNameAsString)

james = "james"
jennifer = "jennifer"
cagle = "cagle"

print("Name:\t" + james.title() + " " + cagle.title()+"\nName:\t" + jennifer.title() + " " + cagle.title())

favoriteFood = '  steak  '
print('***'+favoriteFood+'***')
print('***'+favoriteFood.rstrip()+'***')
print('***'+favoriteFood.lstrip()+'***')
print('***'+favoriteFood.lstrip().rstrip()+'***')
print('***'+favoriteFood.strip()+'***')
print('***'+favoriteFood.lstrip().rstrip().capitalize()+'***')

message = "One of Python's strengths is its diverse community"
print(message)

import pyjokes
  
# using get_jokes() to generate a whole list of jokes
print("Welcome to Infiniti Jokes CLI")
print("To view jokes to laugh at, select the lanaguage and category below")

# Language selection
languages = ['en', 'de', 'es', 'gl' , 'eu', 'it']
while True:
    print("Language: (1) English, (2) German, (3) Spanish, (4) Galician, (5) Basque (6) Italian")
    
    try:
        language_index = int(input("Select Language: "))
    except ValueError:
        print("Invalid input, try again")
        continue

    if language_index >= 1 and language_index <= 6:
        break
    else:
        print("Invalid Language, try again")

# Category selection
categories = ['neutral', 'chuck', 'all']
while True:
    print("Cateory: (1) Neutral, (2) Chuck, (3) All")

    try:
        category_index = int(input("Select Category: "))
    except ValueError:
        print("Invalid input, try again")
        continue

    if category_index >= 1 and category_index <= 3:
        break
    else:
        print("Invalid Category, try again")


list_of_jokes = pyjokes.get_jokes(language=languages[language_index - 1], \
                                    category=categories[category_index - 1])
  
# traversing through the generated list of jokes
# Range of i may change, depending on the number of jokes
# you want to display
print("Here are the jokes based on your selection options. \n\n")
for i in range(len(list_of_jokes)):
    print("\n* " +list_of_jokes[i] + " *", sep='\n')
    if i != len(list_of_jokes) - 1:
        cont = input("\nDo you want to see another joke? Yes(y) or No(n): ").strip()
        if cont.lower() == "n":
            break

print("That's the end folks! See you again really soon.")
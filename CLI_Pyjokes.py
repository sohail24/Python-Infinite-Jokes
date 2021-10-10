import pyjokes
  
# using get_jokes() to generate a whole list of jokes
# language is german
# category is twister
list_of_jokes = pyjokes.get_jokes(language="de", category="twister")
  
# traversing through the generated list of jokes
# Range of i may change, depending on the number of jokes
# you want to display
for i in range(0, 4):
    print(list_of_jokes[i], sep='\n')
def greet():
    name = input("What is your name? ") #this line prompts user for their name
    age = int(input("How old are you? ")) #this line prompts user for their age
    print(f"Hello, {name}! You are {age} years old.")
greet() #this line calls the greet function
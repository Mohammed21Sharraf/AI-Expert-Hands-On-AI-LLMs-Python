print("Hello I'm an AI bot.")
name = input("What's your name?")
print(f"Nice to meet you{name}")
feeling = input("How are you feeling today? (good/bad)?").lower()
if feeling == 'good':
    print("I'm glad to hear that.")
elif feeling == 'bad':
    print("I hope your day gets better.")
else:
    print("I see. Sometimes it's tough to express your feelings into words.")
    
print(f"It was nice chatting with you, {name}.")

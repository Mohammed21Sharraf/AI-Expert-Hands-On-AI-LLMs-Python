# import re, random
# from colorama import Fore, init
import re, random
from colorama import Fore,init


# # Initialize colorama (autoreset ensures each print resets after use)
# init(autoreset=True)
init(autoreset=True)

# # Destination & joke data
destinations = {
    "beaches": ["Bali", "Maldives", "Phuket"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "cities": ["Tokyo", "Paris", "New York"]
}
jokes = [
    "Why don't programmers like nature? Too many bugs!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why do travelers always feel warm? Because of all their hot spots!"
]

# # Helper function to normalize user input (remove extra spaces, make lowercase)
# def normalize_input(text):
#     return re.sub(r"\s+", " ", text.strip().lower())
def normalize_input(text):
    return re.sub(r"\s+"," ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(f"{Fore.CYAN} Travel bot: beaches, mountains, cities?")
    prefrence = input(f"{Fore.YELLOW}You: ")
    prefrence = normalize_input(prefrence)
    if prefrence in destinations:
        suggestion = random.choice(destinations[prefrence])
        print(f"{Fore.GREEN} Travel bot: How about {suggestion}?")
        print(f"{Fore.CYAN} Travel bot: Do you like this? (yes/no)")
        answer = input(f"{Fore.YELLOW} You: ").lower()
        if answer == "yes":
            print(f"{Fore.GREEN} Travel bot: Awesome choice! Enjoy your trip to {suggestion}!")
        elif answer == "no":
            print(f"{Fore.RED} Travel bot: Let's try another.")
        else:
            print(f"{Fore.RED} Travel bot: I'll suggest again.")
    else:
        print(f"{Fore.GREEN} Travel bot: Sorry, I don't have that destination on my list.")
    show_help()


# Offer packing tips based on user’s destination and duration
def packingtips():
    print(f"{Fore.CYAN} Travel bot: Where to?")
    location = normalize_input(input(f"{Fore.YELLOW} You: "))
    print(f"{Fore.CYAN} Travel bot: For how many days?")
    days = normalize_input(input(f"{Fore.YELLOW} You: "))
    print(f"{Fore.GREEN} Travel bot: Packing tips for {days} days in {location}.")
    print(f"{Fore.GREEN}- Pack versatile clothes.")
    print(f"{Fore.GREEN}- Bring chargers for all devices.")
    print(f"{Fore.GREEN}- Check the forecast to make sure your trip goes smoothly.")


# Tell a random joke
def joke():
    print(f"{Fore.YELLOW} Travel bot: {random.choice(jokes)}")

# Display help menu
def show_help():
    print(f"{Fore.MAGENTA}I can:")
    print(Fore.GREEN + "- Suggest travel spots (say 'recommendation')")
    print(Fore.GREEN + "- Offer packing tips (say 'packing')")
    print(Fore.GREEN + "- Tell a joke (say 'joke')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")



# Main chat loop
def chat():
    print(f"{Fore.CYAN} Hello I am travel bot.")
    name = input(f"{Fore.YELLOW} Your name?")
    print(f"{Fore.GREEN} Nice to meet you, {name}!")
    show_help()
    while True:
        User_input = input(f"{Fore.YELLOW} {name}: ")
        User_input = normalize_input(User_input)
        if "recommend" in User_input or "suggest" in User_input:
            recommend()
        elif "pack" in User_input or "packing" in User_input:
            packingtips()
        elif "joke" in User_input or "funny" in User_input:
            joke()
        elif "help" in User_input:
            show_help()
        elif "exit" in User_input or "bye" in User_input:
            print(f"{Fore.CYAN} Travel bot: Safe travels! Goodbye.")
            break
        else:
            print(f"{Fore.RED} Travel bot: Could you please elaborate?")


# Run the chatbot
if __name__ == "__main__":
    chat()
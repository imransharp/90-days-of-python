responses = {}  # Empty dictionary to store responses

while True:
    name = input("Enter your name (or type 'exit' to stop): ")
    if name.lower() == "exit":
        break  # Stop the loop if user types 'exit'
    
    language = input(f"Hi {name}, what's your favorite programming language? ")
    
    responses[name] = language  # Store response in dictionary

print("\n📌 Survey Results:")
for name, language in responses.items():
    print(f"{name} loves {language}.")

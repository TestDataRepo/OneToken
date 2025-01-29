# Create a file and write a weak token to it

weak_token = "123456"  # Example of a weak token

# Open the file in write mode
with open("weak_token.txt", "w") as file:
    file.write(f"token={weak_token}")

print("Weak token written to weak_token.txt")

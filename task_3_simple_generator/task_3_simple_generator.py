import random
import string

def generate_password(length):
    """
    Generate a password using a combination of random characters.
    """
    # Define the characters to use in the password
    # This includes letters, numbers, and symbols for complexity
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("---------------------------------")
    print("    TASK 3: PASSWORD GENERATOR   ")
    print("---------------------------------")
    print("A password generator is a useful tool that generates strong and")
    print("random passwords for users. This project aims to create a")
    print("password generator application using Python, allowing users to")
    print("specify the length and complexity of the password.\n")

    # 1. User Input: Prompt the user to specify the desired length of the password.
    try:
        length = int(input("Enter the desired length of the password: "))
        
        if length <= 0:
            print("Please enter a positive number for the length.")
            return

        # 2. Generate Password: Use a combination of random characters to generate 
        #    a password of the specified length.
        password = generate_password(length)

        # 3. Display the Password: Print the generated password on the screen.
        print(f"\nGenerated Password: {password}")
        print("---------------------------------")

    except ValueError:
        print("Invalid input! Please enter a numeric value for the length.")

if __name__ == "__main__":
    main()

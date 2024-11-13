# Python Program to Greet User and Calculate Birth Year
# This program asks the user for their name and age. It then greets the user with a personalized message 
# and calculates the year they were born based on the current year (2024). Basic error handling is included 
# to manage non-numeric age input.

def main():
    # Prompt the user to enter their name
    name = input("Please enter your name: ")
    
    # Greet the user with a personalized message
    print(f"Hello, {name}! Nice to meet you.")
    
    # Use a loop to ensure valid age input
    while True:
        try:
            # Ask the user for their age
            age = int(input("Please enter your age: "))
            
            # Calculate the birth year
            current_year = 2024
            birth_year = current_year - age
            
            # Display the calculated birth year
            print(f"{name}, you were born in the year {birth_year}.")
            break  # Exit loop if input is valid
        
        except ValueError:
            # Handle non-numeric input
            print("Invalid input. Please enter a numeric age.")

# Run the main function
if __name__ == "__main__":
    main()

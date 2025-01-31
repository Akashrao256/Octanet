import time

print("Please enter your card")
time.sleep(5)

# Set the correct PIN and account balance
password = 1234
balance = 5000

# Get the ATM PIN from the user
pin = int(input("Enter your ATM PIN: "))

# Check if the entered PIN matches the password
if pin == password:
    while True:
        # Print the menu options
        print("""
        1 == Balance
        2 == Withdraw
        3 == Deposit
        4 == Exit
        """)

        try:
            # Ask the user to choose an option
            option = int(input("Please enter your choice: "))

            # Handle different menu options
        
            if option == 1: # Display balance
                print(f"Your current balance is {balance}")

            elif option == 2: # Withdraw money
                withdraw_amount = int(input("Please enter withdraw amount: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} is debited from your account.")
                    print(f"Your current balance is {balance}")
                else:
                    print("Insufficient balance.")
 
            elif option == 3: # Deposit money
                deposit_amount = int(input("Please enter deposit amount: "))
                balance += deposit_amount
                print(f"{deposit_amount} is credited to your account.")
                print(f"Your updated balance is {balance}")

            elif option == 4:  # Exit
                print("Exiting. Thank you for using the ATM!")
                break  # Exit the loop

            else: # Handle invalid menu options
                print("Invalid option. Please try again.")
        except ValueError: # Handle non-numeric inputs
            print("Invalid input. Please enter a number from the menu.")

else: # Handle incorrect pin input
    print("Incorrect PIN. Please try again.")

# ------------------------------------------------------
#        Name: Vivian Nguyen 
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    """ Prompts the user for a sentence repeatedly until a valid word is found.
    If the user's input contains the secret world, print 'You used the secret world!'.
    If the user's input contains the word 'dog' or 'Dog', print 'You used the word "dog" or the word "Dog"
    If anything else, print "Try again". """
    while True:
        # Get input sentence from the user
        sentence = input("Give me a sentence:")
        # Check if the secret word is in the sentence
        if secret_word in sentence:
            print("You used the secret word!")
            break # Exit loop when secret word is found
        # Check if "dog" or "Dog" is found
        elif "dog" in sentence or "Dog" in sentence:
            print('You used the word "dog" or the word "Dog"!')
            break # Exit loop when "dog" or "Dog" is found
        else:
            print("Try again")
            continue # Ask the user again 
    pass



# Task 2
def check_greater():
    """ Prompts the user for two integers repeatedly until they are not equal.
    Compares the two integers and prints which one is greater ("First is Greater"
    or "Second is Greater"). If both integers are equal, prompts the user to try again.
    Prints "Done" upon completion """
    while True:
        # Read two integer inputs from the users
        a = int(input("Give me a first integer:"))
        b = int(input("Give me a second integer:"))
        
        # Determine if the first integer is greater
        if a > b:
            print("First is Greater")
            break # Exit loop if the first integer is greater
    
        # Determine if the second integer is greater
        elif b > a:
            print("Second is Greater")
            break # Exit loop if the second integer is greater
        
        # Determine if two integers are equal
        else:
            print("Try again")
            continue # Re-prompt if numbers are equal
        
    print("Done")
    pass



# Task 3
def get_special_numbers():
    """ Iterates through numbers from 1 to 40 and prints "special" numbers.
    A special number must satisfy all of the following conditions:
    - Must be odd (not divisible by 2)
    - Must be divisible by 3
    - Must NOT be divisible by 5 """
    
    # Loop through integers from 1 up to 41
    for num in range(1,41):
        # Skip even numbers
        if num %2 == 0:
            continue
        
        # Skip numbers not divisible by 3
        elif num%3 != 0:
            continue
        
        # Skip multiples of 5
        elif num%5 == 0:
            continue
        
        # Print number if it meets all three criteria
        else:
            print(num)
    pass


# Task 4.a
def my_for_loop():
    """ Prompts the user for a string and evaluates each character.
    Validates that the input length is between 2 and 5 characters and
    contains no spaces. If invalid, prints "bad word" and returns. Otherwise, iterates
    through the characters and identifies each as either a vowel or a consonant. """
    
    user_string = input("Give me a string:")
    
    # Check if length is not between 2 and 5, or if string contains a space
    if len(user_string) not in range(2,6) or " " in user_string:
        print("bad word")
        return user_string
    
    else:
        # Convert string to list of charaters
        let = list(user_string)
        
        # Iterate over index positions of the charater list
        for i in range(len(let)):
            # Check if current character is a vowel
            if let[i] == "a" or let[i] == "i" or let[i] == "o" or let[i] == "u" or let[i] == "e":
                print(f"{let[i]} is a vowel")
                i += 1
            else:
                print(f"{let[i]} is a consonant")
                i += 1
                
    pass

# Task 4.b
def my_while_loop():
    """ Offer user three choices, take the user's input.
    Repeatedly prompts until a valid selection ('a', 'b', or 'c') is entered.
    If 'a' is selected, repeatedly prompts.
    Returns 'b' with a goodbye message, or exits the program if 'c' is chosen. """
    
    user_choice = input("Choose one option: a, b, or c: ")
    # Keep prompting until input is 'a', 'b', or 'c'
    while user_choice != "a" and user_choice != "b" and user_choice != "c":
        print("try again")
        user_choice = input("Choose one option: a, b, or c: ")
        
    while user_choice == "a":
        user_choice = input("Choose one option: a, b, or c: ")
    if user_choice == "b":
        print("Goodbye")
        return user_choice
    elif user_choice == "c":
        sys.exit()

        
    pass

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

#!/usr/bin/python3


#Script to validate an inputted password using either a whitelist or a blacklist.

#Set prompts to use for each validation function
prompt1 = "Please enter a password. Numbers and alphabetical characters only please."
prompt2 = "Please enter a password. Numbers, alphabetical characters and some symbols are allowed."

#Function to validate a password using a whitelist. The global variable prompt1 is accessed for the prompt.
#A string whitelist is created and set to a string of all permissible characters. To edit the built-in whitelist,
#simply edit this string.

#An empty list white_list is created, as is the variable checking (set to True). The variable password_caps is created and
#set to an empty string. This variable allows the program to ignore capitalization for the purposes of validation,
#and later return the password in its original state. The script then iterates through whitelist and appends each character to the list white_list.

#A while loop is then executed. The user will be prompted for an input as long as the password_caps variable is an empty
#string. This input is set to the variable password. Password is capitalized using .upper() and password_caps is set to this new string.
#The program then iterates through password_caps, checking each character against white_list. If the character is found in the list,
#the program continues. If not, the password_caps string is reset to an empty string, and the user will be prompted to enter a new password.
#Once a password has been inputted and successfully validated, the function will return the password in its original form.

def whitelist_validate():
    global prompt1
    whitelist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@"
    white_list = []
    checking = True
    password_caps = ""
    
    for item in whitelist:
        white_list.append(item)
    #print(white_list)

    while password_caps == "":
        password = input(prompt1)
        password_caps = password.upper()

        for character in password_caps:
            if character in white_list:
                continue
            else:
                password_caps = ""
                continue
    print("Valid password!")
    return password

#Function to validate a password using a blacklist. This function operates in much the same way as the above whitelist
#function, but uses a variable (blacklist) of unauthorized characters instead. A list is created and populated with
#characters in the string blacklist, against which the password is checked. As in the whitelist validation,
#this function uses a while loop and iterates through the inputted password
#(again set to the capitalization-agnostic variable password_caps). This time, however, it checks if each character is NOT in the blacklist.
#If it isn't, the program continues until it has checked every character in the password.
#If a character in the banned list is found, the password_caps string is reset to an empty
#string and the user will be prompted to input a password again. The original password is returned upon successful validation.

def blacklist_validate():
    global prompt2
    blacklist = "#\/\"\' "
    black_list = []
    password_caps = ""
    
    for item in blacklist:
        black_list.append(item)
    #print(black_list)

    while password_caps == "":
        password = input(prompt2 + " Invalid symbols: " + blacklist + "\n")
        password_caps = password.upper()
        for character in password_caps:
            if character not in black_list:
                continue
            else:
                password_caps = ""
                continue
    print("Valid password!")
    return password

 

#Main loop allowing a user to test the validation functions. Checks for a command (either blacklist or whitelist) and executes the appropriate
#validation function. The print function is used here to verify the returned password. Invalid commands are handled with the running while loop.

if __name__ == '__main__':
    running = True

    while running:
        command = input("Password validation tool. Enter 'whitelist' to use a built-in whitelist, or 'blacklist' for a built-in blacklist: ")
        if (command.upper() == "WHITELIST"):
            print(whitelist_validate())
            break
        elif (command.upper() == "BLACKLIST"):
            print(blacklist_validate())
            break
        else:
            print("Invalid command. Please try again.")
            continue

        
            





    
    
        

    

    
            
            
       
        

    




    
        

    
        



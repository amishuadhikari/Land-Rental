def user_name():
    while True:
        correct_name = str(input("What is your name Sir/Maam?:  \n\n"))
        if correct_name.isalpha(): # only accepts if input is alphabetic.
            return correct_name.capitalize() #makes the firts letter of name in capital
        else:  
            print("Please enter a valid name..\nNote: Only first name is required.!!\n") 

def get_valid_option(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isnumeric() == 1 or 2 or 3 or 4:
            if user_input in ("1", "2","3","4"):
                return int(user_input)
            else:
                print("PLease follow the format.")
            return int(user_input)
        else:
            print("PLease follow the format.")
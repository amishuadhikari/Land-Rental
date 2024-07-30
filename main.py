from calculationoperation import RENT ,RETURN
from read import Property
from write import generate_bill_rent, generate_bill_return
from validinput import get_valid_option, user_name

def main():  
       
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    print("New Baneshwor, \t \t  \t \t WELCOME TO TECHNO PROPERTY NEPAL \t \t \t \t\t 014622532")
    print("Kathmandu\n")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")
    name =   user_name()   
    print(f"Hello {name} !\n ")
    continueBuyingLand = True
    while continueBuyingLand == True: 
        print(f"Enter your option {name}.\n")       
        print("Enter 1 to show the Lands:  ")
        print("Enter 2 to RENT: ")
        print("Enter 3 to RETURN: ")
        print("Enter 4 to EXIT\n")
        
        try: #error handling.
            Option = get_valid_option("Enter an option to continue: ")
        except Exception as e:
             print(f"Invalid input. Please try again {name}")
             continue

        if Option ==1:
            show_land = Property() 
            show_land.read_file()#displays the land information from land.txt file.
            continue
        
        
        elif Option == 2:
            show_land = Property()
            show_land.read_file()
            renting_result = RENT(name) #username is passed from here.
            rented_lands = renting_result.Renting_land(renting_result.lands) #handles the renting process.
            total_cost = renting_result.totalcost(rented_lands)             
            generate_bill_rent(name,total_cost,rented_lands)
            continueBuyingLand = True



        elif Option ==3:
            show_land = Property()
            show_land.read_file()  #calls the readfile function
            return_land = RETURN(name) 
            returned_land = return_land.Returning_land() 
            total_cost = return_land.totalcost_return(returned_land)
            generate_bill_return(name,total_cost,returned_land) #name,totalcost,returned_landa are parameters and it prints the bill
            continueBuyingLand = True #the program wont end unless the user presses 4 (exit).
             
        elif Option ==4:
            print(f"Thankyou so much {name} for using our services....")
            continueBuyingLand = False

        
        else:
            print(f"PLease follow the format !!!!!. \n")
            continueBuyingLand = True      
            
        
if __name__ == "__main__":  
    main()
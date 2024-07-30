class RENT():
    def __init__(self, user_name ): #username is used from the main.py file
        self.lands = self.land_list()
        self.user_name = user_name
    def land_list(self): #method
        with open("land.txt", "r") as data:
            data_in_file = data.readlines() 
        return data_in_file

    def Renting_land(self, data_in_file):
        rented_lands = [] # rented land will be appended here after user rents the land
        total_cost = 0  
        continue_buying_lands = True
        while continue_buying_lands: #while loop because unless the user inputs correct kitta number the program will keep running.
            kitta_number = input("Enter the kitta number of the land you want to rent: \n")            
            invalid_kitta = True
            for i in range(len(data_in_file)):
                land_info = data_in_file[i].strip().split(",")#to seperate the line into individual piece of information
                if land_info[0] == kitta_number: 
                    invalid_kitta = False # now kittanumber is valid
                    status = land_info[5].strip() #to get the status of land
                    if status == "Available":
                        print(f"The land with kitta number {kitta_number} is available for rent.")
                        confirm = input(f"Do you want to rent this land {self.user_name}? (y/n): ")
                        if confirm.lower() == "y":
                            while True:
                                duration_of_time = input("For how many months do you want to rent the land: ")
                                if duration_of_time.isdigit() and 0 < int(duration_of_time) <= 36: #should input in digit and should be more than 0 and less than 36.
                                    duration_of_time = int(duration_of_time)
                                    land_info[5] = "Not Available"
                                    data_in_file[i] = ','.join(land_info) + '\n'
                                    with open("land.txt", "w") as file:
                                        file.writelines(data_in_file)
                                    print(f"You have rented the land with kitta number {kitta_number} for {duration_of_time} months.")
                                    rental_price = int(land_info[4].strip()) 
                                    rental_cost = rental_price * duration_of_time
                                    total_cost = total_cost + rental_cost
                                    rented_lands.append((kitta_number, land_info[1],land_info[2],land_info[3],land_info[4], duration_of_time, int(rental_cost))) #appends the rented land detaails to above empty list.
                                    break #exits the loop
                                else:
                                    print("SORRY, Minimum months of renting is 1 and Maximum is 36.")
                        elif confirm.lower() == 'n':
                            print("Renting process is canceled.")  
                        else:
                            print("Please enter 'y' or 'n'. Try Again !! ")
                            continue #goes to next loop
                    elif status == "Not Available":
                        print(f"The land with kitta number {kitta_number} is already unavailable.")
                    else:
                        print(f"Invalid kitta number: {kitta_number}.")
            if invalid_kitta:
                print(f"Invalid kitta number: {kitta_number}.") 
                continue
            while True: # using loop so user can rent multiple lands
                query = input(f"Would you like to rent another land {self.user_name}? (y/n)")
                if query.lower() == "y":
                    break 
                elif query.lower() == "n":
                    if rented_lands:
                        print(f"You have rented {len(rented_lands)} lands in total.")
                        print("----------------------------------------------------------------------------------------------------------------")
                        print("SN".ljust(4, ' '), "| Kitta No.".ljust(10, ' '),  "| Location".ljust(15, ' '),  "|  Land Faced".ljust(12, ' '), "| Anna".ljust(10, ' '), "| Price".ljust(15, ' '), "| Rent Duration".ljust(17, ' ' ), "| TotalCost      ")
                        print("----------------------------------------------------------------------------------------------------------------")
                        for i in range(len(rented_lands)):
                            kitta_no, location, land_faced, anna, price, duration, cost = rented_lands[i] 
                            print(f"{i + 1:<4} | {kitta_no:<9} | {location:<13} | {land_faced:<11} | {anna:<8} | {price:<13} | {duration:<15} | {cost}     ")
                            print("----------------------------------------------------------------------------------------------------------------")                    
                        print( "\t\t\t\t\t\t\t\t\t\t\t", "Total :", f"Rs.{total_cost}")   
                        input("Press Enter to Print Bill: ")              
                    else:
                        print("You haven't rented any land yet.")
                    return rented_lands                                   
                else:
                    print("Please enter either 'y' or 'n'.")
            if invalid_kitta:
                print(f"Invalid kitta number : {kitta_number}")
                continue

    def totalcost(self, rented_lands): 
        total_cost = sum(land[6] for land in rented_lands) #land[6] is price so it will calculate the total.
        return total_cost
    
    
class RETURN(RENT): #

    def __init__(self, user_name):#intializes return class with a user_name parameter
        self.user_name = user_name

    def totalcost_return(self, returned_land):
        total_cost = sum(int(land[6]) + int(land[4]) for land in returned_land)
        return total_cost
    
    def Returning_land(self):
        returned_land = []
        data_in_file = self.land_list() #gains land data
        with open("land.txt", "r") as file:
            data_in_file = file.readlines()
        continue_returning_land = True
        while continue_returning_land:
            kitta_number = input("Enter the kitta number of the land you want to return: ")
            invalid_kitta = True            
            for i in range(len(data_in_file)): #iterates each line in data
                land_info = data_in_file[i].strip().split(",")
                if land_info[0] == kitta_number: 
                    invalid_kitta = False                   
                    status = land_info[5].strip()
                    if status == "Not Available":
                        confirm = input(f"Do you want to return this land {self.user_name}? (y/n): ")
                        if confirm.lower() == "y": 
                            land_info[5] = "Available"
                            data_in_file[i] = ','.join(land_info) + "\n"
                            with open("land.txt", "w") as file:
                                file.writelines(data_in_file) #updates the data in land.txtfile
                            print(f"The land with the kitta number {kitta_number} has been returned.")
                            rental_price = int(land_info[4].strip())                      
                            while True:
                                late_return_query = input("Are you late to return the land on time [y or n]: ")
                                if late_return_query.lower() == 'y':
                                    delayed_month = input("How many months are you late to return : ")
                                    if delayed_month.isdigit() and 0 < int(delayed_month) <= 10: #logic to calucalte the total if renturned late
                                        delay_fine = int(10/100 * int(rental_price) * int(delayed_month))
                                        total = rental_price + int(delay_fine)
                                        returned_land.append((kitta_number, land_info[1], land_info[2], land_info[3], rental_price, delayed_month, delay_fine, total))
                                        print(f"As you have rented land for extra {delayed_month} month 10% charge will be added to each delayed month. ")
                                        break
                                    else:
                                        print("Please try again.")
                                elif late_return_query.lower()== 'n':
                                    total = rental_price
                                    returned_land.append((kitta_number, land_info[1], land_info[2], land_info[3], rental_price, 0, 0, total))#if pressed no the loop will end and print the total
                                    break
                                else:
                                    print("Please enter 'y' or 'n'. ")                                            
                        elif confirm.lower() == "n":
                            print("Process is canceled.")
                        else:
                            print("Please eneter 'y' or 'n'. Try Again! " )
                    elif status == "Available":
                        print(f"You have not rented the land with the kitta number: {kitta_number}")
                    else:
                        print(f"Invalid kitta number: {kitta_number}")          
                        break
            if invalid_kitta:
                print(f"Invalid kitta number: {kitta_number}")
                continue
            
            while True:
                continue_returning_land_query = input(f"Do you want to return another land {self.user_name}? (y/n): ")
                if continue_returning_land_query.lower() == "y":
                    break
                elif continue_returning_land_query.lower()=="n":
                    if returned_land:
                        print("-------------------------------------------------------------------------------------------------------------")
                        print("SN".ljust(4, ' '), "| Kitta No.".ljust(10, ' '), "| Location".ljust(13, ' '), "| Land Faced".ljust(12, ' '), "| Anna".ljust(10, ' '), "| Price".ljust(15, ' '), "| Delayed Month".ljust(12, ' '), "| Delay Fine".ljust(17, ' '))
                        print("-------------------------------------------------------------------------------------------------------------")   
                        for i in range(len(returned_land)):
                            kitta_no, location, land_faced, anna, price, delayed_month, delay_fine, total = returned_land[i]
                            print(f"{i + 1:<4} | {kitta_no:<9} | {location:<11} | {land_faced:<10} | {anna:<8} | {price:<13} | {delayed_month:<13} | {delay_fine}")
                            print("-------------------------------------------------------------------------------------------------------------")
                        print(f"\t\t\t\t\t\t\tTotal: {total}")
                        input("Press Enter to Print Bill: ")
                    else:
                        print("You have not returned any land yet. ")
                    return returned_land
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")            
            if invalid_kitta:
                print(f"Invalid kitta number: {kitta_number}.")
                continue

    
        


                    
                    

        


    




        


    
    
        

        
        

    





            

    
    





                






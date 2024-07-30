import datetime
import random

def generate_bill_rent(user_name, total_cost, rented_lands): #prints bill for rent #parameters
        date = datetime.datetime.now().strftime("%d-%m-%y")
        billname = f"{user_name}{random.randint(1, 1200)}"
        filename = f"{billname}.bill"
        with open(filename, "w") as f:
            f.write(f"Bill no: {billname}\n")
            f.write(f"Date: {date}\n")
            f.write(f"Name: {user_name}\n")
            f.write("-------------------------------------------------------------------------------------------------------------\n")
            f.write("SN".ljust(4, ' ') + "| Kitta No.".ljust(13, ' ') + "| Location".ljust(15, ' ') + " | Land Faced".ljust(15, ' ') + "| Anna".ljust(10, ' ') + "| Price".ljust(14, ' ') + "| RentDuration".ljust(18, ' ') + "| Total Cost \n")
            f.write("-------------------------------------------------------------------------------------------------------------\n")
            for i in range(len(rented_lands)):
                land = rented_lands[i]
                f.write(f"{i + 1:<3} | {land[0]:<10} | {land[1]:<13} | {land[2]:<11} | {land[3]:<7} | {land[4]:<11} | {land[5]:<15} | {land[6]}\n")
                f.write("------------------------------------------------------------------------------------------------------------\n")
            f.write(f"\t \t \t \t \t \t \t \t\t\t Grand Total : Rs.{total_cost}\n")
        print("Thank you so much for using our services.")
        print()        
        print("\t\t\t\t\t\t Namaste !!\n")



def generate_bill_return(user_name,total_cost, returned_land): #prints bill for return
        date = datetime.datetime.now().strftime("%d-%m-%y")
        billname = f"{user_name}{random.randint(1, 1200)}"
        filename = f"{billname}.bill"
        with open(filename, "w") as f:
            f.write(f"Bill no: {billname}\n")
            f.write(f"Date: {date}\n")
            f.write(f"Name: {user_name}\n")
            f.write("----------------------------------------------------------------------------------------------------------------\n")
            f.write("SN".ljust(3, ' ') + " | Kitta No.".ljust(10, ' ') + "| Location".ljust(17, ' ') + "| Land Faced".ljust(12, ' ')+ " | Anna".ljust(10, ' ')+ "| Price".ljust(15, ' ')+ "| Delayed Month".ljust(17, ' ')+ "| Delay Fine\n")
            f.write("----------------------------------------------------------------------------------------------------------------\n")   
            for i in range(len(returned_land)):
                land = returned_land[i]
                f.write(f"{i + 1:<3} | {land[0]:<8} | {land[1]:<13} | {land[2]:<11} | {land[3]:<7} | {land[4]:<11} | {land[5]:<14} | {land[6]}\n")
            f.write("--------------------------------------------------------------------------------------------------------------------\n")
            f.write(f"\t\t\t\t\t\t\tTotal: Rs. {int(total_cost)}")
        print("Your renting has ended.")
        print("Thank you so much for using our services.")
        print()        
        print("\t\t\t\t\t\t Namaste !!\n")

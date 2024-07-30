class Property:
    def __init__(self):
        pass
    
    def read_file(self):
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("SN".ljust(10, ' '), "| Kitta No.".ljust(15, ' '), "| Location".ljust(21, ' '), "| Land Faced".ljust(26, ' '), "| Anna".ljust(11, ' '), "| Price".ljust(24, ' '), "| Status")
        print("------------------------------------------------------------------------------------------------------------------------------------")

        with open("land.txt", "r") as file: #displays the information from the text file
            serial_number = 1
            for line in file:           
                kitta_no, location, land_faced, anna, price, status = line.strip().split(",")         
                print(f"{str(serial_number).ljust(10)}| {kitta_no.ljust(15)}| {location.ljust(20)}| {land_faced.ljust(25)}| {anna.ljust(10)}| {price.ljust(23)}| {status}")
                serial_number += 1
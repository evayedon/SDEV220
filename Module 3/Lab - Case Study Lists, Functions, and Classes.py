class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type 

    def user_input(self):
        self.vehicle_type = input("Enter the vehicle type: ")      


class Automibile(Vehicle):
    def __init__(self, vehicle_type, make, year, model, doors, roof):
        super().__init__(vehicle_type)
        self.make = make
        self.year = year
        self.model = model
        self.doors = doors
        self.roof = roof

    def user_input(self):
        super().user_input()
        self.make = input("Enter the make: ").capitalize()
        while True:
            try:
                self.year = int(input("Enter the year (4 digits): "))
                if len(str(self.year)) == 4 and self.year > 1980:
                    break
                else:
                    print("Year must be 4 digits and greater than 1980")
            except ValueError:
                print("Year must be a number")
        self.model = input("Enter the model: ").capitalize()

        while True:
            try:
                self.doors = int(input("Enter the number f doors (2/4):"))
                if self.doors == 2 or self.doors == 4:
                    break
                else:
                    print("Number of doors must be 2 or 4")
            except ValueError:
                print("Number of doors must be a number")        

        self.roof = input("Enter the type of roof (sun/solid): ").lower()
        while self.roof not in ["sun", "solid"]:
            print("Invalid input. Please enter 'sun' or 'solid'.")
            self.roof = input("Enter the type of roof (sun/solid): ").lower()       

    def car_info(self):
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.doors}")
        print(f"Type of Roof: {self.roof} roof")    



Automibile1 = Automibile("Car", "Toyota", "2019", "Camry", "4", "sun")
Automibile1.car_info()

Automibile1.user_input()
Automibile1.car_info()

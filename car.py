class car:
    colour=None
    model=None
    def car_details(self):
        print("The car details are", self.colour,self.model)

colour=input("Enter the colour")
model=input("Enter the model")
car_obj=car()
car_obj.colour=colour
car_obj.model=model
car_obj.car_details()
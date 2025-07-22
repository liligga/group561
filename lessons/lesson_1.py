class Car:
    # инициализатор
    def __init__(self, model, year):
        # свойства, атрибуты, поля
        self.model = model
        self.year = year
        self.fined = False

    def drive_to_location(self, location):
       print(f"Driving {self.model} to {location}")

if __name__ == '__main__':
    subaru_model = "Subaru Forester"
    car_subaru = Car("Forester", 2020)
    car_honda = Car("Honda Fit", 2021)
    print("Model", car_subaru.model, "Year", car_subaru.year, "fined", car_subaru.fined)
    #print(car_honda)
    car_honda.drive_to_location("Kant")
    print(type(subaru_model))
    print(type(car_subaru))
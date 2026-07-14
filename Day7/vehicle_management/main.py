from car import Car
from ev import EV
from polymorphism import overloading_demo
from exception import VehicleError
from report_export import export_vehicle_data

def main():
    try:
        car1=Car("Toyota","Corolla",2022)
        car2=EV("Tesla","Model 3", 2023,75)

        car1.set_owner("Alice")
        car2.set_owner("Bob")

        vehicle=[car1,car2]

        print(car1.show_info(),car1.get_owner())
        print(car2.show_info(),car2.get_owner())

        print("\n-- OVerlaoding Demo--")
        overloading_demo()

        print("\n--Export Report--")
        print(export_vehicle_data("vehicle_report.csv",vehicle))
    
    except VehicleError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

# car1=Car("Toyota","Camry",2020)
# car2=Car("Honda","Civic",2021)
# ev1=EV("Tesla","Model S",2022,100)

# car1.set_owner("MAdhumitha")
# car2.set_owner("Vidya")
# car2.set_owner("lakshmi")
# print("Owner of car1:", car1.get_owner())
# print("Owner of car2:", car2.get_owner())

# car1.start_engine()
# car1.show_info()

# car2.start_engine()
# car2.show_info()

# ev1.show_info()
# ev1.start_engine()
# ev1.charge_battery()

# cars=[car1,car2]
# for car in cars:
#     car.start_engine()
#     car.show_info()


# ev2=EV("Skoda","Rapido",2021,-50)
# overloading_demo()
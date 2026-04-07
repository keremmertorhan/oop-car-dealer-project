class Car:
    instance_count = 0

    def __init__(self, brand, model, year, max_speed, plate_number):
        self.brand = brand
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.velocity = 0
        self.color = "not defined"

        if not isinstance(plate_number, int) or not (100000 <= plate_number <= 999999):
            raise ValueError("Plate number must be a six-digit integer.")

        self.plate_number = plate_number
        Car.instance_count += 1

    def change_color(self, new_color):
        self.color = new_color

    def run(self):
        self.velocity = 0.75 * self.max_speed
        print(f"{self.brand} {self.model} is now running at {self.velocity} km/h.")

    def stop(self):
        self.velocity = 0
        print(f"{self.brand} {self.model} has stopped.")

    def get_car_info_as_list(self):
        return [
            self.brand,
            self.model,
            self.year,
            self.max_speed,
            self.velocity,
            self.color,
            self.plate_number
        ]

    def __str__(self):
        return (
            f"{self.year} {self.brand} {self.model} | "
            f"Color: {self.color} | "
            f"Plate: {self.plate_number}"
        )

    @classmethod
    def print_instance_count(cls):
        print(f"Currently, there are {cls.instance_count} car objects defined.")


class CarDealer:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
        self.cars_list = []

    def add_car(self, car):
        if isinstance(car, Car):
            self.cars_list.append(car)
        else:
            raise TypeError("Only Car objects can be added to the dealer.")

    def __str__(self):
        if not self.cars_list:
            return f"The car dealer {self.name} has no cars in the list."

        dealer_info = f"The car dealer {self.name} ({self.brand}) has the following cars:\n"
        cars_info = "\n".join(
            f"- {car.brand} {car.model} ({car.year}) | Color: {car.color}"
            for car in self.cars_list
        )
        return dealer_info + cars_info


def main():
    try:
        car1 = Car("BMW", "M8", 2023, 320, 170190)
        car2 = Car("Mercedes", "CLA", 2022, 260, 434512)
        car3 = Car("Honda", "Accord", 2021, 180, 513242)
        car4 = Car("Ford", "Mustang", 2024, 280, 512345)
        car5 = Car("Toyota", "Corolla", 2024, 220, 986786)

        print(car1)
        car1.run()
        car1.change_color("Black")
        print(car1)
        car1.stop()

        print("\nList of values for one car instance:")
        print(car4.get_car_info_as_list())

        print("\nInformation about other instances:")
        print(car2)
        print(car3)

        Car.print_instance_count()

        dealer1 = CarDealer("Premium Cars", "Mixed Brands")
        dealer1.add_car(car2)
        dealer1.add_car(car4)
        dealer1.add_car(car5)

        print("\nDealer Information:")
        print(dealer1)

    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Type Error: {e}")


if __name__ == "__main__":
    main()

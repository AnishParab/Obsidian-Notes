# Encapsulation in Python

``` python
class SportsCar:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        self.__is_engine_on = False
        self.__current_speed = 0
        self.__current_gear = 0
        self.__tyre_company = "MRF"

    @property
    def speed(self):
        return self.__current_speed

    @property
    def tyre_company(self):
        return self.__tyre_company

    @tyre_company.setter
    def tyre_company(self, value):
        if not value:
            raise ValueError("Tyre company cannot be empty")
        self.__tyre_company = value

    def start_engine(self):
        self.__is_engine_on = True
        print(f"{self.__brand} {self.__model}: Engine starts with a roar!")

    def shift_gear(self, gear):
        if not self.__is_engine_on:
            print(f"{self.__brand} {self.__model}: Engine is off! Cannot shift gear.")
            return
        self.__current_gear = gear
        print(f"{self.__brand} {self.__model}: Shifted to gear {self.__current_gear}")

    def accelerate(self):
        if not self.__is_engine_on:
            print(f"{self.__brand} {self.__model}: Engine is off! Cannot accelerate.")
            return
        self.__current_speed += 20
        print(f"{self.__brand} {self.__model}: Accelerating to {self.__current_speed} km/h")

    def brake(self):
        self.__current_speed = max(0, self.__current_speed - 20)
        print(f"{self.__brand} {self.__model}: Braking! Speed is now {self.__current_speed} km/h")

    def stop_engine(self):
        self.__is_engine_on = False
        self.__current_gear = 0
        self.__current_speed = 0
        print(f"{self.__brand} {self.__model}: Engine turned off.")


my_car = SportsCar("Ford", "Mustang")
my_car.start_engine()
my_car.shift_gear(1)
my_car.accelerate()
my_car.shift_gear(2)
my_car.accelerate()
my_car.brake()
my_car.stop_engine()

print(f"Current Speed: {my_car.speed}")

my_car.tyre_company = "Bridgestone"
print(f"Tyre Company: {my_car.tyre_company}")

# my_car.__current_speed = 500  # won't work as expected — name mangling
# my_car._SportsCar__current_speed = 500  # this works — Python can't truly block it
```

---
# Key differences from C++

- `__field` instead of `private` — name mangled, not truly blocked
- `@property` instead of `getSpeed()` — cleaner, accessed like an attribute not a method
- No `delete` — GC handles cleanup
- Added validation in `tyre_company.setter` — C++ version had none

---

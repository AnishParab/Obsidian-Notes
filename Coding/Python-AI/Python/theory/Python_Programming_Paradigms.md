# Example: Functional-Based Programming
``` python
def make_chai():
    if not kettle_has_water():
        fill_kettle()
    plug_in_kettle()
    boil_water()
    if not is_cup_clean():
        wash_cup()
    add_to_cup("tea leaves")
    add_to_cup("sugar")
    pour("boiled water")
    stir("cup")
    serve("chai")

make_chai()
```

---
# Example: Class-Based Programming
``` python
class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip(self):
        print("Sipping chai")

    def add_sugar(self, amount):
        print("Added sugar")

my_chai = Chai(sweetness=3, milk_level=2)
my_chai.add_sugar(3)
my_chai.sip()
```

---

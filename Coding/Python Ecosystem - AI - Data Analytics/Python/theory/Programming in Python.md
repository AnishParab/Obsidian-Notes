# Programming
- Giving instructions to a computer to perform tasks.

---
# Why Python
- **Portable:** Runs on Windows, macOS, Linux
- **Readable:** Simple, clean syntax
- **Productive:** Less code, faster development
- **Rich Standard Library:** Built-in support for common tasks
- **Versatile:** Used for web, data, AI, automation, games

---
# Key Features
- Interpreted
- Dynamically typed
- High-level
- Extensible with C/C++
- Open source
- Large community & **PyPI ecosystem**

---
# Python Applications
- **Web:** Django, Flask
- **Data Science:** NumPy, Pandas, Matplotlib
- **ML/AI:** TensorFlow, PyTorch, scikit-learn
- **Automation:** Selenium, PyAutoGUI
- **Games:** Pygame
- **GUI:** Tkinter, PyQt

---
# Example Code: Functional Based
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
# Example Code: Class Based
``` python
class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level
        
    def sip(self):
	    print("Sipping chai")
		
	def add_sugar(self, amount):
	    print("added the sugar")
		
my_chai = Chai(sweetness=3, milk_level=2)

my_chai.add_sugar(3)
my_chai.sip()
```

---

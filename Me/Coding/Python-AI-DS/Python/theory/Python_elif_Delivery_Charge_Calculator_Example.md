# Problem
**Delivery Charge Calculator**
- You’re building a delivery system for an e-commerce platform. Depending on the distance of the customer’s address, different delivery charges apply.  

**Tasks:**
1. Take input from the user for delivery distance in Kilometers and store it in a variable named distance.
2. If the distance is **2 km or less**, return the string: "Delivery charge: 0"
3. If the distance is **greater than 2 km but not more than 5 km**, return the string: "Delivery charge: 30"
4. If the distance is **greater than 5 km but not more than 10 km**, return the string: "Delivery charge: 50"
5. If the distance is **more than 10 km**, return the string: "Delivery not available for your location."

---
# Code
``` python
distance = input("Delivery distance in kilometers.\n")

distance = int(distance)

if distance <= 2:
    print("Delivery charge is 0 rupees")
elif distance > 2 and distance <= 5:
    print("Delivery charge is 30 rupees")
elif distance > 5 and distance <= 10:
    print("Delivery charge is 50 rupees")
else:
    print("Delivery not available for your location.")
```

---

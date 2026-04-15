# Problem
You're building a smart thermostat alert system:
- If the `device_status` is "active"
	- And `temperature` > 35 -> Warn: "High temperature alert!"
	- Else: "Temperature normal"
- If device is off -> "Device is offline"

---
# Code with `pass` keyword
- `pass` is a null statement. It does nothing when executed. Used as a placeholder where syntax requires a statement but no action is needed.

``` python
device_status = "active"
temperature = 38

if device_staus == "active":
	pass # to be implemented later
else:
	print("Device is offline")
```

---
# Final Code
``` python
device_status = "active"
temperature = 38

if device_staus == "active":
	if temperature > 35:
		print("High temperature alert!")
	else:
		print("Temperature is normal")	
else:
	print("Device is offline")
```

---

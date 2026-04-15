> Multiple cores engaged.

---
# Example Parallelism
``` python
from multiprocessing import Process
import time

def brew_chai(name):
	print(f"Start of {name} chai brewing")
	time.sleep(3)
	print(f"End of {name} chai brewing")
	
if __name__ == "__main__":
	chai_makers = [
		Process(target = brew_chai, args=(f"Chai Maker #{i+1}", ))
		for i in range(3)
	]
	
	# Start all process
	for p in chai_makers:
		p.start()
	
	# Wait for all to complete
	for p in chai_makers:
		p.join()
		
	print("All chai served")
```

**Output**
``` text
Start of Chai Maker #1 chai brewing
Start of Chai Maker #2 chai brewing
Start of Chai Maker #3 chai brewing
End of Chai Maker #1 chai brewing
End of Chai Maker #2 chai brewing
End of Chai Maker #3 chai brewing
All chai served
```


---
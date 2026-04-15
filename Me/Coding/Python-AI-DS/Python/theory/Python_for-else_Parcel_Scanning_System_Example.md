# Problem Statement
**Parcel Scanning System**
- You are automating a parcel scanning system in a warehouse. Each parcel has a barcode, and the system must validate and process each parcel while reporting any issues encountered during scanning.

##### Tasks
1. There is a list named **`parcel_code`** that contains parcel barcodes.
2. The system should iterate through each barcode using a **for loop**:
    - If a barcode is **"DAMAGED"**, skip scanning that parcel using `continue` and log:  
        `"Skipped damaged parcel"`
    - If a barcode is **"STOP"**, immediately halt the scanning process using `break` and log:  
        `"Critical error: Stopping scan"`
    - For all other valid barcodes, log:  
        `"Scanned parcel: <barcode>"`
3. If the loop completes without encountering a `break`, log:  
    `"All parcels scanned successfully"`  
    using a **for–else** construct.
4. Return a list containing **all scan log messages**.

---
# Code
``` python
def scan_parcels(parcel_codes: list[str]):
    logs = []

    for barcode in parcel_codes:
        if barcode == "DAMAGED":
            logs.append("Skipped damaged parcel")
            continue
        if barcode == "STOP":
            logs.append("Critical error: Stopping Scan")
        logs.append(f"Scanned parcel: {barcode}")
    else:
        print("All parcels scanned successfully")

    return logs


parcels = ["A123", "B456", "DAMAGED", "C789"]
print(scan_parcels(parcels))
```

---

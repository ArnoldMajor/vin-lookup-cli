# Vehicle VIN Lookup System

## Overview
The **Vehicle VIN Lookup System** is a command-line interface (CLI) application that allows users to store, search, and manage vehicle records using a vehicle's **VIN (Vehicle Identification Number)**

## Features
✅ Add a vehicle with its VIN, make, model, and year  
✅ Retrieve details of a vehicle by VIN  
✅ List all stored vehicles  
✅ Search vehicles by make, model, or year  
✅ Delete a vehicle record  
✅ User-friendly CLI interface using **Click**  
✅ Database management with **SQLite and SQLAlchemy**  


## Installation & Setup
### **1 Clone the Repository**
```bash
git clone https://github.com/ArnoldMajor/vin-lookup-cli.git
cd vin-lookup-cli
```

### **2 Create a Virtual Environment**
```bash
pipenv shell
```

### **3 Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4 Run the CLI Application**
To see available commands:
```bash
python main.py --help
```

## How to use the CLI Application
### **Add a Vehicle**
```bash
python main.py add-vehicle
```
**Example Input:**
```
Vehicle VIN: ABC1234XYZ
Vehicle Make: Toyota
Vehicle Model: Corolla
Vehicle Year: 2020
```

### **List All Vehicles**
```bash
python main.py list-vehicles
```

### **Find a Vehicle by VIN**
```bash
python main.py find-vehicle ABC1234XYZ
```

### **Delete a Vehicle**
```bash
python main.py delete-vehicle ABC1234XYZ
```

## Future Enhancements
- Search vehicles by make, model, or year  
- Update vehicle details  
- Integrate an external API for VIN validation  


## License
This project is open-source and available under the **MIT License**.

import pandas as pd
import random
from datetime import datetime, timedelta

# Configuration
NUM_PARTS = 500

# Data lists
categories = [
    "Engine Parts", "Brake System", "Suspension", "Electrical",
    "Transmission", "Exhaust System", "Cooling System", "Fuel System"
]

manufacturers = [
    "Bosch", "Denso", "Continental", "Delphi", "Valeo",
    "Mahle", "NGK", "Brembo", "ZF", "Hella"
]

part_names = {
    "Engine Parts": ["Piston", "Cylinder Head", "Camshaft", "Crankshaft", "Oil Pump"],
    "Brake System": ["Brake Pad", "Brake Disc", "Brake Caliper", "Master Cylinder"],
    "Suspension": ["Shock Absorber", "Coil Spring", "Control Arm", "Ball Joint"],
    "Electrical": ["Alternator", "Starter Motor", "Battery", "Spark Plug"],
    "Transmission": ["Clutch Kit", "Gearbox", "Drive Shaft", "CV Joint"],
    "Exhaust System": ["Muffler", "Catalytic Converter", "Exhaust Manifold"],
    "Cooling System": ["Radiator", "Water Pump", "Thermostat", "Cooling Fan"],
    "Fuel System": ["Fuel Pump", "Fuel Injector", "Fuel Filter", "Throttle Body"]
}

# Generate data
data = []
for i in range(NUM_PARTS):
    category = random.choice(categories)
    part_name = random.choice(part_names[category])
    manufacturer = random.choice(manufacturers)
    
    # Price based on category
    base_prices = {
        "Engine Parts": (150, 800),
        "Brake System": (50, 400),
        "Suspension": (80, 500),
        "Electrical": (40, 350),
        "Transmission": (200, 1200),
        "Exhaust System": (100, 600),
        "Cooling System": (60, 400),
        "Fuel System": (70, 450)
    }
    
    price_range = base_prices[category]
    price = round(random.uniform(price_range[0], price_range[1]), 2)
    
    stock = random.randint(0, 100)
    part_number = f"{manufacturer[:3].upper()}-{random.randint(1000, 9999)}"
    
    data.append({
        "Part Number": part_number,
        "Part Name": part_name,
        "Category": category,
        "Manufacturer": manufacturer,
        "Price": price,
        "Stock": stock,
        "Status": "In Stock" if stock > 10 else "Low Stock" if stock > 0 else "Out of Stock"
    })

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
output_file = "auto_parts_data.xlsx"
df.to_excel(output_file, index=False, sheet_name="Auto Parts")

print(f"✅ Generated {NUM_PARTS} auto parts records")
print(f"📁 Saved to: {output_file}")
print(f"\n📊 Summary:")
print(f"  - Categories: {df['Category'].nunique()}")
print(f"  - Manufacturers: {df['Manufacturer'].nunique()}")
print(f"  - Price range: ${df['Price'].min():.2f} - ${df['Price'].max():.2f}")
print(f"  - Average price: ${df['Price'].mean():.2f}")

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import random

st.set_page_config(
    page_title="Auto Parts Analysis",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Auto Parts Analysis Dashboard")
st.markdown("Interactive analysis of automotive parts inventory and pricing")

# Load data
@st.cache_data
def load_data():
    data_file = Path("auto_parts_data.xlsx")
    if not data_file.exists():
        st.info("Generating sample data...")
        generate_sample_data()
    return pd.read_excel(data_file)

def generate_sample_data():
    """Generate sample auto parts data"""
    import random
    
    NUM_PARTS = 500
    
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
    
    data = []
    for i in range(NUM_PARTS):
        category = random.choice(categories)
        part_name = random.choice(part_names[category])
        manufacturer = random.choice(manufacturers)
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
    
    df = pd.DataFrame(data)
    df.to_excel("auto_parts_data.xlsx", index=False, sheet_name="Auto Parts")

df = load_data()

# Sidebar filters
st.sidebar.header("🔍 Filters")

categories = st.sidebar.multiselect(
    "Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

manufacturers = st.sidebar.multiselect(
    "Manufacturer",
    options=df["Manufacturer"].unique(),
    default=df["Manufacturer"].unique()
)

price_range = st.sidebar.slider(
    "Price Range ($)",
    min_value=float(df["Price"].min()),
    max_value=float(df["Price"].max()),
    value=(float(df["Price"].min()), float(df["Price"].max()))
)

# Filter data
filtered_df = df[
    (df["Category"].isin(categories)) &
    (df["Manufacturer"].isin(manufacturers)) &
    (df["Price"] >= price_range[0]) &
    (df["Price"] <= price_range[1])
]

# Metrics
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Parts", len(filtered_df))
with col2:
    st.metric("Avg Price", f"${filtered_df['Price'].mean():.2f}")
with col3:
    st.metric("Total Value", f"${filtered_df['Price'].sum():,.2f}")
with col4:
    st.metric("Categories", filtered_df["Category"].nunique())

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Parts by Category")
    category_counts = filtered_df["Category"].value_counts()
    fig1 = px.pie(
        values=category_counts.values,
        names=category_counts.index,
        hole=0.4
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("💰 Average Price by Manufacturer")
    avg_price = filtered_df.groupby("Manufacturer")["Price"].mean().sort_values(ascending=False)
    fig2 = px.bar(
        x=avg_price.values,
        y=avg_price.index,
        orientation='h',
        labels={'x': 'Average Price ($)', 'y': 'Manufacturer'}
    )
    st.plotly_chart(fig2, use_container_width=True)

# Price distribution
st.subheader("📈 Price Distribution")
fig3 = px.histogram(
    filtered_df,
    x="Price",
    nbins=30,
    labels={'Price': 'Price ($)'},
    color_discrete_sequence=['#636EFA']
)
st.plotly_chart(fig3, use_container_width=True)

# Data table
st.subheader("📋 Filtered Data")
st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# Download button
st.download_button(
    label="📥 Download Filtered Data",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_auto_parts.csv",
    mime="text/csv"
)

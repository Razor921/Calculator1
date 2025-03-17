import streamlit as st
from datetime import datetime, timedelta

# App Title
st.title("Harvest Changeout Calculator")

# Input fields
current_bin_level = st.number_input("Current Bin Level:", min_value=0.0, step=0.1, format="%.2f")
current_hfr = st.number_input("Current HFR:", min_value=0.0, step=0.1, format="%.2f")

# Target bin level and minutes
target_bin_level = 1020
minutes_per_hour = 60

# Function to calculate result
def calculate():
    if current_bin_level > 0 and current_hfr > 0:
        result = (target_bin_level - current_bin_level) / (current_hfr * minutes_per_hour)
        total_minutes = int(result * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60

        # Estimate future time
        future_time = datetime.now() + timedelta(hours=hours, minutes=minutes)
        formatted_time = future_time.strftime("%H:%M (%d %B %Y)")

        st.success(f"**Estimated Changeout Time:**\n{formatted_time}")
    else:
        st.error("Please enter valid positive numbers for both fields.")

# Button to trigger calculation
if st.button("Calculate"):
    calculate()

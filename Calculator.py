import streamlit as st
from datetime import datetime, timedelta

# Title
st.title("Harvest Changeout Calculator")

# Inputs for Current Bin Level and Current HFR
current_bin_level = st.number_input("Current Bin Level:", value=0.0, step=0.1)
current_hfr = st.number_input("Current HFR:", value=0.0000, step=0.0001, format="%.4f")  # Allows 4 decimal places

# Button to calculate
if st.button("Calculate"):
    try:
        target_bin_level = 1020
        minutes_per_hour = 60
        
        # Perform calculation
        result = (target_bin_level - current_bin_level) / (current_hfr * minutes_per_hour)
        
        total_minutes = int(result * 60)
        hours = total_minutes // 60
        minutes = total_minutes % 60
        
        # Get current time and add the result
        current_time = datetime.now()
        future_time = current_time + timedelta(hours=hours, minutes=minutes)
        
        formatted_time = future_time.strftime("%H:%M (%d %B %Y)")
        
        # Display result in large font
        st.markdown(
            f"<div style='text-align: center; font-size: 32px; color: blue;'>"
            f"**Estimate Changeout Time:**<br>{formatted_time}"
            f"</div>", 
            unsafe_allow_html=True
        )
    
    except Exception as e:
        st.error(f"Invalid input: {e}")

# Footer
st.markdown(
    "<div style='text-align: center; font-size: 14px; color: grey;'>"
    "Developed with ❤️ using Streamlit"
    "</div>",
    unsafe_allow_html=True
)

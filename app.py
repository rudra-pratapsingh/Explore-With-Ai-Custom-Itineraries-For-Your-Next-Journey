import streamlit as st
from travel import generate_itinerary

#demo-video link: 
#https://drive.google.com/drive/folders/1EZRLD1kMNIMI8wDX4Uz8sECZG19k84_9?usp=drive_link

#streamlit app
st.title("Travel Itinerary Generator")

#get user input
destination = st.text_input("Enter your desired destination: ")
days = st.number_input("Enter the number of days of your stay: ", min_value=1)
nights = st.number_input("Enter the number of nights of your stay: ", min_value=0)
description = st.text_input("Provide any other additional information here")

#Ensure that user inputs are provided
if st.button("Generate Itinerary"):
  if destination.strip() and days>0 and nights>=0:
    try:
      itinerary = generate_itinerary(
        destination=destination, days=days, nights=nights, description=description
        )
      st.text_area("Generated Itinerary: ", value = itinerary, height = 300)
    
    except Exception as e:
      st.error(f'An error occured: {e}')
  
  else:
      st.error("Make sure all the inputs are provided and are valid")


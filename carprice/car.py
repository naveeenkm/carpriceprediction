import pandas as pd
import numpy as np 
import pickle as pk
import streamlit as st
from PIL import Image 

def car_details():
   p=0
   model=pk.load(open('carprice/model.pkl','rb'))
   st.markdown(
    """
    <div style='text-align: center; background-color: #4CAF50; padding: 10px; border-radius: 10px;'>
        <h1 style='color: white; font-size: 30px;'>PREDICT THE PRICE OF YOUR SELLING CAR</h1>
    </div>
    """, 
    unsafe_allow_html=True
)
   
   cars_data=pd.read_csv("carprice/Cardetails.csv")
   
   def get_brand_name(car_name):
     car_name=car_name.split(' ')[0]
     return car_name.strip()
   
   cars_data['name']=cars_data['name'].apply(get_brand_name)
   name=st.selectbox('Select car brand',cars_data['name'].   unique())
   year=st.slider("Car Manufactured Year ",1994,2024)
   km_driven=st.slider("Number of Kilometers Driven ",11,   200000)
   fuel=st.selectbox('Fuel Type',cars_data['fuel'].unique())
   seller_type=st.selectbox('Seller Type',cars_data   ['seller_type'].unique())
   transmission=st.selectbox('Transmission Type',cars_data   ['transmission'].unique())
   owner=st.selectbox('owner',cars_data['owner'].unique())
   mileage=st.slider("Car Mileage ",10,40)
   engine_cc=st.slider("Engine CC ",700,5000)
   max_power=st.slider("Max Power ",0,200)
   seats=st.slider("Number of Seats ",5,10)
   try:
       car_image = Image.open(f'car_images/{name}.jpg')
       st.image(car_image, caption=f'{name} car', use_column_width=True)
   except FileNotFoundError:
       st.write(f"Image for {name} not found.")
   
   if st.button("Predict"):
       input_data_model=pd.DataFrame([[name,year,km_driven,   fuel,seller_type,transmission,owner,mileage,engine_cc,   max_power,seats]],columns=['name','year','km_driven',   'fuel',	'seller_type','transmission','owner',   'mileage','engine','max_power','seats'])
       input_data_model['owner'].replace(['First Owner',    'Second Owner', 'Third Owner',
          'Fourth & Above Owner', 'Test Drive Car'],[1,2,3,4,   5],inplace=True)
       input_data_model['fuel'].replace(['Diesel', 'Petrol',    'LPG', 'CNG'],[1,2,3,4],inplace=True)
       input_data_model['seller_type'].replace   (['Individual', 'Dealer', 'Trustmark Dealer'],[1,2,3],   inplace=True)
       input_data_model['transmission'].replace(['Manual',    'Automatic'],[1,2],inplace=True)
       input_data_model['name'].replace(['Maruti', 'Skoda',    'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
          'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep',    'Mercedes-Benz',
          'Mitsubishi', 'Audi', 'Volkswagen', 'BMW',    'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia',    'Fiat', 'Force',
          'Ambassador', 'Ashok', 'Isuzu', 'Opel'],[i for i    in range(1,32)],inplace=True)
    
       car_price=model.predict(input_data_model)
       if car_price<0:
           car_price*=-1
       st.markdown(f'''
    <div style="background-color: lightgray; padding: 10px;">
        <p style="font-size: 32px; color: purple; margin: 0;">The car price is going to be {car_price[0]}</p>
    </div>
''', unsafe_allow_html=True)

# Create a JavaScript popup
       st.toast(f'The car price is going to be {car_price[0]}')
       st.session_state['car_predicted'] = True

    
   

        


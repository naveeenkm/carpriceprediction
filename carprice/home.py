import streamlit as st  
from PIL import Image


cars = {
    
    
    "Mercedes": {
        "image": "car photo\mercedes.jpeg",
        "info": "Mileage: 12 kmpl\n\nFeatures: Luxury, cutting-edge technology, superior comfort\n\nDuration: 5 years",
        "url":"https://www.mercedes-benz.co.in/",
        "instagram": "https://www.instagram.com/mercedesbenz/",
        "facebook": "https://www.facebook.com/MercedesBenzIndia/"
    },
    "Ford": {
        
        "image": "car photo\pford.jpeg",
        "info": "Mileage: 12 kmpl\n\nFeatures: Strong performance, safety features, sporty design\n\nDuration: 6 years",
        "url":"https://www.ford.com/?hl=in",
        "instagram": "https://www.instagram.com/ford/",
        "facebook": "https://www.facebook.com/ford/"
    
    },
    "Toyota": {
        "image": "car photo\Toyota.jpeg",
        "info": "Mileage: 14 kmpl\n\nFeatures: Durability, excellent resale value, hybrid technology\n\nDuration: 4 years",
        "url":"https://www.toyotabharat.com/",
        "instagram": "https://www.instagram.com/toyota.india/",
        "facebook": "https://www.facebook.com/TOYOTA.Global/"
    
   },
     "Mahindra": {
        "image": "car photo\Mahindra.jpeg",
        "info": "Mileage: 11 kmpl\n\nFeatures: Rugged build, off-road capability, spacious interiors\n\nDuration: 7 years",
        "url":"https://auto.mahindra.com/",
        "instagram": "https://www.instagram.com/mahindra_auto/",
        "facebook": "https://www.facebook.com/MahindraAutomotiveIndia/"
    
   },
     "Audi": {
        "image": "car photo\Audi.jpeg",
        "info": "Mileage: 13 kmpl\n\nFeatures: Quattro all-wheel drive, luxury interiors, advanced tech\n\nDuration: 3 years",
        "url":"https://www.audi.in/in/web/en.html",
        "instagram": "https://www.instagram.com/audiin/",
        "facebook": "https://www.facebook.com/audiindia/"
    
   },
     "BMW": {
        "image": "car photo\BMW.jpeg",
        "info": "Mileage: 14 kmpl\n\nFeatures: Performance-oriented, driver-focused, luxury\n\nDuration: 2 years",
        "url":"https://www.bmw.in/en/index.html",
        "instagram": "https://www.instagram.com/bmw/",
        "facebook": "https://www.facebook.com/bmwindia/"
    
   },
     "Jaguar": {
        "image": "car photo\Jaguar.jpeg",
        "info": "Mileage: 12 kmpl\n\nFeatures: British luxury, sporty performance, elegant design\n\nDuration: 4 years",
        "url":"https://www.jaguar.in/index.html",
        "instagram": "https://www.instagram.com/jaguar/",
        "facebook": "https://www.facebook.com/Jaguar/"
    
   },
     "Skoda": {
        "image": "car photo\skoda.jpeg",
        "info": "Mileage: 13 kmpl\n\nFeatures: European engineering, robust build quality, premium feel\n\nDuration: 6 years",
        "url":"https://www.skoda-auto.co.in/models/kushaq/kushaq",
        "instagram": "https://www.instagram.com/SkodaIndia/",
        "facebook": "https://www.facebook.com/SkodaIndia/"
    
   },
     "Renault": {
        "image": "car photo\Renault.jpeg",
        "info": "Mileage: 17 kmpl\n\nFeatures: Stylish design, fuel-efficient engines, affordable\n\nDuration: 1 years",
        "url":"https://www.renault.co.in/",
        "instagram": "https://www.instagram.com/RenaultIndia/",
        "facebook": "https://www.facebook.com/RenaultIndia/"
    
   },
     "Jeep": {
        "image": "car photo\Jeep.jpeg",
        "info": "Mileage: 10 kmpl\n\nFeatures: Off-road prowess, rugged design, powerful engines\n\nDuration: 5 years",
        "url":"https://www.jeep-india.com/",
        "instagram": "https://www.instagram.com/jeep/",
        "facebook": "https://www.facebook.com/jeep/"
    
   },
     "Mitsubish": {
        "image": "car photo\Mitsubish.jpeg",
        "info": "Mileage: 11 kmpl\n\nFeatures: Robust build quality, off-road capability, reliable\n\nDuration: 7 years",
        "url":"https://www.mitsubishicars.com/",
        "instagram": "https://www.instagram.com/MitsubishiMotorsOfficial/",
        "facebook": "https://www.facebook.com/MitsubishiMotors.en/"
    
   },
     "Nissan": {
        "image": "car photo\pNissan.jpeg",
        "info": "Mileage: 16 kmpl\n\nFeatures: Innovative technology, reliability, efficient performance\n\nDuration: 6 years",
        "url":"https://www.nissan.in/",
        "instagram": "https://www.instagram.com/Nissan_India/",
        "facebook": "https://www.facebook.com/nissanindia/"
    
   },
     "Maruti": {
        "image": "car photo\maruti.jpeg",
        "info":"""
          **Mileage:** 15 kmpl  
            **Features:**  
             - Air Conditioning
             - Power Steering
             - Power Windows
             - Anti-lock Braking System
             - Leather Seats
        """
        "duration:4 years",
        "url":"https://www.marutisuzuki.com/",
        "instagram": "https://www.instagram.com/marutisuzukiofficial/",
        "facebook": "https://www.facebook.com/MarutiSuzukiOfficial/"

        
    },
    "Honda": {
        "image": "car photo\honda.jpeg",
        "info": "Mileage: 16 kmpl\n\nFeatures: Reliable, smooth engine performance, high resale value\n\nDuration: 3 years",
        "url":"https://www.hondacarindia.com/",
        "instagram": "https://www.instagram.com/hondacarindia/",
        "facebook": "https://www.facebook.com/HondaCarIndia/"
    },
    "Hyundi": {
        "image": "car photo\hyundai.jpeg",
        "info": "Mileage: 14 kmpl\n\nFeatures: Modern design, feature-rich interiors, strong warranty\n\nDuration: 4 years",
        "url":"https://www.hyundai.com/in/en",
        "instagram": "https://www.instagram.com/hyundaiindia/",
        "facebook": "https://www.facebook.com/HyundaiIndia/"
    },
     
}


def app():
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if st.session_state.logged_in:
        st.title("Car Information App")
        

        #car_option = st.selectbox("Select a car", list(cars.keys()))

        for car_option in list(cars.keys()):
            car = cars[car_option]
            col1, col2 = st.columns([5,3])
            with col1:
                
                
                st.image(car["image"], caption=car_option,width=420)
            with col2:
            
                st.markdown(f"**Information:** {car['info']}")
                st.markdown(f"<a href='{car['url']}' target='_blank'>More information about {car_option}</a>", unsafe_allow_html=True)
                st.markdown(f"""
                    <a href='{car['instagram']}' target='_blank'>
                        <img src='https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png' alt='Instagram' style='width:40px;height:40px;'>
                    </a>
                
                <a href='{car['facebook']}' target='_blank'>
                        <img src='https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg' alt='Facebook' style='width:40px;height:40px;margin-left:10px;'>
                </a>
                """, unsafe_allow_html=True)
                
                
                


            # HTML button
                

            # Placeholder for displaying the result
                
                

                    
            # Add CSS for styling
                st.markdown("""
                <style>
                    body {
                        background-color: #f0f2f6;
                        font-family: Arial, sans-serif;
                        
                    }
                    .stImage {
                        border: 2px solid black;
                        border-radius: 3px;
                        padding: 2px;
                        width: 50%;
                        border-color:black;
                    
                        
                    }
                    .stMarkdown {
                        font-size: 20px;
                        
                    }
                    a {
                        color: #FF4B4B;
                        text-decoration: none;
                    }
                    a:hover {
                        text-decoration: underline;
                    }
                    .social-logo {
                        width: 40px;
                        height: 40px;
                        margin-top: 10px;
                        margin-left: 10px;
                    }
                </style>
                
            """, unsafe_allow_html=True)
    else:
        st.markdown(
        """
        <style>
        .stApp {
            background-image: url('https://wallpapers.com/images/featured/1920-x-1080-car-4sdj5tojfx747aly.jpg');
            background-size: cover;
            background-size: 100% 100%;
            background-repeat: no-repeat;
            background-position: center
        }
        </style>
        """,
        unsafe_allow_html=True
    )
        st.write("Login/Signup first")
    
    












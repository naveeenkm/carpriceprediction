import streamlit as st
if not hasattr(st, '_is_prepared'):
    st.set_page_config(page_title="Predict car price")
    st._is_prepared = True
from streamlit_option_menu import option_menu
import about, account, home, CarNews, car,logout,user_account


class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({"title": title, "function": func})

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Car Price',
                options=['Home', 'Signin/Signup', 'Car News', 'About', ],
                icons=['house-fill', 'person-circle', 'newspaper', 'info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app == "Home":
            home.app()
        elif app == "Signin/Signup":
            account.app()
        elif app == "Car News":
            CarNews.app()
        elif app == 'About':
            about.app()

    def run_login(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Car Price',
                options=['Home', 'Predict Price of Car', 'Car News', 'About','Account', 'Logout'],
                icons=['house-fill', 'car-front-fill', 'newspaper', 'info-circle-fill','person-circle','box-arrow-right'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
        if app == "Home":
            home.app()
        elif app == "Predict Price of Car":
            car.car_details()
        elif app == "Car News":
            CarNews.app()
        elif app == 'About':
            about.app()
        elif app == 'Account':
            user_account.app()
        elif app == 'Logout':
            logout.logout_person()
    


app = MultiApp()

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    app.run_login()
else:
    app.run()


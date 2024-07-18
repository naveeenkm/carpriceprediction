import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import json
import requests
import car,main
from main import MultiApp

# Firebase setup
if not firebase_admin._apps:
    cred = credentials.Certificate("car-price-prediction-9f2c1-8f2cda31f055.json")
    firebase_admin.initialize_app(cred)
st.session_state.logged_in = False
key=st.session_state.logged_in
def app():
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
    #print(st.session_state.logged_in)
    # Initialize session state variables
    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Main headline
    if st.session_state.logged_in:
        st.title(f'Welcome :violet[{st.session_state.username}]')
    else:
        st.title('Welcome  :violet[User]')

    # Functions for authentication
    def sign_up_with_email_and_password(email, password, username=None, return_secure_token=True):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp"
            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": return_secure_token
            }
            if username:
                payload["displayName"] = username 
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                return r.json()['email']
            except:
                st.warning(r.json())
        except Exception as e:
            st.warning(f'Signup failed: {e}')

    def sign_in_with_email_and_password(email=None, password=None, return_secure_token=True):
        rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"
        try:
            payload = {
                "returnSecureToken": return_secure_token
            }
            if email:
                payload["email"] = email
            if password:
                payload["password"] = password
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            try:
                data = r.json()
                user_info = {
                    'email': data['email'],
                    'username': data.get('displayName')  # Retrieve username if available
                }
                return user_info
            except:
                st.warning(data)
        except Exception as e:
            st.warning(f'Signin failed: {e}')

    def reset_password(email):
        try:
            rest_api_url = "https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode"
            payload = {
                "email": email,
                "requestType": "PASSWORD_RESET"
            }
            payload = json.dumps(payload)
            r = requests.post(rest_api_url, params={"key": "AIzaSyApr-etDzcGcsVcmaw7R7rPxx3A09as7uw"}, data=payload)
            if r.status_code == 200:
                return True, "Reset email Sent"
            else:
                error_message = r.json().get('error', {}).get('message')
                return False, error_message
        except Exception as e:
            return False, str(e)

    def login():
        try:
            userinfo = sign_in_with_email_and_password(st.session_state.email_input, st.session_state.password_input)
            st.session_state.username = userinfo['username']
            st.session_state.useremail = userinfo['email']
            st.session_state.logged_in = True
        except:
            st.warning('Login Failed')

    def signout():
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.session_state.useremail = ''

    def forget_password():
        email = st.text_input('Email')
        if st.button('Send Reset Link'):
            success, message = reset_password(email)
            if success:
                st.success("Password reset email sent successfully.")
            else:
                st.warning(f"Password reset failed: {message}")

    if not st.session_state.logged_in:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        st.session_state.email_input = email
        st.session_state.password_input = password

        if choice == 'Sign up':
            username = st.text_input("Enter your unique username")
            if st.button('Create my account'):
                user = sign_up_with_email_and_password(email=email, password=password, username=username)
                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
                st.balloons()
        else:
            st.button('Login', on_click=login)
            forget_password()
            
    if st.session_state.logged_in:
        
        st.markdown(f'Email id: <span style="color: blue;">{st.session_state.useremail}</span>', unsafe_allow_html=True)
        # car.car_details()
        run=MultiApp()
        run.run_login()
       
        st.button('Sign out', on_click=signout)

    def ap():
        st.write('Posts')

app()

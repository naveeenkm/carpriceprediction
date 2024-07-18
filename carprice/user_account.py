import streamlit as st
from PIL import Image
import os
import firebase_admin
from firebase_admin import credentials, firestore, auth
from datetime import date

# Initialize Firebase
if not firebase_admin._apps:
    cert = credentials.Certificate("car-price-prediction-9f2c1-8f2cda31f055.json")
    firebase_admin.initialize_app(cert)

db = firestore.client()

def app():
    
    # Ensure session state variables are set
    if 'username' not in st.session_state:
        st.session_state.username = 'Guest'
    if 'useremail' not in st.session_state:
        st.session_state.useremail = 'guest@example.com'
    if 'fullname' not in st.session_state:
        st.session_state.fullname = 'Guest User'
    if 'dob' not in st.session_state:
        st.session_state.dob = date(2000, 1, 1)  # Default date of birth
    if 'profile_photo' not in st.session_state:
        st.session_state.profile_photo = None

    st.title(f'Account Information of :blue[{st.session_state.username}]')

    # Profile Photo Upload
    st.markdown("### Profile Photo")
    uploaded_file = st.file_uploader("Choose a profile photo", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.session_state.profile_photo = image

        # Optionally save the uploaded image to a file
        with open(os.path.join("uploads", "profile_photo.png"), "wb") as f:
            f.write(uploaded_file.getbuffer())

    # Display the profile photo
    if st.session_state.profile_photo is not None:
        st.image(st.session_state.profile_photo, width=150, caption="Profile Photo")
    else:
        st.image('https://via.placeholder.com/150', width=150, caption="Profile Photo")

    # Display username, email, fullname, and dob
    st.markdown(f"**Name:** {st.session_state.username}")
    st.markdown(f"**Email:** {st.session_state.useremail}")
    st.markdown(f"**Full Name:** {st.session_state.fullname}")
    st.markdown(f"**Date of Birth:** {st.session_state.dob}")

    # Additional information
    # st.markdown("### Additional Information")
    # st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lacinia odio vitae vestibulum vestibulum.")

    if 'edit_mode' not in st.session_state:
        st.session_state.edit_mode = False

    if st.session_state.edit_mode:
        # Editing profile
        st.markdown("### Edit Profile")
        new_username = st.text_input("Username", st.session_state.username)
        new_email = st.text_input("Email", st.session_state.useremail)
        new_fullname = st.text_input("Full Name", st.session_state.fullname)
        new_dob = st.date_input("Date of Birth", st.session_state.dob)

        if st.button("Save Changes"):
            # Update session state
            st.session_state.username = new_username
            st.session_state.useremail = new_email
            st.session_state.fullname = new_fullname
            st.session_state.dob = new_dob
            
            try:
                # Update Firebase
                user_ref = db.collection('users').document(st.session_state.useremail)
                user_ref.update({
                    'username': new_username,
                    'email': new_email,
                    'fullname': new_fullname,
                    'dob': str(new_dob)
                })
                st.success("Profile updated successfully!")
            except Exception as e:
                st.error(f"An error occurred while updating the profile: {e}")

            st.session_state.edit_mode = False

        if st.button("Cancel"):
            st.session_state.edit_mode = False

    else:
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("Edit Profile"):
                st.session_state.edit_mode = True

        with col2:
            if st.button("Change Password"):
                change_password()

        with col3:
            if st.button("Log Out"):
                st.session_state.logged_in = False
                st.session_state.username = ''
                st.session_state.useremail = ''
                st.experimental_rerun()

def change_password():
    st.markdown("### Change Password")
    current_password = st.text_input("Current Password", type="password")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm New Password", type="password")

    if st.button("Update Password"):
        if new_password != confirm_password:
            st.error("Passwords do not match!")
        else:
            try:
                user = auth.get_user_by_email(st.session_state.useremail)
                auth.update_user(user.uid, password=new_password)
                st.success("Password updated successfully!")
            except Exception as e:
                st.error(f"An error occurred while updating the password: {e}")

# Ensure you have a directory named "uploads"
if not os.path.exists("uploads"):
    os.makedirs("uploads")

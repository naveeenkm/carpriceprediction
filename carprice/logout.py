import streamlit as st

def logout_person():
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
    st.title(f'Hello :violet[{st.session_state.username}]')
    st.markdown(f'Email: {st.session_state.useremail}')
    st.write("Are you sure you want to log out?")

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Yes, log out"):
            st.session_state.logged_in = False
            st.session_state.username = ''
            st.session_state.useremail = ''
            st.experimental_rerun()
    
    with col2:
        if st.button("No, go back"):
            st.experimental_rerun()

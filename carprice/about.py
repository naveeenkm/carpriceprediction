import streamlit as st

def app():
    st.title(f'About :violet[Us]')

    # Custom CSS for styling
    st.markdown(
        """
        <style>
        /* Set page background color */
        body {
            background-color: #f0f0f0;
            color: #333;
            font-family: Arial, sans-serif;
            line-height: 1.6;
        }
        /* Set header background color */
        .header-text {
            background-color: #3498db;
            color: white;
            padding: 10px;
            border-radius: 5px;
        }
        /* Set section background color */
        .section {
            background-color: #ecf0f1;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        /* Set hyperlink color */
        a {
            color: #2980b9;
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Team Members section
    
    st.markdown('<div class="header-text">Team Members</div>', unsafe_allow_html=True)
    st.markdown("""
    - Naveen K M
    - Padmashree U
    - Prajna H V
    - Rajendra G Gouda
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Contact Information section
    
    st.markdown('<div class="header-text">Contact Information</div>', unsafe_allow_html=True)
    st.markdown("7204529266")
    st.markdown('</div>', unsafe_allow_html=True)

    # Location section with hyperlink
    
    st.markdown('<div class="header-text">Location</div>', unsafe_allow_html=True)
    st.markdown("[Jawaharlal Nehru National College of Engineering, Shimoga](https://example.com)")
    st.markdown('</div>', unsafe_allow_html=True)

    # About the Project section
    
    st.title(f'About This :violet[Application]')
    st.markdown("""
    Our project focuses on predicting car prices using machine learning techniques. The aim is to develop a model that can accurately estimate the market value of cars based on various features such as make, model, year, mileage, engine size, and more.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    # Key Features section
    
    st.markdown('<div class="header-text">Key Features</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Data Collection:** We gathered a comprehensive dataset comprising car listings with detailed information.
    - **Data Preprocessing:** We cleaned and prepared the data, handling missing values and outliers.
    - **Feature Engineering:** We selected relevant features and engineered new ones to enhance prediction accuracy.
    - **Model Development:** We experimented with several machine learning algorithms, including regression models and ensemble methods.
    - **Evaluation:** We evaluated our models using metrics such as Mean Absolute Error (MAE) and Root Mean Square Error (RMSE).
    - **Deployment:** The final model is deployed using Streamlit, allowing users to input car details and get price predictions in real-time.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Main function to run the Streamlit app
def main():
    st.sidebar.title('Navigation')
    pages = {
        "About": app
    }
    selection = st.sidebar.radio("Go to", list(pages.keys()))
    page = pages[selection]
    page()

if __name__ == "__main__":
    main()

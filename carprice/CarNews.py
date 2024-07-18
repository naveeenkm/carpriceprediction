import streamlit as st
import requests

# Function to fetch car news
def app():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if st.session_state.logged_in:
        def fetch_car_news(api_url):
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.json()
            else:
                return None

        # Streamlit app
        def main():
            

            st.title("Latest Car News")
            st.markdown("Stay updated with the latest news about cars!")

            # API URL (replace with your actual API key)
            api_url = "https://newsapi.org/v2/everything?q=cars&apiKey=b5f1aaf9e0de4c47938ce1b67e2e58cb"

            # Fetch car news
            news_data = fetch_car_news(api_url)

            if news_data:
                articles = news_data.get("articles", [])
                for article in articles:
                    st.subheader(article["title"])
                    if article.get("urlToImage"):
                        st.image(article["urlToImage"], width=700)
                    st.markdown(article["description"])
                    st.markdown(f"[Read more...]({article['url']})")
                    st.write("---")
            else:
                st.error("Failed to fetch news.")

        
        main()
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
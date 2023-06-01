import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract relevant data from the webpage
    title = soup.find('h1', class_='product-title').text.strip()
    price = soup.find('span', class_='price-sales').text.strip()
    description = soup.find('div', class_='product-details-description').text.strip()

    return title, price, description

# Streamlit web app
st.title('Web Data Scraper')
url = st.text_input('Enter the URL to scrape')

if st.button('Scrape'):
    if url:
        try:
            title, price, description = scrape_data(url)
            st.write('Title:', title)
            st.write('Price:', price)
            st.write('Description:', description)
        except Exception as e:
            st.write('Error occurred:', str(e))
    else:
        st.write('Please enter a URL to scrape.')

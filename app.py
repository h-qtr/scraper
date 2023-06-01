import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_data(url):
    # Send a GET request to the URL
    response = requests.get(url)

    if response.status_code == 200:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the desired elements on the page
        product_titles = soup.find_all('h5', class_='product-title')
        product_prices = soup.find_all('div', class_='price-box')

        # Extract the data from the found elements
        titles = [title.text.strip() for title in product_titles]
        prices = [price.text.strip() for price in product_prices]

        # Return the scraped data
        return titles, prices
    else:
        st.error('Failed to retrieve data from the website.')

# Streamlit UI
st.title('Web Data Scraper')

# URL input field
url = st.text_input('Enter the URL')

# Scrape button
if st.button('Scrape'):
    if url:
        titles, prices = scrape_data(url)
        if titles and prices:
            # Display the scraped data
            st.header('Product Titles:')
            for title in titles:
                st.write(title)

            st.header('Product Prices:')
            for price in prices:
                st.write(price)
        else:
            st.warning('No data found on the webpage.')
    else:
        st.warning('Please enter a URL.')


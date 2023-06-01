import requests
from bs4 import BeautifulSoup
import streamlit as st

@st.cache
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

# Web scraping and displaying the data
st.title("Web Data Scraper")
url = "https://www.jarir.com/qa-en/"

# Scrape the website
soup = scrape_website(url)

# Find and display the desired data
product_titles = soup.find_all('h2', class_='product-title')

st.header("Product Titles")
for title in product_titles:
    st.write(title.get_text(strip=True))

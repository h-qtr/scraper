import requests
from bs4 import BeautifulSoup
import streamlit as st

def scrape_wikipedia(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the main content div on the page
    content_div = soup.find(id='mw-content-text')
    
    # Find all the paragraphs within the content div
    paragraphs = content_div.find_all('p')
    
    # Extract the text from the paragraphs
    text = '\n'.join([p.get_text() for p in paragraphs])
    
    return text

# Define the URL to scrape
url = 'https://en.wikipedia.org/wiki/Library_Genesis'

# Scrape the data
data = scrape_wikipedia(url)

# Use Streamlit to display the scraped data
st.title("Web Data Scraper")
st.header("Scraped Content from Wikipedia")
st.text(data)

import requests
from bs4 import BeautifulSoup
import streamlit as st

# Function to scrape the website
def scrape_website(url):
    # Send a GET request to the URL
    response = requests.get(url)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract the desired data
    cars = []
    car_elements = soup.find_all('div', class_='classified-listing')
    for car_element in car_elements:
        title = car_element.find('h3', class_='list-title').text.strip()
        price = car_element.find('span', class_='price').text.strip()
        cars.append({'Title': title, 'Price': price})
    
    return cars

# Main code
st.title("Web Data Scraper")
url = "https://www.pakwheels.com/used-cars/family-cars/587667"
cars = scrape_website(url)

# Display the scraped data using Streamlit
if cars:
    st.subheader("Scraped Car Data")
    for car in cars:
        st.write(f"Title: {car['Title']}")
        st.write(f"Price: {car['Price']}")
        st.write("---")
else:
    st.error("Failed to scrape data from the website.")

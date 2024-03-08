import requests
from bs4 import BeautifulSoup

def scrape_e_commerce():
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='col-sm-4 col-lg-4 col-md-4')
    
        with open('scraped_data.txt', 'w', encoding='utf-8') as f:
            for item in items:
                name = item.find('a', class_='title').text.strip()
                price = item.find('h4', class_='pull-right price').text.strip()
                reviews = item.find('p', class_='pull-right').text.strip()

                print(f"Name: {name}\nPrice: {price}\nReviews: {reviews}\n")
                f.write(f"Name: {name}\nPrice: {price}\nReviews: {reviews}\n\n")
        
        print("Scraping successful! Data saved to scraped_data.txt")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

scrape_e_commerce()

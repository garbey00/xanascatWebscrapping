import requests
from bs4 import BeautifulSoup

# Replace the URL with the website you want to scrape
url = 'https://xanascat.gencat.cat/ca/programes/vacances-en-familia/primera-convocatoria-2024?field_hostel_target_id_verf=All&field_taxon_stay_type_target_id=All&page=0'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Example: Extract all the links on the page
    trs = soup.find_all('tr')
    
    print("List of rows:")
    for tr in trs:
        print(tr)
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

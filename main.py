import requests
from bs4 import BeautifulSoup
import csv

csv_file_path = 'xanascat.csv'


def process_page(url: str):
    # Replace the URL with the website you want to scrape
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'lxml')

        # Example: Extract all the links on the page
        trs = soup.find_all('tr')

        i = 0
        for tr in trs:
            if i == 0:
                i = i + 1
                continue
            #print(tr.contents)
            alberg = tr.contents[1].string.rstrip()
            print(alberg)
            tipus = tr.contents[5].string.rstrip()
            print(tipus)
            datas = tr.contents[3]
            datainici = datas.contents[0].string.rstrip()
            datafi = datas.contents[2].string.rstrip()
            print(datainici)
            print(datafi)

            writer.writerow([alberg, datainici, datafi, tipus])
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    base_url = 'https://xanascat.gencat.cat/ca/programes/vacances-en-familia/primera-convocatoria-2024?field_hostel_target_id_verf=All&field_taxon_stay_type_target_id=All'

    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        for i in range(39):
            url = base_url + '&page=' + str(i)
            print(url)
            process_page(url)
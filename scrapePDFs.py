import os 
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

#URL of huberman lab transcripts
url = 'https://readthatpodcast.com'


# # specifiy folder path
folder_location = r'./files'
if not os.path.exists(folder_location):os.mkdir(folder_location)


response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")
for link in soup.select("a[href$='.pdf']"):
    # Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
            f.write(requests.get(urljoin(url,link['href'])).content)

def count_files_in_directory(directory):
    return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])

# Use it like this:
num_files = count_files_in_directory('./files')
print(f'There are {num_files} files in the directory.')

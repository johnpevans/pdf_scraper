#! python3
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests


# Different sites
sites_for_scraping = [
'https://www.state.nj.us/humanservices/dmahs/info/fads.html',
'https://www.state.nj.us/humanservices/providers/rulefees/decisions/dmahs2014.html',
'https://www.state.nj.us/humanservices/dmahs/info/fads_2015.html',
'https://www.state.nj.us/humanservices/dmahs/info/fads_2016.html',
'https://www.state.nj.us/humanservices/dmahs/info/fads_2017.html',
'https://www.state.nj.us/humanservices/dmahs/info/fads_2018.html',
'https://www.state.nj.us/humanservices/dmahs/info/fads_2019.html'
]

scraped_urls = []

for parent_directory in sites_for_scraping:
    r = requests.get(parent_directory)
    soup = bs(r.text, 'lxml')

    for name, link in enumerate(soup.findAll('a')):
        href_link = 'https://www.state.nj.us' + str(link.get('href'))
        if href_link.endswith('.pdf'):
            scraped_urls.append(href_link)

for address in scraped_urls:
    try:
        downloads_folder = r'C:\Users\[INPUT_PATH_HERE]]'
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_experimental_option("prefs", {
            "download.default_directory": downloads_folder,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "plugins.always_open_pdf_externally": True
            })

        driver = webdriver.Chrome(options = options)
        driver.get(address)

        driver.quit
    except:
        print("Download complete!")

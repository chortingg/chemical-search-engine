pip install beautifulsoup4
pip install google
pip install pandas
import urllib as ul
import os
import time
import requests
import bs4
import PyPDF2
from io import BytesIO
from urllib.parse import urljoin
import pandas as pd
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
     
query = "hp gse"
  
for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
    print(j)
driver.get("https://google.com")
search = driver.find_element(By.NAME, "q")
search.send_keys("hp gse")
search.send_keys(Keys.RETURN)
link = driver.find_element(By.PARTIAL_LINK_TEXT, "HP's General Specification for the Environment (GSE)")
link.click()
time.sleep(10)
actions = ActionChains(driver)
actions.send_keys(Keys.TAB * 14)
actions.perform()
actions.send_keys(Keys.RETURN)
actions.perform()
def get_n_first_pages(n: int):
    pages = [2]
page_source = driver.page_source
pages.append(driver.page_source)

def get_pdf(link: str):
    pdf_name = link.split("/")[-1].split(".")[0]
    pdf_link = [
        urljoin(link, l.attrs["href"])
    ]
    pdf_link = pdf_link[0]

pdf_bytes = requests.get(pdf_link).content
p = BytesIO(pdf_bytes)
p.seek(0, os.SEEK_END)
read_pdf = PyPDF2.PdfFileReader(p)
count = read_pdf.numPages
pages_txt = []

for i in range(count):
    page = read_pdf.getPage(i)
    pages_txt.append(page.extractText())

return pdf_name, pages_txt

pages = get_n_first_pages(2)

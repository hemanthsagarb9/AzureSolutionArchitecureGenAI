import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from urllib.parse import urljoin
import json

base_url = "https://learn.microsoft.com"

driver = webdriver.Chrome(service=Service())

_page_url = "https://learn.microsoft.com/en-us/azure/architecture/browse/?skip="

all_archs = []
for i in range(0, 636, 6):
    try:
        page_url = _page_url+str(i)
        driver.get(page_url)

        time.sleep(20)

        architecture_links = driver.find_elements(By.CLASS_NAME, 'card-content-title.stretched-link')

        for link in architecture_links:
            relative_url = link.get_attribute('href')
            full_url = urljoin(base_url, relative_url)
            title = link.text.strip()
            all_archs.append({"title": title, "url": full_url})
    except Exception as e:
        print({"error": str(e)})
driver.quit()

open("azure_archs.json", "w").write(json.dumps(all_archs, indent=4))

from bs4 import BeautifulSoup
import re
import requests
import sys

URL = "http://applications.huntingdonshire.gov.uk/applications/RefuseCalendarMVC/100091196457"

page_res = requests.get(URL)
if page_res.status_code != 200:
    print(f"Failed with status code {page_res.status_code}: {page_res.reason}")
    sys.exit(1)

page_soup = BeautifulSoup(page_res.content, "html.parser")

for bin_type in ["domestic waste", "mixed dry recycling", "garden waste"]:
    parent_el = page_soup.find_all(string=re.compile(f"The {bin_type} in your"))[0].parent
    date_el = parent_el.contents[1]
    print(f"{bin_type}: {date_el.string}")

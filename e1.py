import requests
from bs4 import BeautifulSoup as bs

url='http://historical.elections.virginia.gov/elections/search/' \
    + 'year_from:1924/year_to:2016/office_id:1/stage:General'

r=requests.get('http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General')


s=bs(r.text, 'html.parser')
items=s.find_all('tr', 'election_item')
text=""

for i in items:
    if text!="":
        text+="\n"
    text+=i.find('td',{"class":"year"}).text+" "+i.get("id").split('-')[-1]
   
with open("ELECTION_ID", "w") as output:
    output.write(text)
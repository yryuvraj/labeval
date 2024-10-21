import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://saras.cbse.gov.in/SARAS/AffiliatedList/ListOfSchdirReport'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table') 

headers = [header.text for header in table.find_all('th')]

rows = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    cols =  cols.find_all('b')
    cols = [ele.text.strip() for ele in cols]
    rows.append(cols)

df = pd.DataFrame(rows, columns=headers)

print(df)

s = df[df['School & Head Name'].str.contains('Rajesh Kumar')]['School & Head Name'].values

s = 'GURU HARKRISHAN PUBLIC SCHOOL'

if len(s) > 0:
    print(f"The school with the head: {s}")

t = df['S No'].nunique()
print(f"Total count of unique schools: {t}")

x = df[df['School & Head Name'].str.contains('AMITY INTETNATIONAL SCHOOL')]['School & Head Name'].values
print(x)

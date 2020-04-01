import requests 
from bs4 import BeautifulSoup
import csv

area_name = "Chankyapuri"
locality_score = 9.8



URL = input("Enter the url: ")
r = requests.get(URL)
pageurls = []
pageurls.append(URL)
soup = BeautifulSoup(r.content, 'html.parser')

table = soup.findAll('a', attrs = {'aria-label':'previous page'})


for row in table:
    if row['href'][len(row['href']) -1] != '2':
        pageurls.append(row['href'])

#finds all the pages with the urls of speicifc locality
while(True):
    size = len(pageurls)
    lasturl = pageurls[size-1]
    r = requests.get(lasturl)
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.findAll('a', attrs = {'aria-label':'previous page'})
    for row in table:
        if row['href'] not in pageurls :
            if row['href'][len(row['href']) -1] == '2'  and row['href'][len(row['href']) -1] != '=':
                pageurls.append(row['href'])
            elif row['href'][len(row['href']) -1] != '2':
                pageurls.append(row['href'])

    newsize = len(pageurls)
    if newsize == size:
        break

print(pageurls)
for URL in pageurls:
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser') 
    print("Processing...")

    #getting all the urls
    table = soup.findAll('meta', attrs = {'itemprop':'url'})
    urls = []
    for row in table:
        urls.append(row['content'])
    urls = urls[0:-1]

    available = []
    notAvailable = []
    records = []
    types = []
    bhks = []
    sizes = []
    prices = []
    statuses = []
    ages = []
    URLS = []
    urls = list(dict.fromkeys(urls))

    for url in urls:
        if(".jpg" not in url):
            URL = url
            URLS.append(url)
            r = requests.get(URL)
            soup = BeautifulSoup(r.content, 'html.parser') 
            table = soup.findAll('span', attrs = {'class':'md-name'})
            for row in table:
                name = row.text

            splits = name.split(" BHK ")
            if(len(splits)>=2):
                BHK = splits[0]
                Type = splits[1]
            else:
                BHK = -1
                Type = "NA"
            types.append(Type)
            bhks.append(BHK)

            table = soup.findAll('span', attrs = {'class':'md-size'})
            if(table is not None):
                for row in table:
                    size = row.text
                size = size.replace(" sq ft","")
                size = size.replace(",","")
            else:
                size = 0
            sizes.append(size)

            table = soup.findAll('span', attrs = {'class':'val'})
            if(table is not None):
                for row in table:
                    price = float(row.text)
            else:
                price = 0
            prices.append(price)

            table = soup.findAll('td', attrs = {'id':'Status'})
            if(table is not None):
                for row in table:
                    status = row.text
            else:
                status = "NA"
            statuses.append(status)
            age = ""
            try:
                age_full = soup.find('td',attrs = {'id':'Age of Property'}).text
                if("years" in age_full):
                    age_full = age_full.replace(" years","")
                elif("year" in age_full):
                    age_full = age_full.replace(" year","")
                agesA = age_full.split(" - ")
                age = agesA[1]
            except:
                age = ""
            ages.append(age)
            quotes = ""
            table = soup.find('div', attrs = {'id':'amenity'})
            if(table is not None):
                rows = table.findAll('span', attrs = {'itemprop':"amenityFeature"})
                if(rows is not None):
                    for row in rows:
                        quotes += row.text + ","
                else:
                    quotes += ","

            available.append(quotes)
        
            quotes = ""
            table = soup.findAll('div', attrs = {'class':'disabled'})
            if(table is not None):
                for subtable in table:
                    rows =  subtable.findAll('span', attrs = {'itemprop':"amenityFeature"})
                    if(rows is not None):
                        for row in rows:
                            quotes += row.text + ","
            notAvailable.append(quotes)
        else:
            urls.remove(url)

    myList = []
    for i in range(len(available)):
        tempList = []
        for j in range(12):
            tempList.insert(j,0)
        if("Swimming Pool" in available[i] and "Swimming Pool" not in notAvailable[i]):
            tempList.insert(0,1)
        
        if("Lift Available" in available[i] and "Lift Available" not in notAvailable[i]):
            tempList.insert(1,1)
        
        if("Jogging Track" in available[i] and "Jogging Track" not in notAvailable[i]):
            tempList.insert(2,1)
        
        if("Indoor Games" in available[i] and "Indoor Games" not in notAvailable[i]):
            tempList.insert(3,1)
        
        if("Gymnasium" in available[i] and "Gymnasium" not in notAvailable[i]):
            tempList.insert(4,1)
        
        if("Club House" in available[i] and "Club House" not in notAvailable[i]):
            tempList.insert(5,1)

        if("Children's play area" in available[i] and "Children's play area" not in notAvailable[i]):
            tempList.insert(6,1)
        
        if("Car Parking" in available[i] and "Car Parking" not in notAvailable[i]):
            tempList.insert(7,1)
        
        if("ATM" in available[i] and "ATM" not in notAvailable[i]):
            tempList.insert(8,1)
        
        if("Sports Facility" in available[i] and "Sports Facility" not in notAvailable[i]):
            tempList.insert(9,1)
        
        if("Multipurpose Room" in available[i] and "Multipurpose Room" not in notAvailable[i]):
            tempList.insert(10,1) 

        tempList = tempList[0:11]
        record = [types[i],bhks[i],area_name,locality_score,sizes[i],ages[i]]
        record.extend(tempList)
        record.append(statuses[i])
        record.append(prices[i])
        record.append(URLS[i])
        records.append(record)
        tempList.clear()


    with open("Data.csv","a",newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(records)
    csvFile.close()

# with open("visitedLinks.txt","a") as f:
#     for i in range(len(urls)):
#         st = str(i+1) + " : " + urls[i] + "\n"
#         f.write(st)
# f.close()
print(records)
print("Done!")




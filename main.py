import requests
from bs4 import BeautifulSoup
import csv
fields = ['Code', 'Height', 'Width', 'Length','Weight','Description'] 

def filter_product_code(code):
    parts = code.split(":")
    return parts[1].strip()

def name_to_id(name):
    name = name.replace("-","")
    name = " ".join(name.split())
    id = name.replace(" ","-").lower()
    id = id.replace(".","")
    id = id.replace("%","")
    id = id.replace("(","")
    id = id.replace(")","")
    id = id.replace("/","")
    return id

def get_product_data_by_name(name):
    id = name_to_id(name)
    
    
    url = "https://hyalite.com.au/products/"+id
    response = requests.get(url).text
    print(url)
    soup = BeautifulSoup(response, 'html.parser')
    product_body = soup.find_all("div", class_='product__tabbody')[0]
    product_desc_codes = product_body.find_all('td')
    row = []
    for i ,product_desc_code in enumerate(product_desc_codes):
        if i in [0,2,4,6,8]:
            row.append(product_desc_code.text)
    description = product_body.find('p').text
    row.append(description)
    row[0] = filter_product_code(row[0])
    return row
    
filename = "result.csv"
rows = []

try:
    with open('product_names.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        for i,lines in enumerate(csvFile):
            try :
                if len(lines)>0:
                    row = get_product_data_by_name(lines[0])
                    rows.append(row)
                else:
                    print("Empty row at "+str(i))
               
            except Exception as e:
                
                print("Error - "+str(e)+ " - " + lines[0])
except :
    print("Something is wrong with input file")

with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows)

        

import requests
from bs4 import BeautifulSoup
import csv


def get_all_products():
    names = []
    for i in range(1,62):
        try :

            response = requests.get("https://hyalite.com.au/search?page="+str(i)).text
            # with open("all_page.html","w") as page:
            #     page.write(response)
            soup = BeautifulSoup(response,"html.parser")

            product_list = soup.find("div",class_="products__list")
            products = product_list.find_all("span", class_="prodcard__title")
            
            for product in products:
                names.append([product.text])
        except Exception as e:
            print(i,e)
    return names


names = get_all_products()
print(names)
with open("product_names.csv" , "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(names)



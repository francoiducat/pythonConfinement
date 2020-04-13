import requests
from bs4 import BeautifulSoup
import pandas

base_url = "http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/#t=0&s="

l = []
for page in range(0, 30, 10):
    print(base_url+str(page)+".html")

    r = requests.get(base_url+str(page)+".html", headers={
        'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

    c = r.content

    soup = BeautifulSoup(c, "html.parser")

    divs = soup.findAll("div", {"class": "propertyRow"})

    for div in divs:
        d = {}

        # print("\n")

        d["Address"] = div.findAll(
            "span", {"class": "propAddressCollapse"})[0].text
        d["Locality"] = div.findAll(
            "span", {"class": "propAddressCollapse"})[1].text

        price = div.find("h4", {"class": "propPrice"})
        # print(price.text.replace("\n", "").replace(" ", ""))
        d["Price"] = price.text.replace("\n", "").replace(" ", "")

        try:
            # print(beds.find("b").text)
            d["Beds"] = div.find("span", {"class": "infoBed"}).find("b").text
        except:
            # print("None")
            d["Beds"] = None

        try:
            # print(div.find("span", {"class": "infoSqFt"}).find("b").text)
            d["Area"] = div.find("span", {"class": "infoSqFt"}).find("b").text
        except:
            d["Area"] = None

        try:
            # print(div.find("span", {"class": "infoValueFullBath"}).find("b").text)
            d["Full Baths"] = div.find(
                "span", {"class": "infoValueFullBath"}).find("b").text
        except:
            d["Full Baths"] = None

        try:
            # print(div.find("span", {"class": "infoValueHalfBath"}).find("b").text
            d["Half Baths"] = div.find(
                "span", {"class": "infoValueHalfBath"}).find("b").text
        except:
            d["Half Baths"] = None

        for column_group in div.findAll("div", {"class": "columnGroup"}):
            for feature_group, feature_name in zip(column_group.findAll("span", {"class": "featureGroup"}), column_group.findAll("span", {"class": "featureName"})):
                # print(feature_group.text, feature_name.text)
                if "Lot Size" in feature_group.text:
                    # print(feature_name.text)
                    d["Lot Size"] = feature_name.text
        # print(d)
        l.append(d)
    # print(l)

df = pandas.DataFrame(l)
# print(df)

df.to_csv("resources/data.csv")

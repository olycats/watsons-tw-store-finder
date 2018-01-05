import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

response = requests.get("https://www.watsons.com.tw/store-finder")
page = BeautifulSoup(response.text, "lxml")

df = pd.DataFrame(columns=['storeName', 'storeAddress', 'storeTel', 'storeHours'])
for i in range(0, 1000):
    storeInfo = page.find("div", id="storeInfo" + str(i))
    if storeInfo is None:
        continue
    googlemapPinContent_gmapPin1Content = storeInfo.find("div", class_="googlemapPinContent gmapPin1Content")
    googlePinStore_clearfix = googlemapPinContent_gmapPin1Content.find("div", class_="googlePinStore clearfix")

    # 門市名稱、門市地址
    storeInfo_fl = googlePinStore_clearfix.find("div", class_="storeInfo fl")
    # storeName
    try:
        df.at[i, 'storeName'] = storeInfo_fl.find("h4", class_="storeName mb10").string
    except:
        pass
    # storeAddress
    try:
        df.at[i, 'storeAddress'] = storeInfo_fl.find("p", class_="storeAddress").string
    except:
        pass

    # 門市電話、營業時間
    googlePinStoreInfo_clearfix = googlemapPinContent_gmapPin1Content.find("div", class_="googlePinStoreInfo clearfix")
    if googlePinStoreInfo_clearfix is None:
        continue
    # storeTel
    try:
        if googlePinStoreInfo_clearfix.find("h4").string == "門市電話":
            df.at[i, 'storeTel'] = googlePinStoreInfo_clearfix.find("h4").find_next_sibling("p").string
    except:
        pass
    # storeHours
    try:
        if googlePinStoreInfo_clearfix.find("h5").string == "門市":
            mb20 = googlePinStoreInfo_clearfix.find("h5").find_next_sibling("p", class_="mb20")
            text = ""
            for x in mb20:
                try:
                    text = text + "".join(x.split())
                except:
                    text = text + "\n"
            text = text.rstrip("\n")
            df.at[i, 'storeHours'] = text
    except:
        pass

# output to csv
df.to_csv(path_or_buf=os.path.join(os.getcwd(), "store-finder.csv"), encoding="UTF-8", index=False)

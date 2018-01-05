# watsons-tw-store-finder
使用Python的BeautifulSoup套件，擷取屈臣氏門市列表。

資料來源： [StoreFinder | 屈臣氏 Watsons](https://www.watsons.com.tw/store-finder) 
![webpage](/screenshots/webpage.png?raw=true "webpage")

輸出結果（csv檔）： 
![webpage](/screenshots/store_finder_csv.png?raw=true "webpage")

## Requirements

須安裝[Python3](https://www.python.org/)以及Python語言的[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)套件

安裝BeautifulSoup4 (for Ubuntu 16.04)
```
sudo apt-get install python3-bs4
```


## Code structure


File/Folder          |	Description
 --------------------| ------------------------------------------------ 
.gitignore           | gitignore
README.md            | README
screenshots          | README.md使用的截圖
store-finder-crawler.py| 網頁爬蟲的程式碼
store-finder.csv     | 網頁爬蟲的結果



## 輸出結果
執行 store-finder-crawler.py ，會將結果輸出為CSV檔案：

* store-finder.csv

    除標題欄、標題列之外，共有5欄 * N列。

    欄位名稱      |資料範例
    --------    | ---------------------------------- 
    storeName   | 一心
    storeAddress| 高雄市前鎮區一心二路45號,高雄市,高雄市前鎮區,802
    storeTel    | (07)3300900
    storeHours  | 一~日9:30AM-11:00PM

    其中「營業時間」包含換行字元。

## 我的開發環境：
* Ubuntu 16.04.3 LTS
* Python 3.5.2
* PyCharm Community Edition 2017.2.4

尚未在其他環境測試，不確定是否能支援。

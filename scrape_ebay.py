import bs4, numpy, pandas, requests

# example url - Books/Antiquarian and Collectible
baseurl = 'https://www.ebay.ca/b/Antiquarian-Collectible-Books/29223/bn_1865565?_pgn='
startpage = 1 # initialize at the start page

currentpage = startpage
limit = 5 # max pages to scrape
item_num = 1 # starting item number, used in the final spreadsheet
dataframe = pandas.DataFrame(columns=["Number","Name","Price","PageURL"])

while currentpage <= limit:
    targeturl = baseurl + str(currentpage)
    print(targeturl)
    page = requests.get(targeturl)
    pagesoup = bs4.BeautifulSoup(page.content, features="html.parser")
    pageitems = pagesoup.find_all('li', class_="s-item")
    item_title = []
    for item in pageitems:
        item_title = item.find_all('h3', class_="s-item__title")[0].text
        item_price = item.find_all('span', class_='s-item__price')[0].text
        # append data to new row of DataFrame
        
    currentpage += 1 # increment the page by 1

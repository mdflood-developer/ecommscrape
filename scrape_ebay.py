import bs4, numpy, pandas, requests

# example url - Books/Antiquarian and Collectible
baseurl = 'https://www.ebay.ca/b/Antiquarian-Collectible-Books/29223/bn_1865565?_pgn='
startpage = 1 # initialize at the start page

currentpage = startpage # Ebay listings always begin at 1
limit = 5 # max pages to scrape
dataframe = pandas.DataFrame(columns=["Name","Price","PageURL"])

while currentpage <= limit:
    targeturl = baseurl + str(currentpage)
    print(targeturl)
    page = requests.get(targeturl)
    pagesoup = bs4.BeautifulSoup(page.content, features="html.parser")
    pageitems = pagesoup.find_all('li', class_="s-item")
    for item in pageitems:
        item_title = item.find_all('h3', class_="s-item__title")[0].text
        item_price = item.find_all('span', class_="s-item__price")[0].text
        item_url = item.find_all('a', class_="s-item__link")[0]['href']

        if "New Listing" in item_title:
            item_title = item_title[11:]

        if "C $" in item_price:
            item_price = item_price[3:]

        row_data = {
                    'Name':item_title,
                    'Price':item_price,
                    'PageURL':item_url
                    }
        dataframe = dataframe.append(row_data, ignore_index=True)
        #dataframe = dataframe.append(row_data, ignore_index=True)

    currentpage += 1 # increment the page by 1

dataframe.to_csv('antiquarian-books.csv', sep=",")
print("Scrape completed")

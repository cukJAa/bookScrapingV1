from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import datetime 


def scrapeBooks():
    books = []
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    with pd.ExcelWriter(f'output/booksFromPagesV1[{current_time}].xlsx', engine='openpyxl', mode='w') as writer:
        session = requests.Session()
        print(f"Scraping started [{current_time}]")
        for i in range(1,51):
            session = requests.Session()
            url = f"https://books.toscrape.com/catalogue/page-{i}.html"
            result = session.get(url)
            result  = result.content
            soup = BeautifulSoup(result, "html.parser")
           
            ol = soup.find('ol')
            articles = ol.find_all('article', class_ = 'product_pod')
            
            pageOfBooks = []

            for article in articles:
                image = article.find('img')
                imgSource = image['src']
                imgSource = imgSource.replace('../', 'https://books.toscrape.com/')
                
                star = article.find('p', class_ = 'star-rating')
                star = star['class'][1]
                star_map = {'One': f"{1} out of {5} ",
                            'Two': f"{2} out of {5} ", 
                            'Three': f"{3} out of {5} ", 
                            'Four': f"{4} out of {5} ", 
                            'Five': f"{5} out of {5} "}
                star = star_map.get(star, f"{0} out of {5} ")

                title = image.attrs['alt']
                
                price = article.find('p', class_ = 'price_color').text
                price = float(price[1:])

                books.append([imgSource, star, title, price])
                pageOfBooks.append([imgSource, star, title, price])

                df = pd.DataFrame(pageOfBooks, columns=['Image Source', 'Star Rating', 'Title', 'Price'])
                df.to_excel(writer, index=False, sheet_name=f'Books Page {i}') 
    
    df_all = pd.DataFrame(books, columns=['Image Source', 'Star Rating', 'Title', 'Price'])
    df_all.to_csv(f'output/booksFromPagesV1[{current_time}].csv', index=False)
    currentTimeAfterScrape = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print(f"Scraping finished at [{currentTimeAfterScrape}]. Data saved to output directory")

# Book scraper with scheduler / Basic automation pipeline

- This Python project scrapes book data from a website every 5 minutes using a scheduler. 
- It saves the results into CSV files and XLSX files where each page is a worksheet.

---

## Folder Structure

- project/
- ├── scraper/ # Contains the scraping logic (webScraper.py)
- ├── scheduler/ # Runs the scheduled scraping every 5 minutes (runScheduler.py)
- ├── output/ # Where data are stored
- ├── main.py # Starts the whole program
- ├── requirements.txt
- └── README.md

---

## How it works 

- 'main.py'  - starts the program 
- It runs 'runScheduler.py' from the 'scheduler' folder.
- The scheduler uses 'scheduler.py' to run the 'webScraper' from 'scraper' folder every 5 minutes using 'schedule'
- The scraper user 'requests', 'BeautifulSoup4' to fetch books data from https://books.toscrape.com
- Data is saved in 'output/' folder in .csv file and .xlsx file where each page is a worksheet

---

## How to run 

- Clone repository 
- Install requrements (pip install -r requirements.txt)
- Run the program (python main.py)

---

## List of main libraries used:

- requests
- beautifulsoup4
- schedule
- pandas


---

## Output

- ouput/booksFromPagesV1[datetime].csv -> contains book data with named columns at index 0 (ImageUrl, Rating, Title, Price)
- ouput/booksFromPagesV1[datetime].xlsx -> contains book data with named columns at index 0 (ImageUrl, Rating, Title, Price) 
                                         with pagination each page of URL into worksheet named Book Page (the number of page)  
- Every scheduled run give a new file .csv and .xlsx with the timestamp of the time scraped
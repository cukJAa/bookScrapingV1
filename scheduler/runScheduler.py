import schedule
import time
from datetime import datetime
from scraper.webScraper import scrapeBooks

def startScheduler():
    print("Starting the initial scrape...")
    scrapeBooks()
    print("Scheduling the scraping task every  5 minutes...")
    
    schedule.every(5).minutes.do(scrapeBooks)

    while True:
        schedule.run_pending()
        time.sleep(1)
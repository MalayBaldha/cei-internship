
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests
import yfinance as yf
import pandas as pd

def stocks_url_getter(url):
    # Set up Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Load the webpage
    # url = 'https://www.5paisa.com/stocks/all'
    root = 'https://www.5paisa.com'
    driver.get(url)

    # Get page source and parse with BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the specific div container (replace 'stock-directory__listname' with the actual class name)
    div_container = soup.find('div', class_='stock-directory__listname')

    # Extracting all stock links within the specific div container
    stock_links = []
    if div_container:
        for link in div_container.find_all('a', href=True):
            href = link['href']
            if '/stocks/' in href:
                stock_name = link.text.strip()
                stock_links.append({'name': stock_name, 'link': root + href})

    # Printing all stock links
    # for stock in stock_links:
    #     print(f"Stock Name: {stock['name']}, Link: {stock['link']}")

    # Close the browser
    driver.quit()

    return stock_links


def get_stock_info(url):

    # Set up Selenium WebDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Load the webpage
    driver.get(url)

    # Get page source and parse with BeautifulSoup
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    try:
        nse_code = soup.find('span', id='nsecode').text.strip()
        stock_name = soup.find('h1', class_='stock-page__heading').text.replace(" Share Price", "").strip()

        # Define the stock ticker symbol (e.g., 'ACC.NS' for ACC Ltd.)
        ticker = nse_code + '.NS'
        # print(ticker)
        # Define the date range
        start_date = '2024-01-01'
        end_date = '2024-06-30'

        # Fetch historical data
        stock_data = yf.download(ticker, start=start_date, end=end_date)

        # Rename columns for clarity
        stock_data.rename(columns={
            'Open': 'Open Price',
            'Close': 'Close Price',
            'High': 'High Price',
            'Low': 'Low Price',
            'Volume': 'No. of Shares'
        }, inplace=True)

        # Add a placeholder for 'No. of Trades' (as yfinance does not provide this data)
        stock_data['No. of Trades'] = None
        stock_data['Company Name'] = stock_name
        # Reset index to make 'Date' a column
        stock_data.reset_index(inplace=True)
        stock_data = stock_data[['Date', 'Company Name', 'Open Price', 'Low Price', 'High Price', 'Close Price', 'No. of Shares', 'No. of Trades']]
        
        print(f"{stock_name} Completed!!!")
        driver.quit()
        return stock_data
    except:
        return pd.Series()

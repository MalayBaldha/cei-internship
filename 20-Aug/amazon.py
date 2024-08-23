import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import pandas as pd

async def scrape_amazon_category(category):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        result = []
        # Search for the category on Amazon
        search_url = f"https://www.amazon.in/s?k={category.replace(' ', '+')}"
        await page.goto(search_url)
        pages = 1
        product_urls = []

        while len(product_urls) < 101:
            # Extract product URLs from the search results using JavaScript in the browser context
            urls = await page.evaluate(''' () => {
                                        return Array.from(document.querySelectorAll('.s-main-slot .s-result-item h2 a')).map(a => a.href);
                                       } ''')
            
            product_urls.extend(urls)
            
            # Check if there is a next page and navigate to it
            pages += 1
            search_url = f"https://www.amazon.in/s?k={category.replace(' ', '+')}&page={str(pages)}"
            await page.goto(search_url)
            
        
        product_urls = product_urls[:1011]

        # Visit each product page and scrape information
        for url in product_urls:
            await page.goto(url)
            title = await page.query_selector('span#productTitle')
            price = await page.query_selector('span.a-price span.a-offscreen')
            rating = await page.query_selector('span.a-icon-alt')
            
            title_text = await title.inner_text() if title else 'N/A'
            price_text = await price.inner_text() if price else 'N/A'
            rating_text = await rating.inner_text() if rating else 'N/A'
            
            product = {}
            product["title"] = title_text
            product["category"] = category
            product["price"] = price_text
            product["rating"] = rating_text
            product["url"] = url

            result.append(product)
            # print(f"Title: {title_text}")
            # print(f"Price: {price_text}")
            # print(f"Rating: {rating_text}")
            # print(f"URL: {url}")
            # print("-" * 80)
            
        await browser.close()
        return result

# Run the scraper on all categories
category_names = [ "In-game Currency" , "Yoga Mats" , "Protein" , "Beverages", "Household Supplies" , "Tableware" , "Duffel Bags" , "String Instruments"]
products_list = []

for category in category_names:
    products = asyncio.run(scrape_amazon_category(category))
    print(f"{category} - Completed!!!")
    products_list.extend(products)

df = pd.DataFrame(products_list)
df.to_csv("M:/cei-internship/20-Aug/output2.csv")
from selenium import webdriver

def get_info(search_query):
    driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
    driver.get(f"https://en.wikipedia.org/wiki/{search_query}")
    # You can scrape information from the Wikipedia page here
    # For simplicity, let's just print the page title
    print("Wikipedia Page Title:", driver.title)
    driver.quit()

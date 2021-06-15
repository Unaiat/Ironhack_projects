import requests
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup



def scraping_podemos(url, title):
    """
    This function scrapes the content from one of the pages of the program of Unidas Podemos. 
    Args: The url of the website and the title of the section as strings
    Returns: A list with all the content merged
    """
    url = url
    html = requests.get(url)
    soup = BeautifulSoup(html.content,"html.parser")
    headline = BeautifulSoup(f'''<h2 class="fusion-responsive-typography-calculated">{title}</h2>''')
    headline = headline.text
    intro = soup.find_all("div", {"class": "b-description_readmore js-description_readmore"})
    introduction = [a.getText().strip() for a in intro]
    introduction = introduction[0].replace("\n\r\n", "")
    driver = webdriver.Chrome("./chromedriver")
    driver.get(url)
    titles = driver.find_element_by_xpath('//*[@id="content"]')
    finder = titles.find_elements_by_class_name('card')
    titles = []
    for i in finder:
        variable = i.find_element_by_tag_name("span")
        titles.append(variable.text)
    card_body = soup.find_all("div", {"class": "card-body"})
    text = soup.find_all('p')
    only_text = [a.getText().strip() for a in text]
    head_intro = []
    head_intro.append(headline)
    head_intro.append(introduction)
    all_together = head_intro + titles + only_text
    return all_together

def scrape_ciudadanos():
    """
    This function scrapes the program of the website of Ciudadanos. 
    Args: None
    Returns: A list with the content
    """
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://www.ciudadanos-cs.org/programa-electoral-2021-madrid-4m")
    driver.find_element_by_xpath("/html/body/div/div[4]/div/div/div/div[2]/a[2]").click()
    text = []
    for i in range(1,11):
        driver.find_element_by_css_selector(f"body > div > div.corporate--propuestas-page-content > div > div > div > div.propuestas > div:nth-child({i}) > div.heading > div > div.content > a").click()
        sleep(2)
        finder = driver.find_element_by_class_name('corporate--propuestas-page-content')
        strong = finder.find_elements_by_tag_name("li")
        #sleep(2)
        #driver.find_element_by_css_selector(f"body > div > div.corporate--propuestas-page-content > div > div > div > div.propuestas > div:nth-child({i}) > div.heading > div > div.content > a").click()
    for i in strong:
        text.append(i.text)
    return text

def get_verba(word, date):
    """
    This function downloads a requested csv from the Verba platform of Civio. 
    Args: Term to look for and dates in numbers (dd/mm/yyyy - dd/mm/yyyy), both as strings. 
    Returns: Downloads the csv to downloads folder. 
    """
    driver = webdriver.Chrome("./chromedriver")
    driver.get("https://verba.civio.es/")
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search-box"]/div[1]/input').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search-box"]/div[1]/input').send_keys(word)
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search-box"]/div[2]/button').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="search-box"]/div[2]/div/input').click()
    driver.find_element_by_xpath('//*[@id="search-box"]/div[2]/div/input').click()
    driver.find_element_by_xpath('//*[@id="search-box"]/div[2]/div/input').clear()
    driver.find_element_by_xpath('//*[@id="search-box"]/div[2]/div/input').send_keys(date)
    driver.find_element_by_xpath('/html/body/div[2]/div[4]/button[2]').click()
    sleep(3)
    driver.find_element_by_link_text('CSV').click()
    sleep(2)
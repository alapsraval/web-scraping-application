# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def mars_news():
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    if browser.is_element_present_by_css('li.slide', wait_time=10):  
        html = browser.html
        soup = bs(html, 'html.parser')
        slides = soup.find_all('li', class_='slide')
        news_title = slides[0].find('div',class_='content_title').text
        news_p = slides[0].find('div',class_='article_teaser_body').text
        print('News Headline: ', news_title)
        print('-------------')
        print(news_p,'\n')

def mars_jpl_images():
    mars_jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(mars_jpl_url)

    if browser.is_element_present_by_css('section.primary_media_feature', wait_time=10):
        browser.click_link_by_partial_text('FULL IMAGE')
        browser.click_link_by_partial_text('more info')
        html_jpl = browser.html
        soup_jpl = bs(html_jpl, 'html.parser')
        browser.find_by_css('a img.main_image').click()
        featured_image_url = browser.url # read current page url
        #option 2    
        #featured_image_url = 'https://www.jpl.nasa.gov' + soup_jpl.find('img',class_='main_image').get('src')
        #option 3
        #images = soup_jpl.find_all('div', class_='download_tiff')
        #featured_image_url = images[1].a.get('href')
        print('Featured Image URL: ', featured_image_url)

def mars_weather():
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    if browser.is_element_present_by_css('section article', wait_time=10):
        html_weather = browser.html
        soup_weather = bs(html_weather, 'html.parser')
        latest_tweet = browser.find_by_css('[data-testid="tweet"]')[0]
        mars_weather = latest_tweet.find_by_css('div.r-jwli3a.r-16dba41.r-bnwqim').text
        print('Latest Tweet')
        print('------------')
        print(mars_weather)

    html_weather = requests.get(mars_weather_url)
    soup_weather = bs(html_weather.text, 'html.parser')

    tweet_container = soup_weather.find('div', class_="js-tweet-text-container")
    latest_tweet = tweet_container.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = latest_tweet.text
    mars_weather

def mars_facts():
    mars_facts_url = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(mars_facts_url)
    df = tables[0]
    df.columns = ['Fact', 'Value']
    df['Fact'] = df['Fact'].str.replace(':', '') # remove ':' from Fact column
    df.set_index('Fact', inplace=True)
    html_table = df.to_html()
    html_table

def mars_hemi():
    mars_hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(mars_hemi_url)
    html_hemi = browser.html
    soup_hemi = bs(html_hemi, 'html.parser')
    results = soup_hemi.find_all('div',class_='item')

    hemisphere_image_urls = []
    for item in results:
        title = item.find('h3').text
        browser.click_link_by_partial_text(title)
        time.sleep(1)
        html_subpage = browser.html
        soup_subpage = bs(html_subpage, 'html.parser')
        img_url = soup_subpage.find('div', 'downloads').ul.li.a['href']
        browser.back()
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        
    hemisphere_image_urls

def scrape():
    browser = init_browser()
    listings = {}

    url = "https://chicago.craigslist.org/d/apts-housing-for-rent/search/apa?postal=60532&search_distance=100"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["headline"] = soup.find("a", class_="result-title").get_text()
    listings["price"] = soup.find("span", class_="result-price").get_text()
    listings["hood"] = soup.find("span", class_="result-hood").get_text()

    return listings

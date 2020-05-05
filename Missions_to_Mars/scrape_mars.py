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

def mars_news(browser):
    mars_news_url = 'https://mars.nasa.gov/news/'
    browser.visit(mars_news_url)
    if browser.is_element_present_by_css('li.slide', wait_time=10):  
        html = browser.html
        soup = bs(html, 'html.parser')
        slides = soup.find_all('li', class_='slide')
        news_title = slides[0].find('div',class_='content_title').text
        news_p = slides[0].find('div',class_='article_teaser_body').text

        return news_title, news_p
        # print('News Headline: ', news_title)
        # print('-------------')
        # print(news_p,'\n')

def mars_jpl_images(browser):
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
        # print('Featured Image URL: ', featured_image_url)
        return featured_image_url

def mars_weather(browser):
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)
    
    html_weather = requests.get(mars_weather_url)
    soup_weather = bs(html_weather.text, 'html.parser')

    tweet_container = soup_weather.find('div', class_="js-tweet-text-container")
    latest_tweet = tweet_container.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text")
    mars_weather = latest_tweet.text
    return mars_weather

def mars_facts():
    mars_facts_url = 'https://space-facts.com/mars/'
    
    tables = pd.read_html(mars_facts_url)
    df = tables[0]
    df.columns = ['Fact', 'Value']
    df['Fact'] = df['Fact'].str.replace(':', '') # remove ':' from Fact column
    df.set_index('Fact', inplace=True)
    html_table = df.to_html()
    return html_table

def mars_hemi(browser):
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
        
    return hemisphere_image_urls

def scrape():
    browser = init_browser()
    mars_data = {}

    news_title, news_details = mars_news(browser)

    mars_data["news_title"] = news_title
    mars_data["news_details"] = news_details
    mars_data["featured_image_url"] = mars_jpl_images(browser)
    mars_data["current_weather"] = mars_weather(browser)
    mars_data["facts"] = mars_facts()
    mars_data["hemi_urls"] = mars_hemi(browser)

    browser.quit()
    return mars_data
# Web Scraping with Python - Mission to Mars

This is a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps.

## Step 1 - Scraping

Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* A Jupyter Notebook file `mission_to_mars.ipynb` is used to complete all of the following scraping and analysis tasks.

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the complete image url to the full size `.jpg` image for the current Featured Mars Image.

### Mars Weather

* Visit the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and scrape the latest Mars weather tweet from the page.

### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Convert the data to a HTML table string

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name.

- - -

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* `index.html` displays all of the scraped data in the appropriate HTML elements.

## Requirements
### Modules Required
      * pandas           : 0.25.3
      * splinter==0.9.0
      * beautifulsoup4==4.6.3
      * requests==2.18.4
      * pymongo==3.7.1
      * numpy==1.15.0
      * Flask==1.0.2
      * requests==2.18.4
      * gunicorn==19.9.0
      * lxml==4.2.5
      * bs4==0.0.1
      * Flask-PyMongo==2.1.0

import time
 
 ## Screenshot

 ![Screenshot](https://github.com/alapsraval/web-scraping-application/blob/master/screenshots/flask_app_screenshot.png)

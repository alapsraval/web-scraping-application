# Web Scraping with Python - Mission to Mars

This is a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines the steps.

## Step 1 - Scraping

Initial scraping using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* A Jupyter Notebook file `mission_to_mars.ipynb` is used to complete all of the following scraping and analysis tasks.

### NASA Mars News

* The [NASA Mars News Site](https://mars.nasa.gov/news/) is scraped for latest News Title and Paragraph Text.

### JPL Mars Space Images - Featured Image

* Splinter is used to navigate the site for [JPL Featured Space Image](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) and find the complete image url to the full size `.jpg` image for the current Featured Mars Image.

### Mars Weather

* The latest Mars weather tweet is scraped from the [Mars Weather twitter account] (https://twitter.com/marswxreport?lang=en).

### Mars Facts

* Pandas is used to scrape the table containing facts about the planet including Diameter, Mass, etc. from the [Mars Facts webpage](https://space-facts.com/mars/) and then the data is converted to a HTML table string.

### Mars Hemispheres

* High resolution images for each of Mar's hemispheres are obtained from the [USGS Astrogeology site](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name are saved to variables.

- - -

## Step 2 - MongoDB and Flask Application

MongoDB with Flask templating is used to create a new HTML page that displays all of the information that was scraped from the URLs above.

* All of the scraped data is displayed in the appropriate HTML elements using Bootstrap Grid.

## Requirements
### Modules Required
* pandas           : 0.25.3
* splinter         : 0.13.0
* bs4              : 4.8.2
* python           : 3.7.5
* dateutil         : 2.8.1
* numpy            : 1.17.4
* requests         : 2.22.0
* Flask-PyMongo    : 2.3.0
* pymongo          : 3.10.1
* Flask            : 1.1.1
* chromedriver     : 2.24.1
 
 ## Screenshot

 ![Screenshot](https://github.com/alapsraval/web-scraping-application/blob/master/screenshots/flask_app_screenshot.png)

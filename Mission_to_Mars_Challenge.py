# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


# Set executable_path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## Featured Article


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)



# Parse the HTML
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')




# Parse the HTML to find the title
slide_elem.find('div', class_='content_title')




# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title




# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ## Featured Images


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)



# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()



# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')




# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel




# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ## Featured Table



# Read the table from the above website
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df




# Convert the dataframe back into html code
df.to_html()


#### D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

##### Hemispheres



# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
for x in range(3,7):
    
    # click on each title image to find each page
    title_select = browser.find_by_tag('img')[x]
    title_select.click()

    #Parse the html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    #Find the high resolution image (.jpg extension)
    img_jpg_link = img_soup.find('img', class_="wide-image").get('src')
    img_jpg_link

    # Use the base url to create an absolute url
    img_url = f'https://marshemispheres.com/{img_jpg_link}'

    #Retrieve title
    hemi_title = img_soup.find('h2', class_="title").get_text()


    # Create empty dictionary
    hemispheres = {
        "Title" : hemi_title,
        "Image URL" : img_url    
    }

    # Add the dictionary to the list
    hemisphere_image_urls.append(hemispheres)

    # Send the browser back to the home page
    browser.back()   



# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls



# 5. Quit the browser
browser.quit()







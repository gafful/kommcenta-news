from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None

def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

class News:
    # Initializer / Instance Attributes
    def __init__(self, title, img_src):
        self.title = title
        self.img_src = img_src

    def __repr__(self):
        return '<News {}>'.format(self.title) 

def get_news():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'https://www.ghanaweb.com/GhanaHomePage/'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')# soup
        names = set()
        news = set()
        # lead story

        ts_title = html.select("#lead-story .info a h2")[0].text
        ts_image_src = html.select('#lead-story img')[0]['src']
        ts_image_alt = html.select('#lead-story img')[0]['alt']

        news = News(title= ts_title, img_src=ts_image_src)
        # news = ['title']
        # for li in html.select('li'):
        #     for name in li.text.split('\n'):
        #         if len(name) > 0:
        #             names.add(name.strip())
        # return list(news)
        return news

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

news = get_news()
print(news)
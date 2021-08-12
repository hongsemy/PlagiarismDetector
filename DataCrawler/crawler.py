from urllib.parse import quote_plus
from typing import List
from bs4 import BeautifulSoup
from selenium import webdriver
import platform


# === Private Functions ===


def _google_search(keyword: str) -> List[str]:
    """
    :param keyword:
    A keyword or sentence(s) to look up on Google.
    :return:
    A list of strings where its elements are urls to top results.

    Uses keyword to google search and returns a list of link where each element
    is link to individual website in
    the top results.
    """
    base_url = "https://www.google.com/search?q="
    result_url = base_url + quote_plus(keyword)
    # concatenate to create a full url to the search result page

    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    # An option that prevents a chrome browser from opening

    system = platform.system()

    if system == "window":
        chrome_driver = webdriver.Chrome('chromedriver.exe', options=option)
    else:
        chrome_driver = webdriver.Chrome('./chromedriver', options=option)

    chrome_driver.get(result_url)       # opening url with chrome driver

    result_html = chrome_driver.page_source     # convert html file into string

    soup = BeautifulSoup(result_html, 'html.parser')

    selected_result = soup.select('.yuRUbf')
    # .yuRUbf is used to distinguish desired links from useless information
    # Google uses this class name for results

    urls = []

    for item in selected_result:    # picks out urls
        item_url = item.a.attrs["href"]
        urls.append(item_url)

    return urls


def _get_contents(url: str) -> List[str]:
    """
    :param url:
    An url to the website to crawl contents from.
    :return:
    A list of strings where its elements are string lines of main contents of
    the website.

    Uses an url to crawl contents in the linked website.
    """
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    # An option that prevents a chrome browser from opening
    chrome_driver = webdriver.Chrome("./chromedriver", options=option)
    chrome_driver.get(url)       # opening url with chrome driver

    contents_html = chrome_driver.page_source
    # convert html file into string

    soup = BeautifulSoup(contents_html, "html.parser")

    contents = soup.select("p")
    """
    'p' is used to distinguish contents surrounded by <p> tags from useless 
    information must be fixed since it cannot recognize strings surrounded by
    <a> tags and etc.
    """

    text_lst = []

    for phrase in contents:
        if phrase.string is not None:
            text_lst.append(phrase.string)

    return text_lst


# === Public Functions ===


def crawl(keyword: str) -> List[List[str]]:
    """
    :param keyword:
    A keyword or sentence(s) to look up on Google.
    :return:
    A list of strings where its elements are string lines of main contents from
    each website in the top results.
    """
    url_lst = _google_search(keyword)
    res_lst = []

    for url in url_lst:
        res_lst.append(_get_contents(url))

    return res_lst


if __name__ == "__main__":
    key = input("What to search?: ")
    res = crawl(key)
    print(res)


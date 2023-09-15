# from autoscraper import AutoScraper

# url = "https://www.mage.ai/blog/definitive-guide-to-accuracy-precision-recall-for-product-developers"

# wanted_list = ['Recall']
# scraper = AutoScraper()
# result = scraper.build(url, wanted_list )
# print(result)

from autoscraper import AutoScraper

url = "https://commons.wikimedia.org/wiki/Main_Page"

wanted_list = ['Browsing?']


scraper = AutoScraper()
result = scraper.build(url, wanted_list)
print(result)
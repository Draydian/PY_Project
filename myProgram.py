# Use the Request library
import requests
# Set the target webpage
url = 'http://172.18.58.238/index.php'
r = requests.get(url)
# This will get the full page
print(r.text)

# This will get the status code
print("Return Status:")
print("\t *", r.status_code)

# This will just get just the headers
url2 = 'http://172.18.58.238/headers.php'
h = requests.head(url2)
print("Header:")
headers = {
    'User-Agent' : 'Mobile'
}
print("**********")
# To print line by line
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

import scrapy
class MySpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://172.18.58.238/spicyx/']
    def parse(self, response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'Image Link': x.xpath(newsel).extract_first(),
            }
# To recurse next page
        Page_selector = '.next a ::attr(href)'
        next_page = response.css(Page_selector).extract_first()
        if next_page:
            yield scrapy.request(
                response.urljoin(next_page),
                callback=self.parse
            )

#Terminal Codes
#Run scrapy code (scrapy runspider ScrapyTest.py)
#Saving Json Code (scrapy runspider scrapyTest.py -o results.json -t json)

import unittest
import myProgram as prog


class Test_MySpider(unittest.TestCase):
    def test_spider(self):
        MySpider()  # call MySpider Class


if __name__ == '__main__':
    unittest.main()
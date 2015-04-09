import scrapy

class NobelSpider(scrapy.Spider):
    name = "nobelNominee"
    allowed_domains = ["http://www.nobelprize.org/"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/",
        "http://www.nobelprize.org/nomination/archive/show.php"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
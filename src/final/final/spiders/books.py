import scrapy
import json


class BooksSpider(scrapy.Spider):
    name = "Books"
    allowed_domains = ["goodreads.com"]

    genres = ['crime', 'romance', 'psychology']
    start_urls = {}

    def __init__(self, *args, **kwargs):
        super(BooksSpider, self).__init__(*args, **kwargs)
        self.ans = {genre: [] for genre in self.genres}
        self.set_start_urls()

    def set_start_urls(self):
        self.start_urls = {genre: [] for genre in self.genres}
        for j in range(5):
            if j == 0:
                count = 69
                range1 = 1
                for i in range(range1, range1 + count):
                    self.start_urls[self.genres[j]].append(
                        f'https://www.goodreads.com/list/show/11.Best_Crime_Mystery_Books?page={i}')
            elif j == 1:
                count = 69
                range1 = 1
                for i in range(range1, range1 + count):
                    self.start_urls[self.genres[j]].append(
                        f'https://www.goodreads.com/list/show/10762.Best_Book_Boyfriends?page={i}')
            elif j == 2:
                count = 34
                range1 = 1
                for i in range(range1, range1 + count):
                    self.start_urls[self.genres[j]].append(
                        f'https://www.goodreads.com/list/show/41846.Inspiring_Books?page={i}')
            elif j == 3:
                count = 20
                range1 = 1
                for i in range(range1, range1 + count):
                    self.start_urls[self.genres[j - 1]].append(
                        f'https://www.goodreads.com/list/show/691.Best_Self_Help_Books?page={i}')
            elif j == 4:
                count = 15
                range1 = 1
                for i in range(range1, range1 + count):
                    self.start_urls[self.genres[j - 2]].append(
                        f'https://www.goodreads.com/list/show/86863.Life_Transformation_Books?page={i}')

    def start_requests(self):
        for genre, urls in self.start_urls.items():
            for url in urls:
                yield scrapy.Request(url, callback=self.parse, meta={"genre": genre})

    def parse(self, response):
        genre = response.meta.get("genre")
        book_links = response.css("div.js-tooltipTrigger a::attr(href)").getall()
        #print(len(book_links))
        for link in book_links:
            link = f'https://www.goodreads.com/{link}'
            yield response.follow(link, callback=self.parse_summery, meta={"genre": genre})

    def parse_summery(self, response):
        genre = response.meta.get("genre")
        #link = response.meta.get("link")
        hold = response.css("span.Formatted::text").getall()
        #hold = response.css('div.BookPageMetadataSection__description span.Formatted::text').getall()
        nmd = [text.strip() for text in hold if text.strip()]
        summery = '\n'.join(nmd)
        #god = response.css("h1.Text::text").get()
        self.ans[genre].append(summery)

    def closed(self, reason):
        with open("./../../../../data/raw/raw.json", "w") as f:
            json.dump(self.ans, f)


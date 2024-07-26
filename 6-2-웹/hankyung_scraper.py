import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

class HanKyungScraper:
    def __init__(self):
        self.base_url = "https://www.hankyung.com/economy?page="
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_articles(self, start_date: str, end_date: str):
        articles = []
        page = 1

        while True:
            url = f"{self.base_url}{page}"
            response = self.session.get(url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'html.parser')

            # 첫 번째 기사 추출
            first_article = soup.find('ul', class_='news-list').find('li')
            if not first_article:
                break  # 더 이상 기사가 없는 경우

            date_str = first_article.find('span', class_='txt-date').text.strip()
            article_date = datetime.strptime(date_str, "%Y.%m.%d %H:%M")

            if article_date < datetime.strptime(start_date, "%Y%m%d"):
                break

            title = first_article.find('h3', class_='news-tit').text.strip()
            href = first_article.find('a')['href']
            article_content = first_article.find('p', class_='lead').text.strip()

            articles.append({
                "date": article_date.strftime("%Y.%m.%d %H:%M"),
                "date_edit": article_date.strftime("%Y.%m.%d %H:%M"),
                "href": href,
                "title": title,
                "article": article_content
            })

            # 로그를 출력하여 중간 결과 확인
            print(f"Page {page}:")
            print(f"Date: {article_date.strftime('%Y.%m.%d %H:%M')}")
            print(f"Title: {title}")
            print(f"Link: {href}")
            print(f"Article: {article_content[:200]}...")  # 내용의 일부만 출력
            print("-" * 40)

            page += 1
            if article_date > datetime.strptime(end_date, "%Y%m%d"):
                continue

        return articles

    def save_to_json(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

# Usage example:
if __name__ == "__main__":
    scraper = HanKyungScraper()
    start_date = "20240625"
    end_date = "20240725"
    articles = scraper.get_articles(start_date, end_date)
    scraper.save_to_json(articles, 'results.json')
    print(f"Total articles collected: {len(articles)}")

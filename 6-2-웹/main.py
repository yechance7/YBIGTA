from argparse import ArgumentParser
from datetime import datetime
import json
from hankyung_scraper import HanKyungScraper

def create_parser() -> ArgumentParser:
    today = datetime.today().strftime("%Y%m%d")

    parser = ArgumentParser()
    parser.add_argument("-s", "--start_date", type=str, default="20240625")
    parser.add_argument("-e", "--end_date", type=str, default=today, help=f"example: {today}")
    parser.add_argument("-o", "--output", type=str, default="results.json", help="output json file path")
    return parser

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()

    scraper = HanKyungScraper()
    articles = scraper.get_articles(args.start_date, args.end_date)

    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=4)

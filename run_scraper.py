from src.scraping.rajkot_events import scrape_rajkot_events
from src.nlp.sentiment import analyze_sentiment
from src.report_generation.business_report import generate_business_report

def main():
    print("[INFO] Scraping Rajkot Events...")
    events = scrape_rajkot_events()

    print("[INFO] Simulating trends and retailer data...")
    trends = [
        {"name": "Mirror Work Lehengas", "description": "Popular for Navratri"},
        {"name": "Indo-Western Kurtis", "description": "Favored for Diwali celebrations"}
    ]

    retailers = [
        {"name": "Anaya Couture", "summary": "Strong online engagement"},
        {"name": "Rajvi Fashion", "summary": "Discount campaigns active"}
    ]

    print("[INFO] Generating business report...")
    generate_business_report(trends, events, retailers)

    print("[DONE] Report generated at business_report.html")

if __name__ == "__main__":
    main()

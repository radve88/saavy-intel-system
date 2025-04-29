from jinja2 import Environment, FileSystemLoader
from datetime import datetime
import os

def generate_business_report(trends, events, retailers, output_path="business_report.html"):
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("report_template.html")

    report = template.render(
        report_title="Saavy Boutique Business Report",
        date=datetime.now().strftime("%Y-%m-%d %H:%M"),
        trends=trends,
        events=events,
        retailers=retailers
    )

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report)

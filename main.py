import os
import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from dotenv import load_dotenv

from year_declension import decline_year
from wine_aggregator import get_wine_sorts


def main():
    load_dotenv()
    file_path = os.getenv("FILE_PATH", default="wine.xlsx")
    wine_sorts = get_wine_sorts(file_path)

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml']),
    )
    creation_year = 1920

    template = env.get_template('template.html')

    current_year = datetime.datetime.today().year

    years_passed = current_year - creation_year
    years_text = decline_year(years_passed)

    rendered_page = template.render(
        years=years_passed,
        years_text=years_text,
        wine_sorts=wine_sorts,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()

import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape

from year_declension import decline_year
from wine_aggregator import get_wine_dict

wine_sorts = get_wine_dict()

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml']),
)
first_year = new_year = datetime.datetime(year=1920, month=1, day=1, hour=0)

template = env.get_template('template.html')

years = int((datetime.datetime.today() - first_year).days // 365.25)
years_text = decline_year(years)

rendered_page = template.render(
    years=years,
    years_text=years_text,
    wine_sorts=wine_sorts,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

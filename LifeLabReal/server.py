from flask import Flask, render_template, request
import json

app = Flask(__name__, static_url_path='', static_folder='static')

with open("data/life_expectancy.json") as f:
    life_data = json.load(f)

@app.route('/')
def index():
    usa_endpoints = []
    canada_endpoints = []
    mexico_endpoints = []
    avg_endpoints = []

    years = sorted([int(y) for y in life_data["USA"].keys()])

    for i in range(len(years) - 1):
        y1 = str(years[i])
        y2 = str(years[i + 1])

        usa_y1 = float(life_data["USA"][y1])
        usa_y2 = float(life_data["USA"][y2])
        canada_y1 = float(life_data["Canada"][y1])
        canada_y2 = float(life_data["Canada"][y2])
        mexico_y1 = float(life_data["Mexico"][y1])
        mexico_y2 = float(life_data["Mexico"][y2])

        usa_endpoints.append([usa_y1, usa_y2])
        canada_endpoints.append([canada_y1, canada_y2])
        mexico_endpoints.append([mexico_y1, mexico_y2])
        avg_endpoints.append([
            (usa_y1 + canada_y1 + mexico_y1) / 3,
            (usa_y2 + canada_y2 + mexico_y2) / 3
        ])

    return render_template("index.html",
        usa_endpoints=usa_endpoints,
        canada_endpoints=canada_endpoints,
        mexico_endpoints=mexico_endpoints,
        avg_endpoints=avg_endpoints,
        years=years
    )

@app.route('/year')
def year():
    year = request.args.get("year")
    try:
        usa_value = float(life_data["USA"][year])
        canada_value = float(life_data["Canada"][year])
        mexico_value = float(life_data["Mexico"][year])
    except (KeyError, TypeError):
        return f"No data available for year {year}", 400

    return render_template("year.html",
        year=year,
        usa_value=usa_value,
        canada_value=canada_value,
        mexico_value=mexico_value
    )

if __name__ == "__main__":
    app.run(debug=True)

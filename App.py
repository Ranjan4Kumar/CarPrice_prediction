from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)
car = pd.read_csv('Cleaned car.csv')


# we will create entry point of our application
@app.route('/')
# Thus index function will be called if someone hits on our "route"
def index():
    # we will write all those things here which we need as output in our card
    companies = sorted(car['company'].unique())

    car_model = sorted(car['name'].unique())

    year = sorted(car['year'].unique(), reverse=True)

    fuel_type = car['fuel_type'].unique()

    return render_template('index.html', companies=companies, car_models=car_model, years=year, fuel_types=fuel_type)


if __name__ == "__main__":
    app.run(debug=True)

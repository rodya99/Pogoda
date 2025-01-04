from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Замените на ваш API-ключ OpenWeatherMap
API_KEY = "e0183218a4f361a25d738f3dc6ccb6d0"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    city = ""

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            # URL для API OpenWeatherMap
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru"
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
            else:
                weather_data = {"error": f"Город '{city}' не найден!"}

    return render_template("index.html", weather=weather_data, city=city)

if __name__ == "__main__":
    app.run(debug=True)
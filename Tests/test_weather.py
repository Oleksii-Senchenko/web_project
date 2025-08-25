import requests

API_KEY = "c93b08d71e91ab78bd1de90113052ef2"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "ua"
    }

    resp = requests.get(BASE_URL, params=params)
    resp.raise_for_status()
    return resp.json()


def test_get_weather():
    data = get_weather("Prague")

    assert "main" in data
    assert "temp" in data["main"]
    assert "weather" in data
    assert data["name"].lower() == "prague"


if __name__ == "__main__":
    test_get_weather()
    print("Тест API погоди пройдено успішно!")
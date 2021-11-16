import http.client

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=[INSERT APP ID]'

def cityWeather(city):
    conn = http.client.HTTPSConnection("open-weather13.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "[INSERT HOST]",
        'x-rapidapi-key': "[INSERT KEY]"
        }

    conn.request("GET", "/city/"+city, headers=headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")
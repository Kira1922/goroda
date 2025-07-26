from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            lat = round(results[0]['geometry']['lat'], 2)
            lng = round(results[0]['geometry']['lng'], 2)
            return f"Широта: {lat}, Долгота: {lng}"
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"


key = '7aa3e03722094e7ba4e560632d9facc6'
city = 'Химки'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")

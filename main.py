from opencage.geocoder import OpenCageGeocode

def get_coordinates(city, key):
    try:
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(city, language='ru')
        if results:
            return results[0]['geometry']['lat'], results[0]['geometry']['lng']
        else:
            return "Город не найден"
    except Exception as e:
        return f"Общая ошибка: {e}"


key = '7aa3e03722094e7ba4e560632d9facc6'
city = 'Москва'
coordinates = get_coordinates(city, key)
print(f"Координаты города {city}: {coordinates}")

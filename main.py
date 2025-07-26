from opencage.geocoder import OpenCageGeocode
from tkinter import *

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

def show_coordinates(event=None):
    city = entry.get()
    coordinates = get_coordinates(city, key)
    label.config(text=f"Координаты города {city}: {coordinates}")



key = '7aa3e03722094e7ba4e560632d9facc6'


window = Tk()
window.title("Поиск координат города")
window.geometry("200x100")

entry = Entry()
entry.pack()
entry.bind("<Return>", show_coordinates)

button = Button(text="Поиск", command=show_coordinates)
button.pack()

label = Label(text="Введите город и нажмите Поиск")
label.pack()

window.mainloop()

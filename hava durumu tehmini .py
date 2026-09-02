from tkinter import*
from PIL import ImageTk, Image
import requests 

URL = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = '808b435f4ccb23761037563bec8f80c3'
iconURL =  'https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q': city, 'appid': api_key, 'Lang': 'en'}
    data = requests.get(URL, params=params).json()
    if data:
        city = data ['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return(city, country, temp, icon, condition)

def main():
        city = cityEntry.get()
        weather = getWeather(city)
        if weather:
            locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
            tempLabel['text'] = '{}''C'.format(weather[2])
            conditionLabel['text'] = weather[4]
            icon = ImageTk.PhotoImage(Image.open(requests.get(iconURL.format(weather[3]), stream = True).raw))
            iconLabel.configure(image=icon)
            iconLabel.image = icon
            print(weather)

app = Tk()
app.geometry('301x449')
app.title('sky Forecast')

cityEntry = Entry(app,justify='center')
cityEntry.pack(fill=BOTH,ipady=10,padx=17,pady=4)
cityEntry.focus()

SearchButton = Button(app, text='Search',font=('Arial',14),command=main)
SearchButton.pack(fill=BOTH,ipady=10,padx=20)

iconLabel = Label(app)
iconLabel.pack()

locationLabel = Label(app,font=('arial',40))
locationLabel.pack()

tempLabel = Label(app,font=('arial',50, 'bold'))
tempLabel.pack()

conditionLabel = Label(app,font=('arial', 20))
conditionLabel.pack()

app.mainloop()
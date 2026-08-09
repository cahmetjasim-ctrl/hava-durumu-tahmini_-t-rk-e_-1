from tkinter import*
from PIL import ImageTk,Image
import requests

URL = 'https://api.openweathermap.org/data/2.5/weather?'
api_key = '808b435f4ccb23761037563bec8f80c3'
iconURL = 'https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    params = {'q': city, 'appid': api_key, 'lang': 'tr'} 
    data = requests.get(URL,params=params).json()
    if data:
        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return(city,country,temp,icon,condition)
    
def main():
        city = cityEntry.get()
        weather = getWeather(city)
        if weather:
            locationLabel['text'] = '{},{}'.format(weather[0], weather[1])
            tempLabel['text'] = '{}''C'.format(weather[2])
            conditionLabel['text'] = weather[4]
            icon = ImageTk.PhotoImage(Image.open(requests.get(iconURL.format(weather[3]), stream=True).raw))
            iconLabel.configure(image=icon)
            iconLabel.image = icon

                
app = Tk() #ana pencereyi oluşturur
app.geometry('300x450') # boyutu ayrlar pencere booyutu ama 
app.title('hava durum tahmini sistemi') #pencre başlığı oluşturur

cityEntry=Entry(app,justify='center') # yazının nerde ve ortada yazılcağını söyler ortalamak içinde center kullanırız
cityEntry.pack(fill=BOTH,ipady=10,padx=15,pady=6) # bu kutunun genişlemesineyarıyor bunu yapan fill=BOTH tur 
cityEntry.focus()# buda yazıya odaklannır yani imşeç kutuya odaklanıır 

searchButton = Button(app,text='Arama',font=('Arial',14),command=main) # buton oluşturur ve butona basıldığında buton ve main fonksiyonu çalışır
searchButton.pack(fill=BOTH,ipady=10,padx=20)#buton boyutunu ayarlar ve butonun boyutu penecere boyutuna göre ayarlanır

iconLabel = Label(app) #icon Label oluşturur ve iconLabel.pack() ile pencereye ekler
iconLabel.pack()

locationLabel = Label(app,font=('arial',40)) # şehir ve ülke isimleriniin yazılacağı40 punto ile gösterilceği yer dir 
locationLabel.pack() # sadece varsayılan pencereye ekleniyor 

tempLabel=Label(app,font=('arial',50,'bold')) # Label => tkintırda yazı/metin göstermey yarayan bir widgettir.app => bu etiketin hangi pencereye ait olduğunu belirtiyor  font=> ('ariala',50,'bold') yazıyı parametre yle ayrlıyor 
tempLabel.pack() # sadece pencereye ekleniyor oda varsayılan  pencere yani Tkintıırıın varsayılan yerleşimini kullanıyor 

conditionLabel = Label(app,font=('arial',20)) # ayn mantık ama daha küçük 20 punto ile hava dururmunun yazılacaüı yeri gösteriyor 
conditionLabel.pack()# buda pencereye ekleniyor

app.mainloop()# uygulamayı çalıştırır.

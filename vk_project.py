import speech_recognition as sp # библиотека для работы со звуком и его обработка
import re # библиотека для работы с паттернами
import vk_api # библиотека для работы с вк
import os
def obrabotka_text(): #создаю функцию, так писать это несколько раз очень плохо
    sett=sp.Recognizer() # создаю объект, которые будет настраивать звук
    with sp.Microphone() as f:  # связываю переменную f с микрофоном
        print("Нажмите enter") # для красоты
        input() # тоже
        print("Говорите ") #тоже
        sett.pause_threshold=1 # пауза при записи
        resoult=sett.listen(f) # тут происходит чтение звука
    text=sett.recognize_google(resoult,language="ru-RU") # преобразование в текствый вид
    text_new=re.split(r" ",text) # сплит текст, где есть пробелы
    s="" #пустая переменная
    for i in text_new: #цикл, который 
        s+=i
    s.lower()
    return s
def request_text():
    ob=sp.Recognizer()
    with sp.Microphone() as f2:
        input("Нажмите enter")
        ob.pause_threshold=1
        tex=ob.listen(f2)
    texx=ob.recognize_google(tex,language="ru-RU")
    zq=re.split(r" ",texx)
    texxx=""
    for k in zq:
        texxx+=k
    return texxx
login=input("Введите логин: ")
password=input("Введите пароль: ")
session=vk_api.VkApi(login,password)
session.auth()
metot=session.get_api()
q=vk_api.VkUpload(session)

x=2
while x>1:
    ss=obrabotka_text()
    if (ss =="вбан" or ss=="заблокирвать" or ss=="бан"):
        ownerid=request_text()
        metot.account.ban(owner_id=ownerid)
    elif ss in "списокзаблокированных":
        print(metot.account.getBanned(count=200))
    elif ss in "информация моиданные":
        spic="friends,groups,messages,notifications,sdk,events,gifts,videos"
        spic2="country,https_required,own_posts_default,no_wall_replies,intro,lang"
        print(metot.getCounters(filter=spic))
        print(metot.account.getInfo(fields=spic2))
        print(metot.account.getProfileInfo())
    elif ss in "поменятьфотопрофиля" or ss in "поменятьфотосвое":
        print(os.listdir())
        poto=input("Введите название фото : ")
        q.photo_profile(photo=poto)
        
        
        
 
    

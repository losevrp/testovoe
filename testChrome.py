import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from time import sleep

managerLogin = "manager@mail.ru"
managerPassword = "1"
newUserLogin = "Ivan444"
newUserEmail = "Ivan444@mail.ru"
newUserPassword = "Qwerty123"
newUserAvatar = "G:\Avatar.png" #выбрать файл
newUserData = "08091990" #наверное дата рождения
newUserSex = "Мужской" #Выбрать из выпадающего списка
newUserStartWorkDate = "04072015" #дата начала работы
newUserHobby = "Программирование"
newUserName1 = "Иван"
newUserFamilia1 = "Иванов"
newUserOtchestvo1 = "Иванович"
newUserCat = "Пушок"
newUserDog = "Шарик"
newUserParrot = "Папуг"
newUserSeapig = "Булка"
newUserHamster = "Булочка"
newUserSquerl = "Орешек"
newUserNumber = "20074101"
newUserAdress = "Москва ул Ленина 1"
newUserINN = "123456789"

def fildInsert (path, text):
    elem = driver.find_element(By.XPATH, path)
    elem.send_keys(text)
    #sleep(2)

def LogIn (login, password):
    WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[2]/a')).click()
    fildInsert('/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[1]/td[2]/input', login)
    fildInsert('/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[2]/td[2]/input', password)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/form/table/tbody/tr[3]/td[2]/input').click()

def dataCompare (sitePathData, inputedData):
    elemTaken = driver.find_element(By.XPATH, sitePathData).text
    if elemTaken == inputedData:
        print('Введенные ранее данные ' + inputedData + ' совпадают с полученными с сайта ' + elemTaken)
    else:
        print('Введенные ранее данные ' + inputedData + ' не совпадают с полученными с сайта ' + elemTaken)

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.get("http://users.bugred.ru")

#Логин за менеджера
LogIn(managerLogin, managerPassword)

#Нажать кнопку добавить пользователя
WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/p[1]/a')).click()

#Заполняем поля нового пользователя
fildInsert('/html/body/div[3]/form/table/tbody/tr[1]/td[2]/input', newUserLogin)
fildInsert('/html/body/div[3]/form/table/tbody/tr[2]/td[2]/input', newUserEmail)
fildInsert('/html/body/div[3]/form/table/tbody/tr[3]/td[2]/input', newUserPassword)

#Выбираем файл для аватара
avatar = os.path.abspath(newUserAvatar)
file_input = driver.find_element(By.XPATH, "/html/body/div[3]/form/table/tbody/tr[4]/td[2]/input")
file_input.send_keys(avatar)

fildInsert('/html/body/div[3]/form/table/tbody/tr[5]/td[2]/input', newUserData)
fildInsert('/html/body/div[3]/form/table/tbody/tr[6]/td[2]/select', newUserSex)
fildInsert('/html/body/div[3]/form/table/tbody/tr[7]/td[2]/input', newUserStartWorkDate)
fildInsert('/html/body/div[3]/form/table/tbody/tr[8]/td[2]/textarea', newUserHobby)
fildInsert('/html/body/div[3]/form/table/tbody/tr[9]/td[2]/input', newUserName1)
fildInsert('/html/body/div[3]/form/table/tbody/tr[10]/td[2]/input', newUserFamilia1)
fildInsert('/html/body/div[3]/form/table/tbody/tr[11]/td[2]/input', newUserOtchestvo1)
fildInsert('/html/body/div[3]/form/table/tbody/tr[12]/td[2]/input', newUserCat)
fildInsert('/html/body/div[3]/form/table/tbody/tr[13]/td[2]/input', newUserDog)
fildInsert('/html/body/div[3]/form/table/tbody/tr[14]/td[2]/input', newUserParrot)
fildInsert('/html/body/div[3]/form/table/tbody/tr[15]/td[2]/input', newUserSeapig)
fildInsert('/html/body/div[3]/form/table/tbody/tr[16]/td[2]/input', newUserHamster)
fildInsert('/html/body/div[3]/form/table/tbody/tr[17]/td[2]/input', newUserSquerl)
fildInsert('/html/body/div[3]/form/table/tbody/tr[18]/td[2]/input', newUserNumber)
fildInsert('/html/body/div[3]/form/table/tbody/tr[19]/td[2]/input', newUserAdress)
fildInsert('/html/body/div[3]/form/table/tbody/tr[20]/td[2]/input', newUserINN)

driver.find_element(By.XPATH, '/html/body/div[3]/form/table/tbody/tr[21]/td[2]/input').click()

#Выйти из текущего пользователя
driver.find_element(By.XPATH, '//*[@id="fat-menu"]/a').click()
WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '//*[@id="fat-menu"]/ul/li[3]/a')).click()

#Логин за нового пользователя
LogIn(newUserEmail, newUserPassword)

#Поиск пользователя по mail
fildInsert('/html/body/div[3]/form/table/tbody/tr[4]/td/input', newUserEmail)
driver.find_element(By.XPATH, '/html/body/div[3]/form/table/tbody/tr[5]/td[1]/button').click()

#Посмотреть данные пользователя
WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '/html/body/div[3]/table/tbody/tr/td[7]/a')).click()

#Сравнить данные
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[1]/td[2]', newUserEmail)
#Про
FIO = (newUserFamilia1 + ' ' + newUserName1 + ' ' + newUserOtchestvo1) #формируем строку для проверки данных поля ФИО
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[2]/td[2]', FIO)

#Текст из выпадающего списка пол
selectedText = Select(driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[3]/td[2]/select'))
elemSex = selectedText.first_selected_option.text
if elemSex == newUserSex:
    print('Введенные ранее данные ' + newUserSex + ' совпадают с полученными с сайта ' + elemSex)
else:
    print('Введенные ранее данные ' + newUserSex + ' не совпадают с полученными с сайта ' + elemSex)

dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[4]/td[2]', newUserData)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[5]/td[2]', newUserStartWorkDate)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[6]/td[2]/textarea', newUserHobby)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[7]/td[2]', newUserName1)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[8]/td[2]', newUserFamilia1)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[9]/td[2]', newUserOtchestvo1)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[10]/td[2]', newUserCat)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[11]/td[2]', newUserDog)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[12]/td[2]', newUserParrot)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[13]/td[2]', newUserSeapig)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[14]/td[2]', newUserHamster)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[15]/td[2]', newUserSquerl)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[16]/td[2]', newUserNumber)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[17]/td[2]', newUserAdress)
dataCompare('/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[18]/td[2]', newUserINN)

#Выйти из текущего пользователя
driver.find_element(By.XPATH, '//*[@id="fat-menu"]/a').click()
WebDriverWait(driver, 5).until(lambda x: x.find_element(By.XPATH, '//*[@id="fat-menu"]/ul/li[3]/a')).click()

#Логин за менеджера
LogIn(managerLogin, managerPassword)

#Поиск пользователя по mail
fildInsert('/html/body/div[3]/form/table/tbody/tr[4]/td/input', newUserEmail)
driver.find_element(By.XPATH, '/html/body/div[3]/form/table/tbody/tr[5]/td[1]/button').click()

#Удалить пользователя
driver.find_element(By.XPATH, '/html/body/div[3]/table/tbody/tr/td[6]/a').click()

sleep(5)

driver.quit()
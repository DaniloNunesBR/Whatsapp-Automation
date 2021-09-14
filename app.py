from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pathlib
from selenium.webdriver.common.keys import Keys

scriptDirectory = pathlib.Path().absolute()

options = Options()
#options.add_argument("--headless")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36')
options.add_argument(f"user-data-dir={scriptDirectory}\\profiledata")

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get('https://web.whatsapp.com/')
time.sleep(5)

try:
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div[1]/div/div[2]/div')
    driver.save_screenshot('scan.png')
    input('Scan Code e Press Enter: ')
    time.sleep(10)
    driver.save_screenshot('logged.png')
    print('Logged')
except:
    time.sleep(5)
    driver.save_screenshot('logged.png')
    print('Logged')

def send_message(user,message=0,picture=0,document=0):
    search_people = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
    search_people.click()
    search_people.send_keys(user)
    search_people.send_keys(Keys.RETURN)

    if message:
        message_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[1]/div/div[2]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)

    if picture:
        clip = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
        clip.click()
        message_picture = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[1]/button/input')
        message_picture.send_keys(picture)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div').click()

    if document:
        clip = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div')
        clip.click()
        msg_doc = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button/input')
        msg_doc.send_keys(document)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div/div').click()      

#send_message('Pessoa','Mensagem Final :)')

def chatbot_run():
    quests = [
    ['ola','olá','oi','bom dia','oie','oii'],
    ['sim','gostaria','quero','ok'],
    ['custa','custo','preço','preços','preco','precos','valor','valores','custos'],
    ['entrega','receber','quantos dias'],
    ['como','onde','tenho','interesse','compro','comprar'],
    ['obrigado','certo','beleza']
    ]

    aswers = [
    ['Olá, como vai? Gostaria de saber dos nossos produtos ?'],
    ['Nós temos um robô inovador, que vai automatizar completamente o seu whatsapp'],
    ['Este produto custa uma quantia de 1000 Reais'],
    ['A entrega pode ser feita online imediatamente via Skype, tem interesse em adquirir?'],
    ['Basta acessar o nosso site na bio e solicitar o orçamento'],
    ['Estamos a disposição! Abraço :)']
    ]

    while True:
        try:
            new_message = driver.find_elements_by_class_name('_23LrM')
            new_message[-1].click()

            messages = driver.find_elements_by_class_name('_1Gy50')
            last_message = messages[-1].text

            send = False
            last_message = last_message.lower().replace(',','').replace('.','').replace('?','').split()
            for i in range(len(quests)):
                for j in last_message:
                    if j in quests[i]:
                        
                        aswer = aswers[i][0]
                        try:
                            aswer += '\n' + 'Resp: '
                            for k in quests[i+1]:
                                aswer += '*' + k.capitalize() + '*' + ' '
                        except:
                            aswer = aswers[i][0]

                        name_user = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]/div/div/span').text
                        send_message(name_user,aswer)
                        
                        send = True
                        break
                if send:
                    break

            espera_group = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]')
            espera_group.click()
            espera_group.send_keys('Espera')
            espera_group.send_keys(Keys.RETURN)
        except:
            False
        time.sleep(1)

#chatbot_run()
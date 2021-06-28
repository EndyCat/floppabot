import vk_api, traceback, string, random, threading, time
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from pyowm import OWM
from pyowm.utils.config import get_default_config
vk_session = vk_api.VkApi(token = 'a12d7fc9090368b1df8d71078f29dbea1ec4a5b1960008037cae1101ad48e0d59531578092b18886333a1')
vk = vk_session.get_api()
vku_session = vk_api.VkApi(token = 'bfa652b1df4a1eb3b2315dbe9ef04eab653bae315215ea9a1c9cee6512162e173672931f640ec908d35a0')
vku = vku_session.get_api()
longpoll = VkBotLongPoll(vk_session, 204401689)

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('7d06866815dc03f33c839a93c9d16e98')
mgr = owm.weather_manager()

def sender(uid, text, keyboard=None):
    post = {
        "user_id": uid,
        "message": text,
        "random_id": 0
    }
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()

    vk_session.method("messages.send", post)
    #vk_session.method('messages.send', {'user_id' : uid, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})
def foto(uid, text):
    vk_session.method('messages.send', {'user_id' : uid, 'attachment' : text, 'random_id' : 0})
def chat_sender(id, text, keyboard=None):
    post = {
        "chat_id": id,
        "message": text,
        "random_id": 0
    }
    if keyboard != None:
        post["keyboard"] = keyboard.get_keyboard()

    vk_session.method("messages.send", post)
    #vk_session.method('messages.send', {'chat_id' : id, 'message' : text, 'random_id' : 0})
def chat_foto(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'attachment' : text, 'random_id' : 0})
def chat_stick(id, text):
    vk_session.method('messages.send', {'chat_id' : id, 'sticker_id' : text, 'random_id' : 0})

from PIL import Image, ImageDraw, ImageFont
import requests, pyttsx3
import sys
import textwrap

def draw_multiple_line_text(image, text, font, text_color, text_start_height):
    '''
    From unutbu on [python PIL draw multiline text on image](https://stackoverflow.com/a/7698300/395857)
    '''
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size
    y_text = text_start_height
    lines = textwrap.wrap(text, width=16)
    for line in lines:
        line_width, line_height = font.getsize(line)
        draw.text(((image_width - line_width) / 2, y_text),
                  line, font=font, fill=text_color)
        y_text += line_height

def sign(text):
    try:
        signa = Image.open('floppa.png')
    except:
        print("Unable to load image")
        sys.exit(1)

    idraw = ImageDraw.Draw(signa)
    text_color = (0, 0, 0)
    font = ImageFont.truetype("Lobster.ttf", size=100)
    text_start_height = 560
    #idraw.text((340, 580), text, font=font, fill=(0,0,0,0))
    draw_multiple_line_text(signa, text, font, text_color, text_start_height)

    signa.save('sign.png')
    try:
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_messages('sign.png')
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        if event.from_chat:
            chat_foto(id, attachment)
        else:
            foto(uid, attachment)
    except:
        if event.from_chat:
            chat_sender(id, 'ЧТо то пошло не так, выдаёте администратора!')
        else:
            sender(uid, 'ЧТо то пошло не так, выдаёте администратор')
def think(text):
    try:
        thinke = Image.open('floppaa.png')
    except:
        print("Unable to load image")
        sys.exit(1)
    font = ImageFont.truetype("Lobster.ttf", size=100)
    idraw = ImageDraw.Draw(thinke)
    if len(text) <= 12:
        idraw.text((300, 550), text, font=font, fill=(0,0,0,0))
    else:
        idraw.multiline_text((300, 520), f'{text[:12]}\n {text[13:]}', font=font, fill=(0,0,0,0))



    thinke.save("thinky.png")



    try:
        upload = vk_api.VkUpload(vk)
        photo = upload.photo_messages('thinky.png')
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        if event.from_chat:
            chat_foto(id, attachment)
        else:
            foto(uid, attachment)
    except:
        if event.from_chat:
            chat_sender(id, 'ЧТо то пошло не так, выдаёте администратора!')
        else:
            sender(uid, 'ЧТо то пошло не так, выдаёте администратор')


#def spech(text):
    #engine = pyttsx3.init()
    #ru_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\TokenEnums\RHVoice\Spomenka+Aleksandr"
    #engine.setProperty('voice', ru_voice_id)
    #engine.save_to_file(text, 'test.ogg')
    #engine.runAndWait()


    #doc_link = vku.docs.getWallUploadServer(group_id=204401689)
    #print(doc_link)
    #print(vku.docs.save(file=doc_link,title='audio'))
    #upload = vk_api.VkUpload(vku)
    #audio = upload.audio_message('test.ogg')
    #audio = audio['audio_message']
    #print(audio)
    #owner_id = audio['owner_id']
    #audio_id = audio['id']
    #access_key = audio['access_key']
    #link = audio['link_mp3']
    #audio_key = VkKeyboard(one_time=False, inline=True)
    #audio_key.add_openlink_button('Аудио', link)
    #print(link)
    #attachment = f'doc{owner_id}_{audio_id}_{access_key}'
    #if event.from_chat:
        #chat_sender(id, 'Держи аудио! Ты также можешь скачать его.', audio_key)
        #chat_sender(id, 'Держи ссылку на скачивания этого аудио! \n ' + link)
    #else:
        #sender(uid, 'Держи аудио! Ты также можешь скачать его.', audio_key)
        #hat_sender(uid, 'Держи ссылку на скачивания этого аудио! \n ' + link)


a_replic = ['я Шлёпа - Русский кот!', 'выпьем за любовь!', 'будешь несквик?']
b_replic = ['Хай', 'Привет', 'Здарова']
c_replic = ['Я всего лишь иметация шлёпы... Мне не дано понимать некотыре слова...', 'Ладно', 'Допустим']
d_replic = []

def thread_function():
    while True:
        try:
            vk.messages.setActivity(group_id=204401689,type='typing',peer_id=2000000000 + 2)
            time.sleep(150)
        except:
            pass
if __name__ == "__main__":
    x1 = threading.Thread(target=thread_function, args=())
    x1.start()

while True:
    longpoll = VkBotLongPoll(vk_session, 204401689)
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                msg = event.object.message['text'].lower()
                msg_len = len(msg)
                id = event.chat_id
                uid = event.object.message['from_id']
                #user_get = vk.users.get(user_ids = (uid))
                #user_get = user_get[0]
                #first_name = user_get['first_name']
                #last_name = user_get['last_name']
                #full_name = first_name+" "+last_name

                try:
                    user_get = vk.users.get(user_ids = (uid))
                    user_get = user_get[0]
                    first_name = user_get['first_name']
                    last_name = user_get['last_name']
                    full_name = first_name+" "+last_name

                    kid = event.obj.message["reply_message"]["from_id"]

                    re_user_get = vk.users.get(user_ids = (kid), name_case='gen')
                    re_user_get = re_user_get[0]
                    re_first_name = re_user_get['first_name']
                    re_last_name = re_user_get['last_name']
                    re_full_name = re_first_name+" "+re_last_name
                except:
                    pass
                msg_t = event.object.message['conversation_message_id']
                #url = event.object.message['attachments'][0]['photo']['sizes'][-1]['url']
                start_key = VkKeyboard(one_time=False, inline=True)
                eventik = 'none'
                eventok = 'none'
                try:
                    eventik = event.object.message['action']['type']
                    eventok = event.object.message['action']['member_id']
                except:
                    pass
                try:
                    if event.from_chat:
                        if msg in ['привет', 'хай', 'здарова']:
                            chat_sender(id, random.choice(b_replic) + ', ' + random.choice(a_replic))
                        elif msg[:6] == '/сигна':
                            if msg_len <= 40:
                                sign(msg[7:])
                            else:
                                chat_sender(id, 'Фраза должна быть не длинее 40 символов!')
                        elif 'шлёпа' in msg:
                            chat_sender(id, 'Что то хотел?')
                        elif msg[:7] == '/цитата':
                            if msg_len <= 40:
                                think(msg[8:])
                            else:
                                chat_sender(id, 'Фраза должна быть не длинее 40 символов!')
                        elif msg in ['начать', '/start', 'команды']:
                            start_key.add_openlink_button('Команды', 'https://vk.com/@cultoffloppa-komandy-bota')
                            chat_sender(id, 'Нажми на кнопку!', start_key)
                        elif msg[:6] == '/скажи':
                            chat_sender(id, 'Времнено не работает!')
                            #spech(msg[7:])

                        elif eventik == 'chat_invite_user' and eventok == -204401689:
                            chat_sender(id, 'Всем здарова! Шлёпа в здании. \nГотовы повесилиться? Тогда скорее пишите \"/start\", а также не забдьте выдать доступ к переписке!')


                        elif 'обнять' == msg:
                            try:
                                chat_sender(id, f'🤗 - @id{uid}({full_name}) обнял @id{kid}({re_full_name})')
                            except:
                                chat_sender(id, 'Чувак ты пытаешься обнять воздух... ОТветь на чьё то сообщение.')
                        elif 'ударить' == msg:
                            try:
                                chat_sender(id, f'👊 - @id{uid}({full_name}) побил @id{kid}({re_full_name})')
                            except:
                                chat_sender(id, 'Чувак ты пытаешься ударить воздух... ОТветь на чьё то сообщение.')
                        elif msg[:7] == '/погода':
                            gorod = msg[8:]
                            try:
                                observation = mgr.weather_at_place(gorod)
                                w = observation.weather
                                rain = w.detailed_status
                                temp = w.temperature('celsius')['temp']
                                chat_sender(id, f'В городе {gorod}, {temp}°, {rain}')
                            except:
                                chat_sender(id, 'Указан не вернный город!')
                        elif msg == 'кик':
                            peer_id = 2000000000 + id
                            members = vk.messages.getConversationMembers(peer_id=peer_id)


                            for i in members["items"]:
                                if i["member_id"] == uid:
                                    admin = i.get('is_admin', False)
                                    if admin == True:
                                        try:
                                            chat_sender(id, f'Попытался удалить @id{kid}({re_full_name}) \n Напиши @id{uid}(администратору) чтобы вернутся!! ')
                                            vk.messages.removeChatUser(chat_id=id, member_id=kid)
                                        except:
                                            chat_sender(id, f'Не удалось удалить @id{kid}({re_full_name})')
                                    else:
                                        chat_sender(id, 'Ты не админ.')
                    else:
                        if msg in ['привет', 'хай', 'здарова', 'здравствуй']:
                            sender(uid, random.choice(b_replic) + ', ' + random.choice(a_replic))
                        elif msg[:6] == '/сигна':
                            if msg_len <= 40:
                                sig = threading.Thread(target=sign, args=[msg[7:]])
                                sig.start()
                            else:
                                sender(uid, 'Фраза должна быть не длинее 40 символов!')
                        elif msg[:6] == '/скажи':
                            #if msg_len <= 40:
                            #spech(msg[7:])
                            sender(uid, 'Времнено не работает!')
                            #else:
                                #sender(uid, 'Фраза должна быть не длинее 40 символов!')
                        elif msg[:7] == '/цитата':
                            if msg_len <= 40:
                                think(msg[8:])
                            else:
                                sender(uid, 'Фраза должна быть не длинее 40 символов!')
                        elif msg in ['начать', '/start', 'команды']:
                            start_key.add_openlink_button('Команды', 'https://vk.com/@cultoffloppa-komandy-bota')
                            sender(uid, 'Нажми на кнопку!', start_key)
                        elif 'шлёпа' in msg:
                            sender(uid, 'Что то хотел?')
                        elif msg[:7] == '/погода':
                            gorod = msg[8:]
                            try:
                                observation = mgr.weather_at_place(gorod)
                                w = observation.weather
                                rain = w.detailed_status
                                temp = w.temperature('celsius')['temp']
                                sender(uid, f'В городе {gorod}, {temp}°, {rain}')
                            except:
                                sender(uid, 'Указан не вернный город!')
                        else:
                            sender(uid, random.choice(c_replic))
                except:
                    try:
                        sender(484810309, traceback.format_exc())
                    except:
                        print(traceback.format_exc())

    except:
        longpoll = VkBotLongPoll(vk_session, 204401689)



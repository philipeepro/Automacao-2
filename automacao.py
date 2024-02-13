#Para realizar a autoomação, é necessário isntalar a linguagem Python em
#uma versão compatível com a versão do Windows que você utiliza, e instalar
#no prompt de comando o pyautogui

import pyautogui as pa
import time
import pyperclip
pa.PAUSE = 1


pa.press('win')
pa.press('chrome')

#Sempre que necessário solicitar escrita na automação, escrever entre aspas duplas

pa.write("youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.click(x=890, y=402)
pyperclip.copy("Audioslave")
pa.hotkey('ctrl', 'v')
pa.press('ENTER')

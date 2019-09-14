import pyautogui
import time
from datetime import datetime
print("Ta funcionando")
while (1):
    hora = int(datetime.now().strftime('%H'))
    #print(hora)
    minuto = int(datetime.now().strftime('%M'))
    #print(minuto)
    segundo = int(datetime.now().strftime('%S'))
    #print(segundo)
    
    if hora == 21 and minuto == 0 and segundo == 0:
        print('Iniciando Gravaçao!!')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('r')
        pyautogui.keyUp('r')
        pyautogui.keyUp('ctrl')
        time.sleep(1)
        
    if hora == 0 and minuto == 0 and segundo == 0:
        print('Finalizando Gravaçao!!')
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('r')
        pyautogui.keyUp('r')
        pyautogui.keyUp('ctrl')
        break
    #time.sleep(1)
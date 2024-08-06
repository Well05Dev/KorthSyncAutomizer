import pyautogui as p #automatização
import time as t #delays
import datetime #data e hora
from tkinter import * #pegar resoluções

#ATENÇÃO!
#ESTE SCRIPT SÓ TERÁ O CORRETO FUNCIONAMENTO SE O KORTH JÁ ESTIVER ABERTO.
#CASO O CONTRÁRIO, NÃO FUNCIONARÁ.

# Obtém a data e hora atual
dateTime = datetime.datetime.now()

# Separa a data e a hora em variáveis diferentes
data_atual = dateTime.date()
hora_atual = dateTime.time().replace(microsecond=0)  # Remove os milissegundos

#recebe a resolução da tela
root = Tk()
monitor_width = root.winfo_screenwidth()
monitor_height = root.winfo_screenheight()

#checa as resoluções recebidas. se houver erro de resolução, registra nos logs.
if ((monitor_width == 1366) and (monitor_height == 768)):
    monitor = 1
elif ((monitor_width == 1440) and (monitor_height == 900)):
    monitor = 2
else:
    file_path = "LogsSyncKorth.txt"
    # Abre o arquivo no modo de escrita (append)
    with open(file_path, 'a') as file:
        file.write(f"-------")
        file.write(f"ERRO NA TENTATIVA DE SINCRONIZAÇÃO AUTOMÁTICA POR ERRO DE RESOLUÇÃO. {data_atual}, as {hora_atual}.")
        file.write(f"-------\n\n")

def regLogs():
    file_path = "LogsSyncKorth.txt"
    # Abre o arquivo no modo de escrita (append)
    with open(file_path, 'a') as file:
        file.write(f"-------")
        file.write(f"Korth sincronizado automaticamente via Python. {data_atual}, as {hora_atual}. Resolução: {monitor_width} x {monitor_height}.")
        file.write(f"-------\n\n")


def attKorth():
    if monitor == 1:    
        p.moveTo(1364, 745) #move ao botao da workspace
        p.leftClick()
        t.sleep(.1)
        
        p.moveTo(167, 749) #Move o mouse ao ícone do korth
        p.leftClick() #Clica uma vez
        t.sleep(.5)
        
        p.leftClick() #clica duas vezes no icone
        t.sleep(.15)
        p.leftClick()
        t.sleep(.5)
        
        p.moveTo(817, 454) #move para a posiçao padrao do "ok" do possivel pop-up
        p.leftClick()
        t.sleep(.5)
        
        p.moveTo(1351, 8) #fecha o korth pelo botao do canto superior direito
        p.leftClick()
        t.sleep(2)
        
        p.moveTo(167, 749) #Move o mouse ao ícone do korth
        p.leftClick() #Inicia o korth
        t.sleep(5)

        p.moveTo(54,660) #Move mouse ao botão sincronizador
        p.doubleClick() #Clica duas vezes
        
    elif monitor == 2:
        p.moveTo(1439, 880) #move ao botao da workspace
        p.leftClick()
        t.sleep(.1)
        
        p.moveTo(170, 876) #Move o mouse ao ícone do korth
        p.leftClick() #Clica uma vez
        t.sleep(.5)
        
        p.leftClick() #clica duas vezes no icone
        t.sleep(.15)
        p.leftClick()
        t.sleep(.5)
        
        p.moveTo(860, 481) #move para a posiçao padrao do "ok" do possivel pop-up
        p.leftClick()
        t.sleep(.5)
        
        p.moveTo(1428, 8) #fecha o korth pelo botao do canto superior direito
        p.leftClick()
        t.sleep(2)
        
        p.moveTo(170, 876) #Move o mouse ao ícone do korth
        p.leftClick() #Inicia o korth
        t.sleep(5)

        p.moveTo(53,796) #Move mouse ao botão sincronizador
        p.doubleClick() #Clica duas vezes
        
    try:
        regLogs()
        print("Korth Sincronizado com sucesso!")
    except:
        print(f"Ocorreu um erro no registro de logs {data_atual}, as {hora_atual} ")

attKorth()
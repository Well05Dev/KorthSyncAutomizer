import pyautogui as p
#   
#Script usado para captar a posição do cursor.
#Imprime os valores via terminal.

x, y = p.position()

print("X =",x)
print("Y =", y)
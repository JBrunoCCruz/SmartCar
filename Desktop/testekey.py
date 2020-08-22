# Biblioteca para leitura das teclas do teclado
import keyboard

print('aqui')

# Função bloqueante que espera o pressionamento da tecla
keyboard.read_key()

# A ideia aqui é permanecer no loop se a tecla 'W' foi pressionada
# anteriormente e ainda não foi solta
while True:
    if (not (keyboard.is_pressed('w'))):
        print ('saiu')
        break

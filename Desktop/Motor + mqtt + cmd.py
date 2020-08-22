# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import paho.mqtt.client as mqtt
# Para utilizar ferramentas do sort
import os
# Para utilizar threads
import threading
# Para utilização de temporizadores
import time
# Para leitura do teclado
import keyboard

# Instancia o cliente mqtt
client = mqtt.Client()


#! Definindo funções .#

# Captura de teclas para o controle do motor
def controla_motor ():
    anterior = None


    print ("Controle do motor pronto...Ctrl para sair\r\n")
            
    while True:
        key = keyboard.read_key()
        if (key == 'w'):                  
            anterior = 'w'
            client.publish("motor", "w")
            while True:
                if (not (keyboard.is_pressed('w'))):
                    client.publish("motor", "x")
                    break
        elif (key == 's'):
            anterior = 's'
            client.publish("motor", "s")
            while True:                                                         
                if (not (keyboard.is_pressed('s'))):
                    client.publish("motor", "x")
                    break
        elif (key == 'a'):
            client.publish("motor", "a")
            while True:                         
                if (not (keyboard.is_pressed('a'))):
                    client.publish("motor", "x")
                    break
        elif (key == 'd'):
            client.publish("motor", "d")
            while True:                         
                if (not (keyboard.is_pressed('d'))):
                    client.publish("motor", "x")
                    break
        elif (key == 'space'):
            client.publish("motor", "space")
            while True:                         
                if (not (keyboard.is_pressed('space'))):
                    client.publish("motor", "x")
                    break
        elif (key == 'ctrl'):
            while True:
                if (not (keyboard.is_pressed('ctrl'))):
                    break
            client.publish("motor", "ctrl")
            print ("Encerrando...")
            break
        else:
            pass


# Captura teclas para o controle do angulo da camera
def controla_camera ():
	# O angulo da câmera varia de: -90 a +90 graus
	# E esses valores estão sendo em duty cicle: 88 a 96
    angulo = 92.5
	# Váriavel que irá armzenar a tecla pressionada para o controle
	# da câmera.
    tecla = ''
    
    print ("Controle da camera pronto...\r\n")
    while True:
		# Faz a leitura da tecla pressionada, função bloqueante
        tecla = keyboard.read_key()
		# Verifica se a tecla pressionada é a setinha para cima
		# e se o DutyCicle é menor do que 95
        if (tecla == 'up' and angulo < 95):
            angulo += 0.25
			# O angulo, que aqui representa o duty cicle, é incrementado
			# então envia a mensagem de setinha para cima, para subir
			# a camera
            client.publish("camera", "up")
            while True:
				# Espera a tecla ser solta para não correr o risco de
				# subir muio rapidamente
                if (not (keyboard.is_pressed('up'))):
                    client.publish("camera", "x")                    
                    break            
        elif (tecla == 'down' and angulo > 91):
            angulo -= 0.25
			# O angulo, que aqui representa o duty cicle, é decrementado
			# então envia a mensagem de setinha para baixo, para descer
			# a camera
            client.publish("camera", "down")
            while True:
				# Espera a tecla ser solta para não correr o risco de
				# descer muio rapidamente
                if (not (keyboard.is_pressed('down'))):
                    client.publish("camera", "x")                    
                    break            
        else:
            pass



# Inicializa o broker mosquitto pela linha de comando
# No windows, o mosquitto terá que ter sido adicionado ao PATH
def execute_cmd ():
    os.system ('mosquitto -v')



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("motor/#")
    client.subscribe("camera/#")    

# Função aqui apenas ocmo exemplo, não está mais sendo utilizada no código
# Callback responável por receber uma mensagem publicada no tópico acima
#def on_message(client, userdata, msg):
#    print(msg.topic+" -  "+str(msg.payload))

# Conecta ao broker (loop)
def conect_mqtt ():
    # Instancia o cliente mqtt
    # client = mqtt.Client()
    client.on_connect = on_connect
    # Conecta no MQTT Broker, no meu caso, o Mosquitto
	# se estiver na mesma maquina, pode-se utilizar 'localhost'
	# caso esteja em máquina remota, o 'ip' da máquina remota
	# entre aspas também
    client.connect("localhost", 1883, 60)
    # Inicia o loop
    client.loop_forever()


# Inicio        
if __name__ == "__main__":
	
    # Executa comandos na linha de comandos do Windows
    t1 = threading.Thread(target=execute_cmd)
    t1.start ()
	
    # Espera a inicialização do broker mqtt
    time.sleep (2)              
	
    # Conexao mqtt
    t2 = threading.Thread(target=conect_mqtt)
    t2.start ()
	
    # Espera a conexão cliente mqtt
    time.sleep (2)      
	
    # Controla motor
    # Inicia a trhread para o controle dos motores DC
    t3 = threading.Thread(target=controla_motor)
    t3.start ()

	# Controla camera
    # Inicia a thread para o controle do Servo Motor
    t4 = threading.Thread(target=controla_camera)
    t4.start ()

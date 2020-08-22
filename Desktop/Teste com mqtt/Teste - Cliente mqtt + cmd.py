# Para instalar o paho-mqtt use o comando pip install paho-mqtt
import paho.mqtt.client as mqtt
# Para utilizar ferramentas do sort
import os
# Para utilizar threads
import threading
# Para utilização de temporizadores
import time


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    
    # O subscribe fica no on_connect pois, caso perca a conexão ele a renova
    # Lembrando que quando usado o #, você está falando que tudo que chegar após a barra do topico, será recebido
    client.subscribe("topico/#")
    
# Callback responável por receber uma mensagem publicada no tópico acima
def on_message(client, userdata, msg):
    print(msg.topic+" -  "+str(msg.payload))
    

# Importa o publish do paho-mqtt
#import paho.mqtt.publish as publish
# Publica
#publish.single("topico/teste", "Oi, aqui é um teste", hostname="IP_OU_URL_BROKER")

# Inicializa o broker mosquitto pela linha de comando
def execute_cmd ():
	os.system ('mosquitto -v')

# main
if __name__ == "__main__":
	# Executa comandos na linha de comandos do Windows
    t = threading.Thread(target=execute_cmd)
    t.start ()
    
    print ("comando executado")
    time.sleep (3)
	
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    # Seta um usuário e senha para o Broker, se não tem, não use esta linha
    # client.username_pw_set("USUARIO", password="SENHA")

    # Conecta no MQTT Broker, no meu caso, o Mosquitto
    client.connect("localhost", 1883, 60)
    # client.connect("192.168.146.2", 1883, 60)
    # Inicia o loop
    client.loop_forever()

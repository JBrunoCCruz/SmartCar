'''import paho.mqtt.subscribe as subscribe

msg = subscribe.simple("topico/#", hostname="localhost")
print("%s %s" % (msg.topic, msg.payload))
'''
# Importando apenas a lib para utilizar a subscrição
import paho.mqtt.subscribe as subscribe
# Importando lib para utilização de threads
import threading


# message.payload -> messagem publica no topico
def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))
	
# message.payload -> messagem publica no topico
def on_message_print_motor(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))    



# Função que espera algo ser publicado no topico 'topico'
# Quando há a detecção, é chamada função on_message_print para
# realizar algum trabalho
def on_message_print_t1():
    subscribe.callback(on_message_print, "topico/#", hostname="localhost")    

# Função que espera algo ser publicado no topico 'motor'
# Quando há a detecção, é chamada função on_message_print_motor para
# realizar algum trabalho
def on_message_print_motor_t2():
    subscribe.callback(on_message_print_motor, "motor/#", hostname="localhost")    



# Foi necessario utilizar threads pois os após 'subscribe.callback',
# não era mais possível chamar outras funções. entrava em loop.
if __name__ == "__main__":
    t1 = threading.Thread (target = on_message_print_t1)
    t1.start ()

    t2 = threading.Thread (target = on_message_print_motor_t2)
    t2.start ()

import PySimpleGUI as sg
import webbrowser
import cv2

sg.theme('DarkTeal5')

#Tamanho da tela
WIN_W = 30
WIN_H = 50

#Layout
layout = [
    [ #Linha 1
        sg.Button('Abrir câmera', font=('Consolas', 20), key='-ABRIRCAMERA-')
    ],
    [ #Linha 2
        sg.Text(' ') #Simula uma quebra de linha
    ],
    [ #Linha 3
        sg.Button('V', font=('Consolas', 20), key='-CV-'),
        sg.Text('CV On/Off'),
        sg.Button('P', font=('Consolas', 20), key='-PRINT-'),
        sg.Text('Print'),
        sg.Button('R', font=('Consolas', 20), key='-RECORD-'),
        sg.Text('Rec.')
    ],
    [ #Linha 4
        sg.Text(' ') #Simula uma quebra de linha
    ],
    [ #Linha 5
        sg.Text('Controle do carro'), sg.Text('   '), sg.Text('Controle da câmera')
    ],
    [ #Linha 6
        sg.Button('W ^', font=('Consolas', 20), key='-UP-'),
        sg.Button('S v', font=('Consolas', 20), key='-DOWN-'),
        sg.Text('   '),
        sg.Button('^', font=('Consolas', 20), key='-CAMUP-')
    ],
    [ #Linha 7
        sg.Button('< A', font=('Consolas', 20), key='-LEFT-'),
        sg.Button('D >', font=('Consolas', 20), key='-RIGHT-'),
        sg.Text('   '),
        sg.Button('v', font=('Consolas', 20), key='-CAMDOWN-')
    ],
    [ #Linha 8
        sg.Text(' ') #Simula uma quebra de linha
    ],
    [ #Linha 9
        sg.Text('Log')
    ],
    [ #Linha 10
        sg.Output(size=((WIN_W*2), int(WIN_W/2)))
    ]
]

#Classe contendo app
class App():
    def __init__(self):
        self.window = sg.Window('SmartCar', layout=layout, margins=(0,0), return_keyboard_events=False)
        self.window.read(timeout=1)
        self.cv = True
        self.ipJetson = ''
    
    def start(self):
        while True:
            event, self.values = self.window.Read()
            print(event)

            if event in (None, 'Exit', sg.WIN_CLOSED):
                break

            if event in ('-ABRIRCAMERA-'):
                self.ipJetson = sg.popup_get_text('Informe o IP da Jetson','IP Jetson')
                webbrowser.open('http://{}:8000'.format(self.ipJetson, new=0, autoraise=True))
                print('Jetson cam running on IP: {}'.format(self.ipJetson))
            
            if event in ('-CV-'):
                self.cv = True if self.cv == False else False
                print('CV {}'.format('On' if self.cv == True else 'Off'))
            
            if event in ('-PRINT-'):
                print('')

            if event in ('-RECORD-'):
                print('')

            if event in ('-UP-'):
                print('')

            if event in ('-DOWN-'):
                print('')

            if event in ('-LEFT-'):
                print('')

            if event in ('-RIGHT-'):
                print('')

            if event in ('-CAMUP-'):
                print('')

            if event in ('-CAMDOWN-'):
                print('')
            
            if event == 'p' or event == 'P':
                print('P/p pressionado')

app = App()
app.start()

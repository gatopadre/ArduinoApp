import os
import sys
import serial
import time
import json
from helpers import terminal_messages

arduino = serial.Serial()
arduino.baudrate = 9600
arduino.bytesize=serial.EIGHTBITS
arduino.parity=serial.PARITY_NONE
arduino.stopbits=serial.STOPBITS_ONE
arduino.timeout=1
arduino.xonxoff=False
arduino.rtscts=False
arduino.dsrdtr=False
arduino.writeTimeout=None

if os.name == 'nt':
    arduino.port = 'COM6' # para windows
else:
    arduino.port = '/dev/ttyACM0' # para linux

def connect():
    result = False
    if arduino.is_open:
        terminal_messages.show_message('success', 'conexion exitosa.')
        result = {'option':'connect', 'value' : 'conexion exitosa.'}
    terminal_messages.show_message('info', 'abriendo conexion con arduino...')
    arduino.open()
    time.sleep(2)
    if arduino.is_open:
        terminal_messages.show_message('success', 'conexion exitosa.')
        result = {'option':'connect', 'value' : 'conexion exitosa.'}
    else:
        terminal_messages.show_message('error', 'conexion fallida.')
        result = {'option':'connect', 'value' : 'conexion fallida.'}

def disconnect():
    result = False
    terminal_messages.show_message('info', 'cerrando conexion con arduino...')
    if arduino.is_open:
        arduino.close()
        terminal_messages.show_message('success', 'conexion cerrada.')
        result = {'option':'disconnect', 'value' : 'conexion cerrada.'}
    else:
        result = {'option':'disconnect', 'value' : 'conexion cerrada.'}
    return result

def receive_data():
    if arduino.is_open:
        result = arduino.read(100)
        message = 'resultado : {}'.format(result)
        terminal_messages.show_message('debug', message)
        if not result:
            terminal_messages.show_message('error', 'no se recibio lectura.')
        else:
            message = 'mensaje recibido "{}"'.format(result)
            terminal_messages.show_message('success', message)

def read_line():
    if arduino.is_open:
        result = arduino.readline()
        message = 'resultado : {}'.format(result)
        terminal_messages.show_message('debug', message)
        if not result:
            terminal_messages.show_message('error', 'no se recibio lectura.')
        else:
            message = 'mensaje recibido "{}"'.format(result)
            terminal_messages.show_message('success', message)

def send_data(data):
    if arduino.is_open:
        message = 'enviando data "{}" a arduino...'.format(data)
        terminal_messages.show_message('info', message)
        arduino.write(data.encode())

''' recibe la orden para enviar a arduino y devuelve json con la respuesta '''
def send_order(data):
    result = False
    if arduino.is_open:
        message = 'enviando orden "{}" a arduino...'.format(data)
        terminal_messages.show_message('info', message)
        arduino.write(data.encode())
        time.sleep(1)
        result = arduino.readline()
        if not result or result == b'\r\n':
            terminal_messages.show_message('error', 'respuesta arduino vacia.')
            return {'option':'error', 'value':'respuesta arduino vacia.'}
        result = result.decode('utf-8').strip('\n')
        result = result.replace('\'','"')
        result = json.loads(result)
    else:
        result = {'option':'error', 'value' : 'se ha perdido la conexion con arduino'}
    terminal_messages.show_message('info', result)
    return result

def status():
    result = False
    if arduino.is_open:
        result = {'option':'status', 'value' : 'conectado'}
    else:
        result = {'option':'status', 'value' : 'desconectado'}
    return result
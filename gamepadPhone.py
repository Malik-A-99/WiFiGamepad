import zmq
import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

context = zmq.Context()

bg_color = (0,128,128)
screen = pygame.display.set_mode((300,300))
pygame.display.set_caption('test')
screen.fill(bg_color)
pygame.display.flip()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
if (socket.connect("tcp://10.27.27.12:5555")):
    print('Connected!')

buttonCount = joystick.get_numbuttons()
button = []
for i in range(buttonCount):
    button.append(i)

while True:
    analogLeftX = round(joystick.get_axis(0), 3)
    analogLeftY = round(joystick.get_axis(1), 3)
    analogRightX = round(joystick.get_axis(2), 3)
    analogRightY = round(joystick.get_axis(3), 3)
    TriggerLeft = round(joystick.get_axis(4), 3)
    TriggerRight = round(joystick.get_axis(5), 3)


    event = pygame.event.wait()

    if event.type == JOYAXISMOTION or event.type == JOYBUTTONDOWN or event.type == JOYBUTTONUP:
        socket.send_string(str(analogLeftX)+"|"+
                           str(analogLeftY)+"|"+
                           str(analogRightX)+"|"+
                           str(analogRightY)+"|"+
                           str(TriggerLeft)+"|"+
                           str(TriggerRight)+"|"+
                           str(joystick.get_button(button[0]))+"|"+
                           str(joystick.get_button(button[1]))+"|"+
                           str(joystick.get_button(button[2]))+"|"+
                           str(joystick.get_button(button[3]))+"|"+
                           str(joystick.get_button(button[4]))+"|"+
                           str(joystick.get_button(button[5]))+"|"+
                           str(joystick.get_button(button[6]))+"|"+
                           str(joystick.get_button(button[7]))+"|"+
                           str(joystick.get_button(button[8]))+"|"+
                           str(joystick.get_button(button[9]))+"|"+
                           str(joystick.get_button(button[10]))+"|"+
                           str(joystick.get_button(button[11]))+"|"+
                           str(joystick.get_button(button[12]))+"|"+
                           str(joystick.get_button(button[13]))+"|"+
                           str(joystick.get_button(button[14]))+"|"+
                           str(joystick.get_button(button[15])))
        message = socket.recv()
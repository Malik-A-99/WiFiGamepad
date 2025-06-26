import zmq
import vgamepad as vg

gamepad = vg.VX360Gamepad()

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print('starting gamepad')
while True:
    #  Format message received from controller
    message = str(socket.recv())
    message = message.replace("b",'')
    message = message.replace("'",'')

    button = []

    LeftStickX,LeftStickY,RightStickX,RightStickY,TriggerLeft,TriggerRight,b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15 = message.split("|")
    #print(message)
    
    gamepad.left_joystick_float(float(LeftStickX), float(LeftStickY) * -1)
    gamepad.right_joystick_float(float(RightStickX), float(RightStickY) * -1)
    gamepad.left_trigger_float(float(TriggerLeft))
    gamepad.right_trigger_float(float(TriggerRight))


    (b0 == '1' and gamepad.press_button(0x1000)) 
    (b0 == '0' and gamepad.release_button(0x1000))

    (b1 == '1' and gamepad.press_button(0x2000)) 
    (b1 == '0' and gamepad.release_button(0x2000))

    (b2 == '1' and gamepad.press_button(0x4000)) 
    (b2 == '0' and gamepad.release_button(0x4000))

    (b3 == '1' and gamepad.press_button(0x8000)) 
    (b3 == '0' and gamepad.release_button(0x8000))

    (b4 == '1' and gamepad.press_button(0x0020)) 
    (b4 == '0' and gamepad.release_button(0x0020))

    (b5 == '1' and gamepad.press_button(0x0010)) 
    (b5 == '0' and gamepad.release_button(0x0010))

    (b6 == '1' and gamepad.press_button(0x0010)) 
    (b6 == '0' and gamepad.release_button(0x0010))

    (b7 == '1' and gamepad.press_button(0x0040)) 
    (b7 == '0' and gamepad.release_button(0x0040))

    (b8 == '1' and gamepad.press_button(0x0080)) 
    (b8 == '0' and gamepad.release_button(0x0080))

    (b9 == '1' and gamepad.press_button(0x0100)) 
    (b9 == '0' and gamepad.release_button(0x0100))

    (b10 == '1' and gamepad.press_button(0x0200)) 
    (b10 == '0' and gamepad.release_button(0x0200))

    (b11 == '1' and gamepad.press_button(0x0001)) 
    (b11 == '0' and gamepad.release_button(0x0001))

    (b12 == '1' and gamepad.press_button(0x0002)) 
    (b12 == '0' and gamepad.release_button(0x0002))

    (b13 == '1' and gamepad.press_button(0x0004)) 
    (b13 == '0' and gamepad.release_button(0x0004))

    (b14 == '1' and gamepad.press_button(0x0008)) 
    (b14 == '0' and gamepad.release_button(0x0008))

    # (b15 == '1' and gamepad.press_button(0x1000)) 
    # (b15 == '0' and gamepad.release_button(0x1000)) 
    gamepad.update()
    
    

    #  Send reply back to client
    socket.send_string(str(message))
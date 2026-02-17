---
---
 
Crie o SDCard
https://www.ev3dev.org/downloads/
https://education.lego.com/en-us/product-resources/mindstorms-ev3/teacher-resources/python-for-ev3/

Documentação
https://docs.pybricks.com/en/v2.0/index.html

IDE
https://vscodium.com/

Extensão
https://open-vsx.org/vscode/item?itemName=ev3dev.ev3dev-browser

Com isso vc consegue usar seu ev3 pelo cabo USB.

Agora vamos preparar o pc para usar pelo Bluetooth

Instale no Debian 13:
sudo apt install bluez

Wireless and Networks >
Bluetooth >
Powered [x]
Visible [x]

Escaneie no PC e confirme no EV3

Wireless and Networks >
Tethering>
Bluetooth [x]

Inicie a conexão e aceite no EV3:
Authorize service BNEP? Accept

Código main.py de exemplo:
#!/usr/bin/env pybricks-micropython

## exemplo
# fonte: https://docs.pybricks.com/en/v2.0/start_ev3.html
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port

# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
#test_motor = Motor(Port.B)

# Write your program here

# Play a sound.
ev3.speaker.beep()

# Escrever na tela
ev3.screen.clear()
ev3.screen.print("Ola Mundo!")

# Falar
ev3.speaker.set_speech_options("pt-br")
ev3.speaker.say("Ola Mundo")

# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 90)

# Play another beep sound.
ev3.speaker.beep(frequency=1000, duration=500)

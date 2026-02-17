---
---

Esses dias peguei um PTP que estava sofrendo interferência e não conseguia acessar o lado AP por HTTP. Muito lento consegui abrir SSH.
Então precisei alterar a frequência pra depois continuar a configurar.
Usei o comando SED que esta disponível no shell.
Supondo que mudei de 5500 MHz para 5560 MHz segue o exemplo



cd /tmp/
sed -i "s/radio.1.freq=5500/radio.1.freq=5560/g" running.cfg
sed -i "s/radio.1.freq=5500/radio.1.freq=5560/g" system.cfg
save
reboot

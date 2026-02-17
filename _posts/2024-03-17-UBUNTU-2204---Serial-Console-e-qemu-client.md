### QEMU AGENT

Instala o cliente qemu lembre de ativar na options da VM

```
sudo apt -y install qemu-guest-agent
sudo systemctl enable qemu-guest-agent
sudo systemctl startqemu-guest-agent
sudo systemctl statusqemu-guest-agent
```

### Ativar Serial Console

#### Altera o grub

Recomendo fazer um snapshot pq um erro no grub pode causar muita dor de cabeça

vi /etc/default/grub

```
GRUB_CMDLINE_LINUX="console=tty0 console=ttyS0,115200n8"
```

Agora a ediçõa do arquivo vai ser aplicada ao grub de fato.

update-grub

fonte: <https://help.ubuntu.com/community/SerialConsoleHowto>

####  Serviço com autologin

Se alguém chegou no seu proxmox pra colocar um disco de boot alternativo e trocar sua senha da maquina ta fácil. Execto se vc realmente criptografou o disco. Mas nesse ponto ainda sim outros tantos problemas podem ocorrer. Se a maquina for sua e o proxmox também facilita sua vida. Nerds de segurança podem deixar comentários com uma lista de motivos pra não fazer isso.

Outra forma é criar um arquivo com serviço no sistema:

mkdir /etc/systemd/system/serial-getty@ttyS0.service.d

cd /etc/systemd/system/serial-getty@ttyS0.service.d

vi autologin.conf
```

[Service]
ExecStart=
ExecStart=/sbin/agetty -a root --noclear %I 115200 vt102
```

Ative o serviço e inicie ele:

```
systemctl enable serial-getty@ttyS0.service
systemctl start serial-getty@ttyS0.service
```

**Sudo**

Para facilitar o acesso crie um arquivo pra cada usuário em

```
cd /etc/sudoers.d
vi joao
joaoALL=(ALL:ALL) ALL
vi maria
maria ALL=NOPASSWD: ALL
```

João vai precisar digitar a senha dele pra virar root

Maria nem vai precisar lembrar a senha dela pra virar root. Aqui é vacilo pq se por algum serviço bugado alguém ganhar seu shell, já ganha o do root também.

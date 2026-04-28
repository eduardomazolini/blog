---
order: 2
---
# Splash

Alguns usuários ficam intimidados com os detalhes dos logs de inicialização só o fato de exibir os dados os assusta, então vamos colocar uma tela mais bonita e esconder os detalhes.
Esses detalhes ainda podem ser vistos pressionando `<ESC>`.

Edite o arquivo `/etc/default/grub`
```
sudo vi /etc/default/grub
```

Altere para conter a palavra `splash`
```
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"
```

Atualize e reinicie:
```
sudo update-grub
sudo reboot
```

Para trocar o efeito:
```
sudo plymouth-set-default-theme --list
sudo plymouth-set-default-theme spinner 
udo update-initramfs -u -k all
```

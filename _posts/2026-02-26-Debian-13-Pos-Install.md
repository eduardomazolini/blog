---

tags: [linux, debian]
---

# Meu pós-instalação do Debian

## Alt+Tab
> Vou chamar de **Super** a tecla que normalmente fica entre Crtl e Alt, que em muitos teclados tem o logo do Windows.

Para editar as teclas de atalho navegue até:

Configurações -> Teclado -> Atalhos de Teclado -> Veja e personalize atalhos -> Navegação


### Alternar entre aplicativos

Apesar da janela de configuração mostrar Super+Tab, no terminal podemos ver que são 2 combinações:
- Super+Tab
- Alt+Tab

O **Super+Tab** mantem o modo linux de alternar entre aplicativos.

### Alternar entre janelas

Para funcionar o **Alt+Tab** igual no Windows ou seja alternar entre todas as janelas e não só entre aplicativos eu faço a alteração pela interface gráfica mesmo.


### Alternar entre janelas do mesmo applicativo

Mas também aproveito para ensinar que existe o **Alt+'(tecla acima do tab)** que alterna entre janelas do mesmo app.

### Opção por terminal

```
gsettings list-recursively org.gnome.desktop.wm.keybindings 
```
Quando vc altera pela interface grafica a opção backward é configurada automaticamente.
No terminal é preciso especificar a sequencia de atalho.

```
gsettings set org.gnome.desktop.wm.keybindings switch-applications "['<Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "['<Shift><Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows-backward "['<Shift><Alt>Tab']"
```

## [Flatpak](https://flatpak.org/setup/Debian)

Para ativar o flatpak existe um tutorial simples no site oficial, lá tem a opção pra GNOME e KDE
Ao instalar o plugin do gnome ele já instala o flatpak como dependência.

```
sudo apt install gnome-software-plugin-flatpak
```

Precisa também configurar o repositório
```
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

## [AppImage](https://appimage.org/)

Alguns AppImages exigem [FUSE versão 2](https://github.com/AppImage/AppImageKit/wiki/FUSE) para ser executado. O AppImages mais recente tem a versão 3 do FUSE incorporada. Filesystem no Userspace (FUSE) é um sistema que permite que usuários não-root montem sistemas de arquivos.

> O site do FUSE recomenda uma alteração de repositório que não precisei fazer.

```
sudo apt install libfuse2t64
```

**[Gear Lever](https://gearlever.mijorus.it/)** organiza os AppImage:
```
sudo flatpak install flathub it.mijorus.gearlever
```

> VM
>
>Eu executei na VM e precisei colocar `--disable-gpu` nos parâmetros de um AppImage. Acredito que o erro seja pontual, por isso não procurei mais detalhes. Ativando **OpenGL** e **Aceleração 3D** também funcionou.

## Splash

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

## Luks

> Não use esse tutorial por enquanto!
> Se vc souber o problema por favor me avise!

Um pequeno ajuste para não ter que digitar 2 senhas no boot

### Preparar o ambiente:
Preciso declarar no `/etc/cryptsetup-initramfs/conf-hook`
```
echo 'KEYFILE_PATTERN=/etc/keys/*.key' | sudo tee -a /etc/cryptsetup-initramfs/conf-hook
```
> Importante! Esse passo só ocorre uma vez mas é fundamental pro sistema funcionar. Mas também é o problema deste tutorial.
> A chave é copiada do disco que esta criptografado para dentro do initramfs que não é criptografado, nem esta em uma partição criptografada.

Vou criar uma chave em um local seguro:
```
sudo mkdir -m 700 /etc/keys
sudo chmod 400 /etc/keys/vda3.key
```

### Criar a chave da partição:

Criar a chave especifica desta partição:
```
sudo dd if=/dev/urandom of=/etc/keys/vda3.key bs=512 count=8
```

Editar o `/etc/crypttab`,  a linha que trata do vda3 entre o UUID e demais para metros tem a palavra `none`, vamos trocar pelo caminho do arquivo.

De:
```
vda3_crypt UUID=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx none luks,swap,discard,x-initrd.attach
```

Para:
```
vda3_crypt UUID=xxxxxxxx-xxxx-xxxx-xxxxx-xxxxxxxxxxxx /etc/keys/vda3.key luks,swap,discard,x-initrd.attach
```

Vou atribuir essa chave ao Luks. Será solicitado a senha atual. não vamos apagar ela, só estamos adicionando mais uma forma de abrir:
```
sudo cryptsetup luksAddKey /dev/vda3 /etc/keys/vda3.key
```

### Atualizar a inicialização
Atualizar o initramfs para ele guardar a chave e saber a quem pertence:
```
sudo update-initramfs -u
```

### Se deu errado?

Eu tive um problema ao criar o swap, precisei refazer:
Desativei:
```
sudo swapoff /dev/mapper/vda3_crypt
sudo cryptsetup close vda3_crypt
```

Formatei novamente o Luks:
```
sudo cryptsetup luksFormat --type luks2 /dev/vda3
```

A saída:
```
WARNING!
========
Isto vai sobrescrever dados em /dev/vda3 permanentemente.

Are you sure? (Type 'yes' in capital letters): YES
Digite a senha para /dev/vda3: 
Verificar senha:
```

Adicionei novamente a chave:
``` 
sudo cryptsetup luksAddKey /dev/vda3 /etc/keys/vda3.key
``` 

A saída:
``` 
Digite qualquer senha existente: 
Warning: keyslot operation could fail as it requires more than available memory.
Warning: keyslot operation could fail as it requires more than available memory.
``` 

Abri com a chave para testar:
``` 
sudo cryptsetup open /dev/vda3 vda3_crypt --key-file /etc/keys/vda3.key
``` 
A saída:
``` 
Warning: keyslot operation could fail as it requires more than available memory.
```

Tive que pegar o novo id:
```
lsblk | grep vda3_crypt
sudo blkid /dev/vda3
```

Trocar no `/etc/crypttab`
```
sudo vi /etc/crypttab
```

Formatar o swap:
```
sudo mkswap /dev/mapper/vda3_crypt
sudo swapon /dev/mapper/vda3_crypt
```

Um ajuste de segurança:
```
echo 'UMASK=0077' | sudo tee /etc/initramfs-tools/conf.d/umask
```
> `/etc/initramfs-tools/initramfs.conf` também pode conter o valor

Atualizado o initramfs:
```
sudo update-initramfs -u
```
A saída:
```
update-initramfs: Generating /boot/initrd.img-6.12.73+deb13-amd64
cryptsetup: WARNING: Resume target vda3_crypt uses a key file
```

## Hibernar

Para hibernar parece o initramfs precisa saber onde esta armazenado o dump da memoria RAM.
Esse espaço precisa ser **2/5 maior que a memória RAM** segundo o [wiki do Debian](https://wiki.debian.org/Hibernation#Suspend_and_hibernate_configuration_with_systemd_.2F_Debian_Buster_and_more_recent), pra quem tem pouca memória trabalhar com o dobro ou no minimo 50%

O Debian deixou a informação por padrão em `/etc/initramfs-tools/conf.d/resume`:
```
RESUME=/dev/mapper/vda3_crypt
```

---
tags: [linux, Proxmox, VM]
---

Como falei antes usar cloud-init e libguestfs é muito útil aqui vou escrever como eu usei.

Primeiro precisa instalar a ferramenta:
  
  
    apt install libguestfs-tools guestfsd -y
  




Eu guardo minhas ISOs em um NFS que não fica no servidor mas está montado nele, então vou trabalhar dele assim posso usar o resultado em todos os servidores da rede, use a pasta onde você guarda suas ISOs e templates.
  
  
    cd /mnt/pve/nfs-remoto/
  

Baixe o arquivo da sua distribuição, observe que eu usei genericcloud e extensão raw.
  
  
    wget https://cloud.debian.org/img/cloud/bookworm/latest/debian-12-genericcloud-amd64.raw
  




Para facilitar minha vida criei um script pra deixar a imagem com os ajustes que eu uso. Mas você pode fazer linha por linha.

UPDATE: 22/09/2025

Saiu a versão 13 do Debian eu precisei fazer novamente

Ai resolvi melhorar o script.

Desta vez deixei no GitHub Gist para facilitar o Download.

[create-vm-linux.sh](https://gist.github.com/eduardomazolini/a83b111a93904f209202e41060d51638)

[customize-image.sh](https://gist.github.com/eduardomazolini/124d62de2b0c50b0a15de2d25ca766e2) 





Eu criei o arquivo **cloud-prep.sh** :
  
  
    #!/bin/bash
    IMAGEM="debian-12-genericcloud-amd64.raw"
    SERIAL_DEVICE="ttyS0"
    BAUD_RATE="115200"
  
    # Instala QEMU Guest Agent
    virt-customize -a "$IMAGEM" \
      --install qemu-guest-agent
  
    # Criar diretório de override para serial-getty
    virt-customize -a "$IMAGEM" \
      --mkdir /etc/systemd/system/serial-getty@${SERIAL_DEVICE}.service.d
  
    # Criar arquivo de override com autologin root
    virt-customize -a "$IMAGEM" \
      --write "/etc/systemd/system/serial-getty@${SERIAL_DEVICE}.service.d/override.conf:[Service]
    ExecStart=
    ExecStart=-/sbin/agetty --autologin root --keep-baud ${BAUD_RATE},38400,9600 %I \$TERM
    TTYVTDisallocate=no"
  
    # Habilitar o serviço serial-getty
    virt-customize -a "$IMAGEM" \
      --run-command "systemctl enable serial-getty@${SERIAL_DEVICE}.service"
  
    # Configurar GRUB_CMDLINE_LINUX
    virt-customize -a "$IMAGEM" \
      --edit '/etc/default/grub:s/^GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX="console=tty0 console='${SERIAL_DEVICE}','${BAUD_RATE}'"/'
  
    # Configurar GRUB_TERMINAL
    virt-customize -a "$IMAGEM" \
      --edit '/etc/default/grub:s/^#?GRUB_TERMINAL=.*/GRUB_TERMINAL="console serial"/'
  
    # Configurar GRUB_SERIAL_COMMAND
    virt-customize -a "$IMAGEM" \
      --edit '/etc/default/grub:s/^#?GRUB_SERIAL_COMMAND=.*/GRUB_SERIAL_COMMAND="serial --speed='${BAUD_RATE}' --unit=0 --parity=no --stop=1"/'
  
    # Atualizar configuração do GRUB
    virt-customize -a "$IMAGEM" \
      --run-command "update-grub"
  
    echo "Configurado qemu-guest-agent"
    echo "Configuração do console serial"
  

O arquivo deve ser executável:
  
  
    chmod +x ~/cloud-prep.sh
  

Execute:
  
  
    ~/cloud-prep.sh
  

Então use o novo arquivo em suas VMs importando o disco, no exemplo o ID da VM é 101 altere para o de sua VM:
  
  
    qm importdisk 101 debian-12-genericcloud-amd64.raw local-lvm
  

Por ultimo adicione ao Hardware da VM o **CloudInit Drive** para poder fazer as configurações. Eu usei **EFI Disk** também.

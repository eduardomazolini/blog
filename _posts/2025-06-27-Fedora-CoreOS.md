---
tags: [linux, Proxmox, VM]
---

Para usar o Fedora Core é necessário criar um arquivo de inicialização semelhante à ideia do Cloud-init.

Mas o arquivo de configuração YAML (YAML Ain't Markup Language) é conhecido como [Butane](https://coreos.github.io/butane/).

Esse arquivo precisa ser convertido para JSON, conhecido como [Ignition](https://coreos.github.io/ignition/).

Para definir a senha no arquivo, é preciso criar o hash usado no Linux. Uma forma de fazer isso é usando Podman:
  
  
  podman run -ti --rm quay.io/coreos/mkpasswd --method=yescrypt

Exemplo do arquivo Butane que eu usei:
```
variant: fcos
version: 1.6.0
passwd:
  users:
    - name: core
      ssh_authorized_keys:
        - ssh-ed25519 AAAAC3NzaXXXXXXXXXXXXXXXII/RsHt5CL/v5juZaj+qmQfw9G+n6J24PzTLu+hIuMOd
      password_hash: $y$j9T$GNBLbCycFxXXXXni1hs.$GHx/wq5SwJpqyXXXXXXXXXXtfDY9nSYqLx7jqpt2w99
storage:
  files:
    - path: /etc/hostname
      mode: 0644
      contents:
        inline: fcos01
    - path: /etc/vconsole.conf
      mode: 0644
      contents:
        inline: |
          KEYMAP=br-abnt2
systemd:
  units:
    - name: rpm-ostree-install-qemu-agent.service
      enabled: true
      contents: |
        [Unit]
        Description=Install QEMU Guest Agent
        Wants=network-online.target
        After=network-online.target
        Before=systemd-user-sessions.service
        ConditionPathExists=!/usr/bin/qemu-ga
        
        [Service]
        Type=oneshot
        RemainAfterExit=yes
        ExecStart=/usr/bin/rpm-ostree install --apply-live --allow-inactive qemu-guest-agent
        ExecStartPost=/usr/bin/systemctl enable --now qemu-guest-agent.service
        
        [Install]
        WantedBy=multi-user.target    - name: serial-getty@ttyS0.service
    - name: serial-getty@ttyS0.service
      dropins:
      - name: autologin-core.conf
        contents: |
          [Service]
          # Override Execstart in main unit
          ExecStart=
          # Add new Execstart with `-` prefix to ignore failure`
          ExecStart=-/usr/sbin/agetty --autologin core --noclear %I $TERM
```

Para converter o Butane em Ignition:

No Linux:
podman run -i --rm quay.io/coreos/butane --pretty --strict < fcos.bn | tee fcos.ign

No PowerShell:
```
Get-Content fcos.bn | 
    podman run -i --rm quay.io/coreos/butane --pretty --strict | 
    ConvertFrom-Json | 
    ConvertTo-Json -Depth 100 -Compress | 
    Set-Content fcos.minimized.ign -Encoding utf8
```
    

Ou:
```
Get-Content fcos.bn | 
    podman run -i --rm quay.io/coreos/butane --pretty --strict | 
    Tee-Object -FilePath fcos2.ign -Encoding utf8
```
    

Se for usar VirtualBox:

Depois de importar o arquivo OVA, crie o guestproperty:
    
```    
"C:\Program Files\Oracle\VirtualBox\VBoxManage.exe" guestproperty set 'FCOS' /Ignition/Config "$(cat .\fcos.minimized.ign)"
```

No meu caso, a máquina chamava FCOS e o arquivo Ignition fcos.minimized.ign.

Se for usar Proxmox, uma opção é iniciar com ISO e depois baixar o ign previamente hospedado por HTTP:

```
curl -o coreos.ign http://<ip-address>:8080/coreos/coreos.ign
coreos-installer install /dev/sda -i coreos.ign
```

Outra opção é editar o arquivo:
```
/etc/pve/qemu-server/<vmid>.conf
```

```
cicustom: vendor=nfs-remoto:snippets/example.ign
```

```
qm set 1001 --cicustom "vendor=nfs-remoto:snippets/example.ign"
```

Adicione na máquina uma interface serial porque foi configurada como terminal.

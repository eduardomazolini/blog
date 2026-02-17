---
---

Para ativar os PCs que suspenderam por tempo e ter acesso remoto.

1) Instalar o ethtool
  
  
    sudo apt update
    sudo apt install ethtool
  

2) listar as interfaces
  
  
    ip addr
  

No meu caso identifiquei `enp2s0`

3) Crie o arquivo de serviço como root
  
  
    sudo nano /etc/systemd/system/wol@.service
  

4) coloque o conteúdo
  
  
    [Unit]
    Description=Wake-on-LAN para %i
    After=network.target suspend.target hibernate.target
  
    [Service]
    Type=oneshot
    ExecStart=/sbin/ethtool -s %i wol g
  
    [Install]
    WantedBy=multi-user.target suspend.target hibernate.target
  

5) Ative o serviço e desta vez observe que o nome do serviço contém a interface
  
  
    sudo systemctl enable wol@enp2s0.service
  

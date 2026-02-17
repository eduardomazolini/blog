---
tags: [linux]
---

http://poptop.sourceforge.net/yum/stable/packages/ppp-2.4.4-9.0.rhel5.i386.rpm
http://poptop.sourceforge.net/yum/stable/packages/pptpd-1.3.4-1.rhel5.1.i386.rpm
http://poptop.sourceforge.net/yum/stable/packages/dkms-2.0.17.5-1.noarch.rpm
http://poptop.sourceforge.net/yum/stable/packages/kernel_ppp_mppe-1.0.2-3dkms.noarch.rpm
    
Instalei esses arquivos e segui um tutorial do próprio site da [poptop](https://poptop.sourceforge.net/dox/).

## Atualização 2026

Felizmente o mundo melhorou muito no linux eu usava Debian e dependia de pacotes rpm da RedHat.
Mas sobre **PPTP** a atualização é **não use**.
Que momento estamos, o **OpenVPN** já virou passado, o queridinho agora é o **WireGuard**.
O Windows 10 encerrou no fim do ano e o cliente padrão dele permitia redes **IKEv2**, **L2TP/IPsec**, **SSTP** e **PPTP**.
O MacOS aceita **IKEv2**, **L2TP/IPsec** não aceita o **PPTP** a algum tempo. Precisa ainda do software oficial para o **WireGuard**.
No Linux Debian 13 o cliente já vem nativo com **L2TP**, **WireGuard** e **PPTP** (mas não é pq tem que você deve usar.)
Hoje VPN de instalação rápida ainda é **L2TP/IPsec**. Mas o modo certo de entregar isso para um cliente é sem duvida o **WireGuard** assim como a alguns ano era o **OpenVPN**.

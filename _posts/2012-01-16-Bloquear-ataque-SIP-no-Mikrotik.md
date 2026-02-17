---
tags: [asterisk, Mikrotik, segurança, voip]
---

Gostaria de compartilhar como eu fiz para evitar ataques ao meu Asterisk.
Em casa eu tenho uma routerboard com mikrotik.
Penso que o que fiz aqui pode ser utilizado direto no linux também se alguém souber exatamente como por favor divida comigo.

Por favor, não copie o que você não entende.

```
/ip firewall layer7-protocol
add name=sip regexp="sip/[0-2]\\\\.[0-9].403"

/ip firewall mangle
add action=add-dst-to-address-list address-list="SENHA SIP ERRADA" address-list-timeout=2m chain=forward comment="Marca ip com senha errada" disabled=no layer7-protocol=sip protocol=udp src-port=5060

/ip firewall filter 
add action=drop chain=forward comment="senha sip errada" disabled=no dst-port=5060 protocol=udp src-address-list="SENHA SIP ERRADA"
```

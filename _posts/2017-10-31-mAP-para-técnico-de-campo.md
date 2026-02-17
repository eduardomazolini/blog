---
---

### **Objetivo:**

Permitir ao técnico agilidade na instalação acessando todos os equipamentos sem ficar fixando IP.
A configuração se parece com:
\- as Ethernet em bridge
\- a WLAN com NAT e servidor DHCP.

**Sugestões  adicionais não listadas aqui:**
\- O mAP pode fazer para o cliente a demonstração do serviço de Hotspot do Mikrotik
\- O mAP pode discar uma OVPN pra um servidor da empresa.
\- O Suporte pode discar uma EoIP em cima da OVPN pra ajudar o técnico de campo.



### **Pontos de atenção:**

\- Mikrotik reiniciado sem configuração default não tem IP precisa de acesso por MAC, tem que estar na mesma bridge.
\- O notebook ou celular do técnico precisa de um servidor DHCP,
\- Como é tudo uma só bridge e tem um DHCP Server ativo devemos evitar que ele conflite com o roteador do cliente ou DHCP da CPE que serve ao roteador do cliente.



### **Solução:**

1) Trabalhar em bridge para permitir o acesso ao mikrotik por MAC.
2) Adicionar vários IPs diferentes na bridge para comunicação com cada rede que os equipamentos usam.
3) Criar DHCP Server da RB que é usada no Wi-Fi.
4) Fazer SRC-NAT do que vai para os equipamentos pois eles não tem gateway default.
5) Filtrar DHCP Server da RB que não atrapalhe a rede do cliente.
6) Configurações Básicas para acesso a RB.




### **Passo a passo:**

**1) Trabalhar em bridge para permitir o acesso ao mikrotik por MAC.**

/interface bridge
add name=bridge
/interface bridge port
add bridge=bridge interface=wlan1
add bridge=bridge interface=ether1
add bridge=bridge interface=ether2
**
****2) Adicionar vários IPs diferentes na bridge para comunicação com cada rede que os equipamentos usam.**





/ip address
add address=192.168.1.10/24 interface=bridge comment="UBNT"
add address=10.0.0.204/24 interface=bridge comment="Padrao p Cliente"
/ip dhcp-client
add default-route-distance=1 disabled=no interface=bridge


/ip dns
set servers=8.8.8.8,8.8.4.4
/ip route
add distance=10 gateway=10.0.0.1 comment="Padrao p Cliente distancia maior que dhcp client"




**3) Criar DHCP Server da RB que é usada no Wi-Fi.**





/ip address

add address=192.168.5.1/24 interface=bridge
/ip pool
add name=pool-wifi ranges=192.168.5.100-192.168.5.200
/ip dhcp-server
add address-pool=pool-wifi disabled=no interface=bridge name=server-wifi

/ip dhcp-server network
add address=192.168.5.0/24 dns-server=8.8.8.8,8.8.4.4 gateway=192.168.5.1


/interface wireless security-profiles
add authentication-types=wpa-psk,wpa2-psk mode=dynamic-keys name=wireless \
    wpa-pre-shared-key=02091925 wpa2-pre-shared-key=02091925
/interface wireless
set [ find default-name=wlan1 ] disabled=no mode=ap-bridge security-profile=wireless \
    ssid=WiFiTecnico




**4) Fazer SRC-NAT do que vai para os equipamentos pois eles não tem gateway default.**


/ip firewall nat
add action=masquerade chain=srcnat src-address=192.168.5.0/24






**5) Filtrar DHCP Server da RB que não atrapalhe a rede do cliente.**





/interface bridge filter
add action=drop chain=input dst-port=67 in-interface=ether1 ip-protocol=udp \
    mac-protocol=ip
add action=drop chain=output dst-port=68 ip-protocol=udp mac-protocol=ip \
    out-interface=ether1
add action=drop chain=input dst-port=67 in-interface=ether2 ip-protocol=udp \
    mac-protocol=ip
add action=drop chain=output dst-port=68 ip-protocol=udp mac-protocol=ip \
    out-interface=ether2
add action=drop chain=forward dst-port=67 in-interface=wlan1 ip-protocol=udp \
    mac-protocol=ip
add action=drop chain=forward dst-port=68 ip-protocol=udp mac-protocol=ip \
    out-interface=wlan1

**6) Configurações Básicas para acesso a RB.**





/system identity
set name=mAP-Tecnico1
/user group
add name=null
/user aaa
set default-group=null


/user


add name=BLABLABLA password=BLABLABLA group=full
set [find name=admin] group=null password=RANDOM

set 0 group=null




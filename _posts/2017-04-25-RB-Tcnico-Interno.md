---
---

### **Objetivo:**

Permitir ao técnico ficar na rede da empresa e ter acesso aos equipamentos resetados que esta configurando.



### **Pontos de atenção:**

\- Mikrotik reiniciado sem configuração default não tem IP precisa de acesso por MAC, tem que estar na mesma bridge.
\- Alguns equipamentos ao reiniciar tem servidor DHCP que pode propagar para rede corporativa(link).
\- O Equipamento configurado por um técnico não pode ser visível para outro ou na rede corporativa.
\- Alguns equipamentos precisam de DHCP client, mas não devem se misturar a rede corporativa.



### **Solução:**

1) Trabalhar em bridge para permitir o acesso ao mikrotik por MAC e ao DHCP da empresa no PC do técnico.
2) Adicionar vários IPs diferentes na bridge para comunicação com cada rede que os equipamentos usam.
3) Fazer SRC-NAT do que vai para os equipamentos pois eles não tem gateway default.
4) Fazer redirect na Bridge quando o destino são as redes dos equipamentos, assim usando RB como gateway.
5) Filtrar toda comunicação entre empresa e equipamentos.
6) Filtrar DHCP Server dos equipamentos para o PC do técnico.
7) Criar DHCP Server da RB que é usada para alguns equipamentos.
8) Filtrar DHCP Server da RB que é usada para alguns equipamentos, para não atender PC do técnico e rede corporativa.
9) Configurações Básicas para acesso a RB.




### **Passo a passo:**

**1) Trabalhar em bridge para permitir o acesso ao mikrotik por MAC e ao DHCP da empresa no PC do técnico.**
/interface bridge
add name=bridge1
/interface ethernet
set [ find default-name=ether1 ] name=ether1-Link
set [ find default-name=ether2 ] name=ether2-Notebook poe-out=off
set [ find default-name=ether3 ] poe-out=off
set [ find default-name=ether4 ] poe-out=off
/interface bridge port
add bridge=bridge1 interface=ether2-Notebook
add bridge=bridge1 interface=ether3
add bridge=bridge1 interface=ether4
add bridge=bridge1 interface=ether5
add bridge=bridge1 interface=ether1-Link
add bridge=bridge1

**2) Adicionar vários  IPs diferentes na bridge para comunicação com cada rede que os equipamentos usam.**
/ip address
add address=10.0.0.2/24 interface=ether3 network=10.0.0.0
add address=192.168.1.2/24 interface=ether3 network=192.168.1.0
add address=192.168.2.2/24 interface=ether3 network=192.168.2.0
add address=192.168.88.2/24 interface=ether3 network=192.168.88.0
add address=192.168.100.2/24 interface=ether3 network=192.168.100.0
add address=192.168.13.1/24 interface=bridge1 network=192.168.13.0

**3) Fazer SRC-NAT do que vai para os equipamentos  pois eles não tem gateway default.**
/ip firewall nat
add action=masquerade chain=srcnat dst-address=10.0.0.0/24
add action=masquerade chain=srcnat dst-address=192.168.1.0/24
add action=masquerade chain=srcnat dst-address=192.168.2.0/24
add action=masquerade chain=srcnat dst-address=192.168.88.0/24
add action=masquerade chain=srcnat dst-address=192.168.100.0/24
add action=masquerade chain=srcnat src-address=192.168.13.0/24

**4) Fazer redirect na Bridge quando o destino são as redes dos equipamentos, assim usando RB como gateway.**
/interface bridge nat
add action=redirect chain=dstnat dst-address=10.0.0.0/24 mac-protocol=ip
add action=redirect chain=dstnat dst-address=192.168.1.0/24 mac-protocol=ip
add action=redirect chain=dstnat dst-address=192.168.2.0/24 mac-protocol=ip
add action=redirect chain=dstnat dst-address=192.168.88.0/24 mac-protocol=ip
add action=redirect chain=dstnat dst-address=192.168.100.0/24 mac-protocol=ip
add action=redirect chain=dstnat dst-address=192.168.13.0/24 mac-protocol=ip

**5) Filtrar toda comunicação entre empresa e equipamentos.**
/interface bridge filter
add action=accept chain=forward in-interface=ether2-Notebook out-interface=ether1-Link
add action=accept chain=forward in-interface=ether1-Link out-interface=ether2-Notebook
add action=drop chain=forward out-interface=ether1-Link
add action=drop chain=forward in-interface=ether1-Link

**6) Filtrar DHCP Server dos equipamentos para o PC do técnico.**
/interface bridge filter
add action=drop chain=forward comment=\
    "Oferta DHCP - Colocar depois de permitir a rede da empresa" dst-port=68,67 \
    ip-protocol=udp mac-protocol=ip out-interface=ether2-Notebook
add action=drop chain=forward comment=\
    "Requisi\E7\E3o DHCP - Colocar depois de permitir a rede da empresa" \
    dst-port=67,68 in-interface=ether2-Notebook ip-protocol=udp mac-protocol=ip

**7) Criar DHCP Server da RB que é usada para alguns equipamentos.**
/ip pool
add name=dhcp_pool1 ranges=192.168.13.2-192.168.13.254
/ip dhcp-server network
add address=192.168.13.0/24 gateway=192.168.13.1
/ip dhcp-server
add address-pool=dhcp_pool1 disabled=no interface=bridge1 name=dhcp1

**8) Filtrar DHCP Server da RB que é usada para alguns equipamentos, para não atender PC do técnico e rede corporativa.**
/interface bridge filter
add action=drop chain=output comment="Oferta DHCP" dst-port=68 ip-protocol=\
    udp mac-protocol=ip out-interface=ether1-Link
add action=drop chain=output comment="Oferta DHCP" dst-port=68 ip-protocol=\
    udp mac-protocol=ip out-interface=ether2-Notebook
add action=drop chain=input comment="Requisi\E7\E3o DHCP" dst-port=67 \
    in-interface=ether1-Link ip-protocol=udp mac-protocol=ip
add action=drop chain=input comment="Requisi\E7\E3o DHCP" dst-port=67 \
    in-interface=ether2-Notebook ip-protocol=udp mac-protocol=ip

**9) Configurações Básicas para acesso a RB.**
/ip dhcp-client
add dhcp-options=hostname,clientid disabled=no interface=ether1-Link
/system identity
set name="MikroTik - Suporte1"
/ip dns
set servers=8.8.8.8,8.8.4.4
/user set admin password=********

---
---

Usando uma RB com 2 portas ethernet e 1 wireless.
Consegui inserir os clientes da wireless, como se fossem o PC da rede cabeada.

Acho que todos são responsáveis pelo que fazem, criei isso com o objetivo de fazer a transparência, mas teria me sido útil no passado.
Isso foi inspirado em um vídeo do MUM onde o palestrante faz mil coisas com um mAP.

Tentativas de me achar:


1) Tamanho e uptime do cabo
Existem equipamentos que para efeito de teste medem o cabo e dizem o tamanho de cada par. Se você colocar um cabo novo ligado a esse equipamento e o administrador testar novamente e tiver o resultado antigo vai perceber.
Solução:
\- Colocar a RB próxima ao lado que não deve ter esse controle, mantendo o cabo original saindo do equipamento com esse controle.
\- Usar um cabo do mesmo tamanho para o outro lado (os pares podem ter diferença de tamanho o que entregaria você).
\- Ligar os cabos da LAN e WAN ao mesmo tempo na RB depois de ligada.
Comentário:
Nem nos servidores do pentágono deve ter essa preocupação


2) TTL
Cada sistema operacional tem um valor de TTL na origem do pedido:
Windows 128
Linux 64
Quando passa por um roteador esse valor é reduzido em 1, por tanto você seria percebido se colocasse um roteador a mais.
Solução:
\- Saber qual é o sistema de cada lado e setar novo valor para o TTL, novo pois você poderia ter equipamentos na rede Wi-Fi diferentes com os da rede LAN.
Comentário:
Diversos provedores já no passado pensaram em bloquear o usuário de adicionar roteador para ele não dividir a internet, em redes corporativas nunca vi esse controle. Vou mostrar a solução.


3) Pacote ARP
O ARP pergunta o MAC de alguém e conta o seu próprio MAC e IP para facilitar a resposta.
Dentro do protocolo ARP esta o IP e esse valor não pode ser alterado.
Mas em rede local IP não é usado pra quase nada.
Solução:
\- Desabilitar o ARP e inserir na tabela ARP entradas estáticas.
Comentário:
O problema é pior que ser achado, é achar um IP que não seja de outro equipamento da rede. Vou mostrar a solução.


4) DNS
Em uma rede corporativa solicitações de site externos não costumam ser feitas ao DNS interno.
Isso em teoria poderia ser detectado ou o DNS poderia responder um site interno de bloqueio.
Não deve existir rota em redes internas para DNSs externos como 8.8.8.8, então precisa saber o DNS interno.
Solução:
\- Usar um Modem 4G USB e acessar a internet e DNS pelo 4G
\- Colocar um firewall dropando DNS pra rede corporativa.
\- Adicionar entradas estáticas no arquivo host do PC usado na Wi-Fi. SIM o Windows também tem arquivo host, como no linux.
\- Usar um Modem 4G USB e acessar a internet e DNS pelo 4G
\- Cadastrar o DNS interno como segunda opção a ser usado, sabendo dos riscos.
Comentário:
Ser pego aqui é o de menos o questão é resposta errada. E a dificuldade de saber o DNS interno a usar.


5) Outros protocolos e excesso de trafego
Quando você liga um PC ou celular a rede diversos programas em background tentaram enviar e receber dados, isso pode te entregar.
Solução:
\- Adicionar regras bem restritivas ao firewall, trabalhar com lista branca.
Comentário:
Como isso vai depender muito do local e lista necessária não vou abordar aqui.


6) MAC
Switchs de datacenters costumam desligar a porta se outro MAC for conectado a ela como medida de segurança.
Solução:
\- Clonar o MAC do PC para o Switch.
\- Clonar o MAC do Switch para o PC.
Comentário:
Eu já derrubei uma porta sem querer ao fazer o sniffer de um servidor. Isso com certeza gerou um log. Mas logs só são olhados quando um problema precisa ser analisado.
Eu desliguei e religuei o switch "por acidente" a porta dele voltou liguei o servidor novamente, ninguém foi demitido a analise do sniffer ajudou a resolver o problema e ainda teve comoração no final do dia.


7) IPSec
Se toda rede trabalhar com IPSec ai não tem como entrar ou ler nada.
Sem solução.


Eu adicionaria a essa solução um Modem 4G USB com isso:
\- Colocaria o DNS público
\- Host da rede no arquivo hosts
\- rota default para o Modem
\- rotas necessárias para a rede corporativa
Com isso você pode trabalhar do seu notebook em um cliente usando a internet e a rede dele ao mesmo tempo, como se estivesse usando o PC que lhe foi dado para trabalhar.


Bom eu vou mostrar o que fiz infelizmente tudo manual agradeceria se alguém pensasse em script pra pegar as informações e automatizar a configuração.


Cenário do Lab:
PC com IP 192.168.55.254 MAC E4:8D:8C:65:B8:A9 e TTL 128
Gateway com IP 192.168.55.1 MAC 4C:5E:0C:71:5A:67 e TTL 64
Para facilitar criei um IP fictício 10.100.100.0/24 que não deve corresponder ao da rede que vai ser usada.

Como funcionou a transparência
Foi mais simples que pensava
Fiz NAT na Bridge para os MACs
Fiz NAT no firewall para os IPs
Fiz o trafego da bridge passar pelo firewall para permitir recuperar os pacotes recebidos com origem em NAT de saída e também interceptar algum pacote como fiz com o Winbox.
Eu me expus colocando a interceptação de pacotes para a porta do Winbox, fazendo parecer que o PC tem a porta do Winbox aberta, também permitindo acessar a RB de fora do Wi-Fi.


A parte comum:
`
/interface ethernet
set [ find default-name=ether1 ] name=ether-WAN
set [ find default-name=ether2 ] name=ether-LAN
/interface bridge
add arp=disabled name=bridge-Invisible
/interface bridge port
add bridge=bridge-Invisible interface=ether-LAN
add bridge=bridge-Invisible interface=ether-WAN
/interface bridge settings
set use-ip-firewall=yes
/ip neighbor discovery
set ether-LAN discover=no
set ether-WAN discover=no
set bridge-Invisible discover=no
/ip address
add address=10.100.100.2/24 interface=ether-LAN network=10.100.100.0
/ip route
add distance=1 gateway=10.100.100.1
`


A parte onde os TTLs, MACs e IPs da rede devem ser colocados com atenção:
`
/ip firewall mangle
add action=change-ttl chain=postrouting dst-address=192.168.55.254 new-ttl=set:64 out-interface=bridge-invisivel passthrough=yes
add action=change-ttl chain=postrouting new-ttl=set:128 out-interface=bridge-invisivel passthrough=yes


/ip arp
add address=10.100.100.1 comment=GATEWAY interface=bridge-Invisible mac-address=4C:5E:0C:71:5A:67
add address=10.100.100.254 comment=PC interface=bridge-Invisible mac-address=E4:8D:8C:65:B8:A9
/interface bridge nat
add action=src-nat chain=srcnat out-interface=ether-WAN to-src-mac-address=E4:8D:8C:65:B8:A9
add action=src-nat chain=srcnat out-interface=ether-LAN to-src-mac-address=4C:5E:0C:71:5A:67
/ip firewall nat
add action=src-nat chain=srcnat out-interface=bridge-Invisible to-addresses=192.168.55.1 dst-address=192.168.55.254
add action=src-nat chain=srcnat out-interface=bridge-Invisible to-addresses=192.168.55.254
add action=redirect chain=dstnat dst-port=8291 dst-address=192.168.55.254 in-interface=bridge-Invisible protocol=tcp
/ip route
add distance=1 gateway=10.100.100.254 dst-address=192.168.55.254/32
`


Eu criei rapidamente uma rede pois neste local de lab a internet era liberada sem proxy.
`
/interface wireless
set [ find default-name=wlan1 ] band=2ghz-b/g/n disabled=no mode=ap-bridge
/ip address
add address=192.168.56.1/24 interface=wlan1 network=192.168.56.0
/ip pool
add name=dhcp_pool0 ranges=192.168.56.10-192.168.56.254
/ip dhcp-server
add address-pool=dhcp_pool0 disabled=no interface=wlan1 name=dhcp1
/ip dhcp-server network
add address=192.168.56.0/24 gateway=192.168.56.1
/ip dns
set servers=8.8.8.8,8.8.4.4
`

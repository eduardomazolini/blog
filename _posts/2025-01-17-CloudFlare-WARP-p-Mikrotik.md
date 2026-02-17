---
---

A CloudFlare oferece o serviço o serviço [Zero Trust](https://one.dash.cloudflare.com) que é gratuito até certo ponto e muito útil.

O que é o Zero Trust, como o nome diz é não confiar em ninguém então o usuário tem que estar em uma VPN e os Servidores também, as redes também.

Ela também oferece um serviço de VPN WARP que no fundo é uma VPN WireGuard.

Esse serviço ele tem 3 formas:

1) Versão para usuário simples ele não precisa nem de registro.

[https://one.one.one.one/ ](https://one.one.one.one/)

<https://github.com/ViRb3/wgcf>

Não precisa de autenticação então é fácil de usar em um roteador mikrotik

endpoint:

    engage.cloudflareclient.com

        ipv4:162.159.192.1 





2) Versão Zero Trust para usuários (time) 

<https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/> 


<https://github.com/poscat0x04/wgcf-teams>

Precisa autenticar a cada 24h pode ser feito com Service Token mas mesmo assim é chato o processo teria que criar uma automação, dentro do mikrotik fica dificil.


[Como usar o Service Token](https://developers.cloudflare.com/cloudflare-one/identity/service-tokens/) 


 

3) Versão Zero Trust para sites (gateway) (escritórios)

<https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/private-net/warp-connector/> 


<https://github.com/AnimMouse/wgcf-connector/>

Esse que eu tive dificuldade de achava e é realmente útil.

Queria muito agradecer a grande diferencial foi a contribuição desse Anim Mouse.

 

Tipos de acesso

WARP User -> Internet 

WARP Site -> Internet


WARP User -> WARP Site

WARP Site -> WARP Site

 

O acesso do tipo **Internet - > site** precisa do **Cloudflared** (CloudFlare Túnel).

<https://developers.cloudflare.com/cloudflare-one/connections/connect-networks/>





O acesso do tipo **WARP XXX - > WARP Site** precisa que o cliente envie IPs privados para a CloudFlare para isso veja a configuração a baixo e **remova os IPs privados que estão no site remoto** da lista ou crie sua configuração como necessário.


<https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/configure-warp/route-traffic/split-tunnels/#remove-a-route>

Também vai ser preciso criar a regra de roteamento informando que rede esta atrás de qual **WARP Conector** na configuração do túnel. 





**!ATENÇÃO com endpoint!**

**endpoint** :
ipv4: 162.159.193.1  **
**

O**endpoint** correto para o serviço **Zero Trust** é  19**3** 162.159.193.1


Eu não achei um lugar oficial para confirmar o número exato a não ser o link a baixo e comentários no github.

<https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/deployment/firewall/>

<https://github.com/poscat0x04/wgcf-teams/issues/5>

No cliente WARP é possível ver o valor correto, escrevi os comandos que podem ser úteis.

<https://blog.mazolini.com.br/2025/01/extraindo-configuracao-do-cliente-warp.html> 








### Configurando o Mikrotik para usar WARP como uma VPN Wireguard


As ferramentas acima dos links do github vão gerar um texto que pode ser importado em alguns clientes wireguard, mas não no Mikrotik.

Também é possível extrair os valores do seu cliente linux, [AQUI](https://blog.mazolini.com.br/2025/01/extraindo-configuracao-do-cliente-warp.html) esta a lista de comandos. 


Aqui vou mostrar como usar o texto para configurar o básico do mikrotik.

Como disse o básico só o que envolve criar a interface.




Arquivo wireguard de **exemplo** use o gerado por **você**!!!


> # routing-id: 0x000000
> [Interface]
> PrivateKey = chave+privada
> Address = 2606:4700:110:86cb:4b9d:6889:fe5e:dfee/128
> Address = 100.96.0.1/32
> DNS = 1.1.1.1
> DNS = 2606:4700:4700::1111
> MTU = 1420
> 
> [Peer]
> PublicKey = bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo=
> AllowedIPs = ::/0
> AllowedIPs = 0.0.0.0/0
> Endpoint = engage.cloudflareclient.com:2408
> 
> 

Criar a interface wireguard

Substitua a chave+privada 


> /interface wireguard add mtu=1420 name=Cloudflare-WARP private-key="chave+privada"




Criar a endpoint do wireguard

Observe se a chave publica não mudou mas parece sempre ser a mesma. 


> /interface wireguard peers add allowed-address=0.0.0.0/0,::/0 endpoint-address=162.159.193.1 endpoint-port=2408 interface=Cloudflare-WARP name=Cloudflare-PoP persistent-keepalive=2m public-key="bmXOC+F1FxEMF9dyiK2H5/1SUtzH0JuVo51h2wPfgyo="
> 




Crie os IPs nas interfaces

Muita atenção pq esse valores mudam

> /ip address add address=100.96.0.1/12 interface=Cloudflare-WARP
> /ipv6 address add address=2606:4700:110:8ced:11b5:d064:abc:ee89/128 interface=Cloudflare-WARP
> 
> 

Crie o NAT de saída

Atenção com o IP usado, poderia ser um masquerad mas sabemos o IP então não tem motivo para consumir processamento da RB atoa.


Lembre que em algumas situações esse nat não será necessário. Para acesso **site-to-site** não precisa do NAT, mas ai se trata de uma configuração mais avançada vc mesmo pense quais serão as regras para não fazer o NAT.


> /ip firewall nat add action=src-nat chain=srcnat out-interface=Cloudflare-WARP to-addresses=100.96.0.1




Crie a rota de saída

Lembre que é uma VPN então vc não pode substituir rota de saída padrão simplesmente. Você deve saber o que fazer aqui então só vou descrever algumas opções.




1ª opção


Criar a rota para o endpoint em cima da rota padrão existente

    Lembre de editar o seu gatway, o meu no exemplo é 192.168.0.1, troque esse valor. 


> /ip route
> add dst-address=162.159.193.0/24 gateway=192.168.0.1
> 

Subir a distancia da rota padrão

Criar uma nova rota padrão pela interface use o nome da interface (igual PPPoE)

2ª opção

Crie uma rota em tabela de roteamento alternativa

 

No firewall marque as conexões para usar a nova rota na tabela de roteamento alternativa.

3ª opção


Crie uma rota em tabela de roteamento alternativa

> /ip route
> add dst-address=0.0.0.0/0 gateway=Cloudflare-WARP routing-table=cloudFlare
> 

 

Selecione a tabela de roteamento com base no ip de origem

    No exemplo o range do Pool DHCP é 192.18.10.0/24 


> /routing table
> add fib name=cloudFlare
> /routing rule
> add action=lookup disabled=no src-address=192.168.10.0/24 table=cloudFlare

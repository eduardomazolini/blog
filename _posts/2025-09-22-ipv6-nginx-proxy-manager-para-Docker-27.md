Eu preciso encaminhar acesso ipv6 para alguns servidores.
Depois de atribuir o ip ao servidor host o encaminhamento de porta do ipv6 não funcionava.

Pode ser que vc queira extender a rede ipv6 até o seus container não é o meu caso eu preciso que o Docker faça o NAT e encaminhe a porta para o container. Mas se vc tiver ipv6 pra estender a rede só de declarar o ipv6 não ULA ele ira funcionar se vc habilitar o roteamento ipv6 no linux.

BUG o Docker não é inteligente para criar varias redes só com uma declaração de range base /48 com size /64, percebi isso quando fui criar a segunda rede. Então vc tem que criar varias entradas, espero que isso mude logo.

O parâmetro ip6tables, que faz o nat, só funciona com experimental.

Isso tudo eu estava usando versão:

```
docker --version
Docker version 26.1.2, build 211e74b

docker --version
Docker version 24.0.4, build 3713ee1
```

Para versão maior que v28 :
```
{
  "ipv6": true,
  "ip6tables": true
}
```
Atenção pq algumas portas como a 80 funcionam sem o ip6tables true, o que me fez perder 2 dias procurando um firewall na port 443 que não existia.
Se funciona para 80 pq não funcionaria para 443?
Pois é! Só sei que foi assim.

Então minha solução foi criar o arquivo /etc/docker/daemon.json para versões anteriores:
 
```
{
  "ipv6": true,
  "fixed-cidr-v6": "fd00:2705:0001::/64",
  "experimental": true,
  "ip6tables": true,
  "default-address-pools": [
	{
	  "base": "172.20.0.0/16",
	  "size": 24
	},
	{
	  "base": "fd00:2705:0002::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0003::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0004::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0005::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0006::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0007::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0008::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0009::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0010::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0011::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0012::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0013::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0014::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0015::/48",
	  "size": 64
	},
	{
	  "base": "fd00:2705:0016::/48",
	  "size": 64
	}
  ]
}
```
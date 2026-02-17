---
tags: [Mikrotik]
---

Infelizmente ao contrario do Speedy (ADSL) trocar de IP no Virtua(serviço da NET) é mais complicado.

No ADSL basta cancelar a conexão e discar novamente.

No net um truque manual é mudar o mac e reiniciar o modem.

Mas como não tenho como reiniciar o modem automaticamente estou propondo um outro caminho alternativo.

Se alguém tiver outro truque por favor me avise.

O Net Virtua oferece 2 ips validos, pelo menos aqui em casa. O truque é usar estes IPs.

Descobri mudando o MAC antes de desligar o modem.

Para ter 2 MACs usando o Mikrotik tive que usar um cabo de rede para fazer um loop.

Bridge – internet 1 (MAC1)

Porta1 – Modem Virtua

Porta2 – Cabo de Loop

Bridge – internet2 (MAC2)

Porta3 – Cabo de Loop





Usei umas regras no firewall para as conexões de estado “new” criar um connection mark e depois do connection mark o route mark. (não é o foco deste post.)

Mas com IP dinâmico 2 interfaces podiam cair hora em redes distintas hora na mesma rede.

Precisei criar um script pra definir o gateway para conexão com route mark.

Segue o script que usei para fazer isso. Tem variáveis a mais não usadas é que acabo usando em outros scripts.

Em casa meu router com a internet é um RB750G o wireless meu queimou era um Links WRT54GS, o atual tenho ate vergonha de contar qual é.

Em casa para usar os 2 IPs tive que ter 2 MACs seguidos. Por que isso funcionou? Não sei mesmo, “Só sei que foi assim.”

Script:

```
:global lastip1
:global lastip2
:global lastativo
:global interfaceAtiva
:global gateway1
:global gateway2
:global addressAtivo
:global interface1 "internet1"
:global addressMasc1 [/ip address get [find interface=$interface1] address]
:global address1 [:pick $addressMasc1 begin=0 end=[:find $addressMasc1 "/" -1]]
:global network1 [/ip address get [find interface=$interface1] network]
:global Masc1 [:pick $addressMasc1 begin=[:find $addressMasc1 "/" -1] end=[:len $addressMasc1]]
:global interface2 "internet2"
:global addressMasc2 [/ip address get [find interface=$interface2] address]
:global address2 [:pick $addressMasc2 begin=0 end=[:find $addressMasc2 "/" -1]]
:global network2 [/ip address get [find interface=$interface2] network]
:global Masc2 [:pick $addressMasc2 begin=[:find $addressMasc2 "/" -1] end=[:len $addressMasc2]]
:if ($network1=$network2) do={
:set addressAtivo [/ip route get [find dst-address="$network1"."$Masc1"] pref-src]
:set gateway1 [/ip route get [find active=no dynamic=yes dst-address=0.0.0.0/0] gateway]
:set gateway2 $gateway1
:if ($addressAtivo=$address1) do={
:set interfaceAtiva $interface1
} else={
:set interfaceAtiva $interface2
}
} else={
:set interfaceAtiva [:pick [:tostr [/ip route get [find active=yes dynamic=yes dst-address=0.0.0.0/0] gateway-status]] [:find [:tostr [/ip route get [find active=yes dynamic=yes dst-address=0.0.0.0/0] gateway-status]] "internet" -1] [:len [:tostr [/ip route get [find active=yes dynamic=yes dst-address=0.0.0.0/0] gateway-status]]]]
:if ($interfaceAtiva=$interface1) do={
:set gateway1 [/ip route get [find active=yes dynamic=yes dst-address=0.0.0.0/0] gateway]
:set gateway2 [/ip route get [find active=no dynamic=yes dst-address=0.0.0.0/0] gateway]
} else={
:set gateway2 [/ip route get [find active=yes dynamic=yes dst-address=0.0.0.0/0] gateway]
:set gateway1 [/ip route get [find active=no dynamic=yes dst-address=0.0.0.0/0] gateway]
}
}

:if (!(($lastativo=$interfaceAtiva)&&($lastip1=$address1)&&($lastip2=$address2))) do={
/ip route remove [find routing-mark="rota2"]
:if ($interfaceAtiva=$interface1) do={
/ip route add dst-address=0.0.0.0/0 routing-mark=rota2 pref-src=$address2 gateway=$gateway2
} else={
/ip route add dst-address=0.0.0.0/0 routing-mark=rota2 pref-src=$address1 gateway=$gateway1
}
}

:if (!(($lastativo=$interfaceAtiva)&&($lastip1=$address1)&&($lastip2=$address2))) do={
:log info "atualizado"
}
set lastip1 $address1
set lastip2 $address2
set lastativo $interfaceAtiva
```

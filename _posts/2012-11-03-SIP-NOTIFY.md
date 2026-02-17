---
---

Eu fiz isso em 04/08/2011 mas só agora tive tempo para publicar aqui, mandei e-mail pra lista do asterisk na época.
Eu tive muitos aparelhos que precisava atualizar com provisionamento. O que me perguntava era como fazer isso tudo de uma só vez.
Então um colega da lista de asterisk me apresentou o netcat para um outro fim.
Eu teste o notify do asterisk e sniffei a mensagem, então fui removendo itens para deixa-la mais genérica e com menor tamanho, para minha surpresa o telefone que estava usando não validava nenhum dado.
Usando essa mensagem genérica e o ip de broadcast eu resetei todos os aparelhos da mesma vlan que estava.

Veja a receita de bolo:

1) Baixe o netcat da internet (para Windows no meu caso).

http://www.downloadnetcat.com/nc11nt.zip

2) Crie o arquivo notify.txt com o seguinte texto:

```
NOTIFY sip:0.0.0.0 SIP/2.0
Via: SIP/2.0/UDP 0.0.0.0:5060
From: "U" <sip:U@0.0.0.0>
To:
Call-ID: 0@0.0.0.0
CSeq: 102 NOTIFY
Event: check-sync;reboot=true
Content-Length: 0
```

3) Digite:
```
nc -u 255.255.255.255 < notify.txt
```

---
tags: [asterisk]
---

Pra criar um tronco de entrada e saída no elastix, na tela do tronco preencha o seguinte:
```
Trunk Name: [LOGIN]

Peer Details:
host=dynamic
username=[LOGIN]
secret=[Senha]
type=friend
context=from-trunk
```

No SPA3102 na aba PSTN Line
```
Proxy: [IP do Elastix]
Outbound Proxy: [Sem nada]
Use Outbound Proxy: no
Register: yes

Display Name: [Sem nada]
User ID: [Login]
Password: [Senha]
Use Auth ID: no
Auth ID: [Sem nada]
```

```
PSTN-To-VoIP Gateway Setup
PSTN Caller Default DP: 1
Dial Plan 1: "(<:[ramal]>)"
```

---
tags: [1.4.21, 1.4.24.1, asterisk, elastix, segurança]
---

Hoje na lista do Asterisk foi discutida uma vulnerabilidade do Asterisk e uma solução.
Eu tentei aplicar a solução e vi que ela só era eficiente em versões superiores a 1.4.24.1
Eu uso a versão 1.2.21.2

Obrigado aos participantes da lista.

A vulnerabilidade e que um atacante conseguiu testar a existência de 60 ramais por segundo.
Depois de identificar que o ramal existe ele passa a tentar descobrir a senha.

Soluções:
1) <http://www.voipexperts.com.br/tutoriais-sobre-asterisk-e-voip/seguranca-no-asterisk>
2) http://downloads.asterisk.org/pub/security/AST-2009-003.html
3) http://www.voip-info.org/wiki/view/Fail2Ban+(with+iptables)+And+Asterisk

Eu apliquei o indicado na 1 e atualizei conforme indicado na 2.
A 3ª solução eu vou estudar e assim que aplicar eu posto novidades.

Bom mãos a obra!

Se vc tem asterisk 1.4 mas inferior a 1.4.24.1 primeiro vamos atualizar ele.

```bash
cd /tmp
wget http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-1.4.26.2.tar.gz
```

Descompactei
```bash
tar -xvf asterisk-1.4.26.2.tar.gz
```

Compilei
```bash
cd asterisk-1.4.26.2
./configure
make
```

Copiei só o arquivo modificado pra solucionar o problema.

```bash
cp /tmp/asterisk-1.4.26.2/channels/chan_sip.so /usr/lib/asterisk/modules/chan_sip.so
```


Agora vamos pedir pra ele se comportar igual com ramais existentes e ramais não existentes.

```bash
cd /etc/asterisk
echo alwaysauthreject=yes>> sip_general_custom.conf
```

Isso adicionou o ```alwaysauthreject=yes``` no arquivo ```sip_general_custom.conf```

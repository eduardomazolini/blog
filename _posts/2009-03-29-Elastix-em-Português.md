---
tags: [asterisk]
---

O Pessoal do [DISC-OS](http://sourceforge.net/projects/disc-os/files/Disc-OS%20Sounds/1.0-RELEASE/Disc-OS-Sounds-1.0-pt_BR.tar.gz/download) liberou já a muito tempo as gravações do asterisk em português.
Baixe o RPM pra dentro do elastix e instale com o comando.
```
rpm -ivh --nodeps Disc-OS-Sounds-1.0-pt_BR.rpm
```

Depois altere o arquivo /etc/asterisk/sip_general_custom.conf e coloque a seguinte linha:
```
language=pt_BR
```

Use o comando a seguir pra entrar no editor vi: vi /etc/asterisk/sip_general_custom.conf
Digite i para entrar em modo "insert"
Digite o texto: ```language=pt_BR```
```digite <esc>:wq para salvar```
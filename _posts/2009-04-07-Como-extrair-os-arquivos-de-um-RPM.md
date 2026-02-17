---
tags: [linux]
---

Dica rápida pra não perder.
Estava precisando só de um arquivo que vinha no rpm. Mas já tinha o asterisk instalado customizado. Então precisei dessa dica pra poder pegar o arquivo.
Se alguém sabe um modo melhor me avisa.

rpm2cpio asterisk-1.4.21.2-2.i386.rpm | cpio -idmv

---
tags: [asterisk]
---
Eu não conseguia completar ligações no SIP da Vivo para celulares iPhone.

Consegui resolver para mim e fiz pull request no projeto oficial.

O problema é o maxptime fixo até o momento em 150 que tem que ser multiplo do tamanho do pacote enviado, normalmente 20ms. Uma outra solução seria reduzir para 10ms

O que sugeri foi alterar o valor para 140ms que é multiplo de 20ms e 10ms

https://github.com/asterisk/testsuite/issues/15
https://github.com/asterisk/testsuite/commit/2acead229ff85003ad63cd8e2e2ed66d66ef9bd9  
https://github.com/asterisk/asterisk/issues/260
https://github.com/asterisk/asterisk/commit/91e368c4858bd578b07a70f98f961f3f85e41195
https://github.com/asterisk/asterisk/commits?author=eduardomazolini

Mas como recompilar o asterisk atual (2023) do freePBX

yum install git
cd /usr/src/
git clone --depth 1 --branch 16.30.0 https://github.com/asterisk/asterisk.git asterisk-16.30.0
vi /usr/src/asterisk-16.30.0/main/codec_builtin.c

Editei todos os valores ".maximum_ms" impar para 10 a menos.

yum install bzip2
yum install openssl
yum install openssl-devel
yum install patch
yum install libedit
yum install libedit-devel
yum install uuid
yum install uuid-devel
yum install libuuid-devel
yum install jansson
yum install jansson-devel
yum install libxml2-devel
yum install libxml2
yum install sqlite
yum install libsqlite3x
yum install libsqlite3x-devel
./configure
make
cp  usr/src/asterisk-16.30.0/main/asterisk /usr/sbin/asterisk

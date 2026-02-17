---
---

Consegui colocar a radio no meu DISC-OS
Sei que isso vai consumir banda mas valeu pela experiência.

```musiconhold.conf```

```ini
[default] 
mode=custom 
application=/usr/local/bin/mpg123 -q -r 8000 -f 8192 -s --mono http://servidor:porta/
```



Depois da palavra **mono** vem o endereço exemplo http://servidor:porta/
Este endereço esta dentro dos arquivos como listen.pls, ouvir.m3u, real.ram no site das radios.

Para instalar o **mpg123** :

``` bash
wget http://ufpr.dl.sourceforge.net/sourceforge/mpg123/mpg123-1.4.2.tar.gz 
tar -vzxf mpg123-1.4.2.tar.gz
cd mpg123-1.4.2
./configure
make
make install
```

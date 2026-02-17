Infelizmente a Epson não tem drive para ARM nem para sistema de 32bits i386. Pq eu queria usar minha OrangePi ou RapsbarryPi como servidor de impressão. Também tentei deixar um netbook Atom antigo que é 32Bits.

No fim tive que deixar um notebook Positivo de 32G de disco e 1Gb de RAM.

```
wget https://download3.ebz.epson.net/dsc/f/03/00/15/64/76/69bb3d019d2d4a6b1eeab2fbe4db5c081d2b6b86/epson-inkjet-printer-201312w_1.0.1-1_amd64.deb
```

apt install cups

apt install printer-driver-gutenprint printer-driver-foo2zjs printer-driver-ptouch ghostscript cups-filters libcupsimage2

apt install ./epson-inkjet-printer-201312w_1.0.1-1_amd64.deb

Esses pacotes acima resolvem erros como:

Filter failed

EPSON_L1800_Series: error while loading shared libraries: libcupsimage.so.2: cannot open shared object file: No such file or directory

PID 0000 (/usr/lib/cups/filter/gstoraster) exited with no errors. 

Para acessar remotamente edite:
/etc/cups/cupsd.conf

Comente:
```
Listen localhost:631
```

adicione:
Port 631

Procure os blocos <Location />, <Location /admin>, e <Location /admin/conf> e adicione as linhas abaixo dentro de cada bloco:

Allow @LOCAL

Ative o serviço:
sudo systemctl enable cups
sudo systemctl start cups

Se precisar reinicie o serviço:
sudo systemctl restart cups

Adicione seu usuário como autorizado:
sudo usermod -aG lpadmin $(whoami)

FONTE: https://download.ebz.epson.net/dsc/search/01/search/
O site da Epson em português não tem drive para Linux.

---
---

Tenho 2 servidores DELL e preciso olhar como esta a saúde do RAID e dos discos.

Baixei o STORCLI_SAS3.5_P36 de https://www.broadcom.com/support/download-search?dk=storcli

wget https://docs.broadcom.com/docs-and-downloads/host-bus-adapters/host-bus-adapters-common-files/sas_sata_nvme_12g_p36/STORCLI_SAS3.5_P36.zip 





descompactei e na pasta ubuntu tem um .deb

unzip STORCLI_SAS3.5_P36.zip 


cd STORCLI_SAS3.5_P36/univ_viva_cli_rel/Unified_storcli_all_os/Ubuntu/

dpkg -i storcli_007.3503.0000.0000_all.deb




Foi necessário criar um link simbolico para executar o comando de forma mais comoda.

ln -s /opt/MegaRAID/storcli/storcli64 /usr/local/bin/storcli





Alguns comandos uteis:

storcli show
storcli /c0/vall show
storcli /c0/eall/sall show
storcli /c0 show all


Para saber o nome do seu servidor também tem um comando interessante:

dmidecode -s system-product-name




Para saber detalhes dos discos físicos:

smartctl -a /dev/sda -d megaraid,0
smartctl -a /dev/sda -d megaraid,1
smartctl -a /dev/sda -d megaraid,2
smartctl -a /dev/sda -d megaraid,3


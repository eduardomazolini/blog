---
---

    Eu fui unir 2 proxmox em um cluster e cometi o erro de não fazer backup da pasta pve. Com isso perdi todas as maquinas do segundo servidor. Não os arquivos salvos na LVM, mas os .conf. As maquinas não pararam elas só sumiram da configuração. 

    Eu costumo fazer backup de tudo a cada 2 dias e os arquivos de configuração não são modificados com frequência então não precisava recuperar as maquinas com dados de 2 dias a trás só os arquivos de configuração para elas aparecerem novamente na configuração.

 

Para os VMs:



Eu copiei já descompactando o arquivo para minha maquina local. Lendo do meu nas e gravando já local eu otimizei a operação ganhando bastante tempo, pq fazia leitura continua em quanto em outro disco fazia a escrita continua.

Extrai a configuração para um arquivo e movi eles para a pasta correta. 

unzstd -o ~/vzdump-qemu-202.vma /mnt/pve/nfs-remoto/dump/vzdump-qemu-202-2025_11_28-00_49_09.vma.zst

vma config ~/vzdump-qemu-202.vma > 202.conf

rm ~/vzdump-qemu-202.vma

mv *.conf /etc/pve/nodes/servidor02/qemu-server/




Já os containers LXC a operação é um pouco diferente.

Confere se existe:
tar --use-compress-program=unzstd -tf /mnt/pve/nfs-remoto/dump/vzdump-lxc-120-2025_12_11-01_47_39.tar.zst | grep './etc/vzdump/pct.conf'

Extrai:
tar --use-compress-program=unzstd -xf /mnt/pve/nfs-remoto/dump/vzdump-lxc-120-2025_12_11-01_47_39.tar.zst ./etc/vzdump/pct.conf

Move:
mv ./etc/vzdump/pct.conf /etc/pve/nodes/servidor02/lxc/120.conf

Apaga a pasta:
Cuidado para não fazer esse comando da raiz e remover o /etc do seu servidor.
rm -Rf etc



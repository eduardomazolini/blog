---
tags: alpine, Proxmox
---
Eu já falei sobre o cloud-init mas usei ele no limite da GUI.
O que era extra eu fazia editando a imagem direto como o libguestfs.
Mas com alpine existe um problema em ativar a rede com DNS em quanto usa o libguestfs então não da pra atualizar ou baixar bibliotecas da rede.
Com isso aprendi um outro nivel do uso do cloud-init.

 Já tinha feito algo parecido com fedora core, mas não tinha reparado.

 Criei um arquivo snippets.

alpine-qga.yaml

#cloud-config
package_update: true
packages:
- qemu-guest-agent

runcmd:
- rc-update add qemu-guest-agent default
- rc-service qemu-guest-agent start
 

Então configuro ele na maquina, só é possível por linha de comando:
qm set <ID_VM> \--cicustom "user=nfs-remoto:snippets/alpine-qga.yaml"

 

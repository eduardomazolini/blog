---
order: 8
tags:
  - btrfs
---
# BTRFS - Snapshot

Se instalar usando opção sem LVM, criando a partição manualmente e escolha o / como BTRFS para facilitar.

## Referências

https://github.com/Antynea/grub-btrfs.git

https://github.com/wmutschl/timeshift-autosnap-apt.git

## Snapshot root

sudo mount /dev/vda4 /mnt
sudo mkdir -p /mnt/.snapshots
sudo btrfs subvolume snapshot -r /mnt/@rootfs /mnt/.snapshots/rootfs-inicial
sudo umount /mnt

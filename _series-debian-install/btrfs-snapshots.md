---
order: 8
---
# BTRFS - Snapshot

Se instalar usando opção sem LVM, criando a partição manualmente e escolha o / como btrfs para facilitar.

## Refencias

https://github.com/Antynea/grub-btrfs.git

https://github.com/wmutschl/timeshift-autosnap-apt.git

## Snapshot root

sudo mount /dev/vda4 /mnt
sudo mkdir -p /mnt/.snapshots
sudo btrfs subvolume snapshot -r /mnt/@rootfs /mnt/.snapshots/rootfs-inicial
sudo umount /mnt

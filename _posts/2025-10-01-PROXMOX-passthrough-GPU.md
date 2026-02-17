---
tags: [Proxmox]
---

No Servidor Proxmox

nano /etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet iommu=pt"

update-grub

nano /etc/modules-load.d/vfio.conf
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd

update-initramfs -u -k all

reboot

Para conferir: 

lsmod | grep vfio
dmesg | grep -e DMAR -e IOMMU -e AMD-Vi
pvesh get /nodes/$(hostname)/hardware/pci --pci-class-blacklist ""

Na VM
Configure os repositorios adicionais:
vi /etc/apt/sources.list
contrib non-free non-free-firmware

apt update
apt install nvidia-driver
apt install linux-headers-$(uname -r)





Problemas encontrados sem uma explicação:

\- Não use EFI em vez disso use:
bios: seabios

\- Especifique o Display como Standard VGA (std), normalmente uso vga: serial0
vga: std

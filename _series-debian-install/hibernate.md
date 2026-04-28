---
order: 5
---

## Hibernar

Para hibernar parece o initramfs precisa saber onde esta armazenado o dump da memoria RAM.
Esse espaço precisa ser **2/5 maior que a memória RAM** segundo o [wiki do Debian](https://wiki.debian.org/Hibernation#Suspend_and_hibernate_configuration_with_systemd_.2F_Debian_Buster_and_more_recent), pra quem tem pouca memória trabalhar com o dobro ou no minimo 50% a mais.

O Debian deixou a informação por padrão em `/etc/initramfs-tools/conf.d/resume`:
```
RESUME=/dev/mapper/vda3_crypt
```

>Tive já problema de usar hibernate quando o modo é BIOS  e ao usar vídeo Virtio.

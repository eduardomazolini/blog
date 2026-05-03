---
order: 7
---
# BTRFS - Particionando

Se instalar usando opção sem LVM, criando a partição manualmente e escolha o / como BTRFS para facilitar.

## Identificando

```
$ sudo btrfs subvolume list /
ID 256 gen 100 top level 5 path @rootfs

$ cat /etc/fstab 
# / was on /dev/vda4 during installation
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6 /               btrfs   defaults,subvol=@rootfs 0       0
# /boot was on /dev/vda2 during installation
UUID=5cd3c2e7-7af3-4ae8-bf26-999b3f9b0e2e /boot           ext4    defaults        0       2
# /boot/efi was on /dev/vda3 during installation
UUID=64C4-7A53  /boot/efi       vfat    umask=0077      0       1
# swap was on /dev/vda1 during installation
UUID=e1c75794-527d-4420-a04d-0cbd1fd63d4f none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0

$ lsblk -f
NAME   FSTYPE  FSVER            LABEL                 UUID                                 FSAVAIL FSUSE% MOUNTPOINTS
sr0    iso9660 Joliet Extension Debian 13.2.0 amd64 1 2025-11-15-12-52-21-00                              
vda                                                                                                       
├─vda1 swap    1                                      e1c75794-527d-4420-a04d-0cbd1fd63d4f                [SWAP]
├─vda2 ext4    1.0                                    5cd3c2e7-7af3-4ae8-bf26-999b3f9b0e2e    767M    10% /boot
├─vda3 vfat    FAT32                                  64C4-7A53                             478,2M     2% /boot/efi
└─vda4 btrfs                                          fbcfacaa-e0db-4ae3-87dd-4808332a27d6   48,2G    16% /
```

## Criando os volumes

``` bash
sudo mount /dev/vda4 /mnt

sudo btrfs subvolume create /mnt/@home
sudo btrfs subvolume create /mnt/@log
sudo btrfs subvolume create /mnt/@cache
sudo btrfs subvolume create /mnt/@tmp
```

## Verificado

``` bash
mount | grep /mnt

btrfs subvolume list /mnt
```

## Copiando os dados
``` bash
sudo mkdir -p /mnt/home
sudo mount -o subvol=@home /dev/vda4 /mnt/home
sudo rsync -aAX --progress /home/ /mnt/home/

sudo mkdir -p /mnt/log
sudo mount -o subvol=@log /dev/vda4 /mnt/log
sudo rsync -aAX /var/log/ /mnt/log/

sudo mkdir -p /mnt/cache
sudo mount -o subvol=@cache /dev/vda4 /mnt/cache
sudo rsync -aAX /var/cache/ /mnt/cache/
```

## Preparando a montagem

Decidindo a compressão

```
| Nível | Compressão      | CPU         | Uso recomendado           |
| ----- | --------------- | ----------- | ------------------------- |
| 1     | menor           | muito baixa | CPUs fracas               |
| 3     | **equilibrado** | baixa       | **desktop padrão**        |
| 5     | maior           | média       | notebooks modernos        |
| 7     | alta            | alta        | arquivos grandes          |
| 10+   | máxima          | muito alta  | não recomendado para root |

```

Editar o /etc/fstab
``` bash
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6  /          btrfs  subvol=@rootfs,compress=zstd:3,noatime 0 0
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6  /home      btrfs  subvol=@home,compress=zstd,noatime    0 0
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6  /var/log   btrfs  subvol=@log                           0 0
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6  /var/cache btrfs  subvol=@cache                         0 0
UUID=fbcfacaa-e0db-4ae3-87dd-4808332a27d6  /tmp       btrfs  subvol=@tmp,nosuid,nodev              0 0
```

Se quiser comprimir o que não foi comprimido pode usar o comando a baixo:

``` bash
sudo btrfs filesystem defragment -r -czstd /
```

Vamos limpar tudo agora
``` bash
sudo umount /mnt/home
sudo rm -R /mnt/home
sudo umount /mnt/log
sudo rm -R /mnt/log
sudo umount /mnt/cache
sudo rm -R /mnt/cache
sudo umount /mnt
```

## Mover os diretórios

``` bash
sudo mv /home /home.old
sudo mkdir /home
sudo mv /var/log /var/log.old
sudo mkdir /var/log
sudo mv /var/cache /var/cache.old
sudo mkdir /var/cache

sudo systemctl daemon-reload
sudo mount -a
```

## Verificar as permissões de /tmp

Tem que ser "drwxrwxrwt"

``` bash
$ ls -ld /tmp
drwxr-xr-x 1 root root 138 dez 17 12:18 /tmp
$ sudo chmod 1777 /tmp
$ ls -ld /tmp
drwxrwxrwt 1 root root 138 dez 17 12:18 /tmp
```

## Verificando a montargem e limpando

``` bash
findmnt -t btrfs
$ findmnt -t btrfs
TARGET       SOURCE              FSTYPE OPTIONS
/            /dev/vda4[/@rootfs] btrfs  rw,relatime,discard=async,space_cache=v2,subvolid=256,subvol=/@rootfs
├─/tmp       /dev/vda4[/@tmp]    btrfs  rw,nosuid,nodev,relatime,discard=async,space_cache=v2,subvolid=260,subvol=/@tmp
├─/home      /dev/vda4[/@home]   btrfs  rw,noatime,discard=async,space_cache=v2,subvolid=257,subvol=/@home
├─/var/log   /dev/vda4[/@log]    btrfs  rw,relatime,discard=async,space_cache=v2,subvolid=258,subvol=/@log
└─/var/cache /dev/vda4[/@cache]  btrfs  rw,relatime,discard=async,space_cache=v2,subvolid=259,subvol=/@cache
```


## Limpeza dos dados
Agora vamos apagar os dados antigos, que já foram copiados com rsync

``` bash
sudo rm -rf /home.old
sudo rm -rf /var/log.old
sudo rm -rf /var/cache.old
```

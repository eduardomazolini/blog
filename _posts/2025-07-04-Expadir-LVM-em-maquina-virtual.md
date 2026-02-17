### Para expandir o disco precisamos:

 1. Com fdisk
	* apagar a partição
	* Recriar a partição com o mesmo setor de inicio

> IMPORTANTE: Não apagar a "LVM2_member signature"

```
# fdisk /dev/vdb
Command (m for help): p
Disk /dev/vdb: 30 GiB, 32212254720 bytes, 62914560 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x986b9785

Device     Boot Start      End  Sectors Size Id Type
/dev/vdb1        2048 20971519 20969472  10G 8e Linux LVM

Command (m for help): d 1

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1):
First sector (2048-62914559, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-62914559, default 62914559):

Created a new partition 1 of type 'Linux' and of size 30 GiB.
Partition #1 contains a LVM2_member signature.

Do you want to remove the signature? [Y]es/[N]o: n

Command (m for help): w

The partition table has been altered.
Syncing disks.
```

2. Atualizar o PV:

```
# pvresize /dev/vdb1
Physical volume "/dev/vdb1" changed
1 physical volume(s) resized or updated / 0 physical volume(s) not resized
```

3. Expandir a LV:

```
# lvextend -l +100%FREE /dev/mediaVG/media
Size of logical volume mediaVG/media changed from 10.00 GiB (2560 extents) to 30.00 GiB (7680 extents).
Logical volume mediaVG/media successfully resized.
```

4. Expandir o sistema de arquivos ext3/ext4:

Para sistemas de arquivos ext3 ou ext4, você precisará usar o comando `resize2fs` para expandir o sistema de arquivos para usar todo o espaço disponível no LV.
```

 # resize2fs /dev/mediaVG/media
 resize2fs 1.45.5 (07-Jan-2020)
 Filesystem at /dev/mediaVG/media is mounted on /mnt/media; on-line resizing required
 old_desc_blocks = 2, new_desc_blocks = 4
 The filesystem on /dev/mediaVG/media is now 7864320 (4k) blocks long.
```

>IMPORTANTE: Se o sistema de arquivos estiver montado, o resize2fs fará a expansão online. Se não estiver montado, adicione a opção `-f` para forçar a verificação do sistema de arquivos antes de expandir.

### Verificando o espaço disponível após a expansão:
```

# df -h /mnt/media
Filesystem               Size  Used Avail Use% Mounted on
/dev/mapper/mediaVG-media   30G   8G   21G  28% /mnt/media
```

### Dica importante:

Se você estiver usando XFS como sistema de arquivos, o processo é diferente. Para XFS você deve usar:

``` 
# xfs_growfs /mnt/media
```

E o sistema de arquivos deve estar montado durante a operação.

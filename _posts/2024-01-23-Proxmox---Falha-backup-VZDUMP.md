Sofri com isso no meu servidor pois o backup é remoto.

O log dizia:

```
command 'rsync --stats -h --numeric-ids -aH --delete --no-whole-file --sparse --one-file-system --relative '--exclude=/tmp/?*' '--exclude=/var/tmp/?*' '--exclude=/var/run/?*.pid' /proc/????/root//./ /mnt/pve/nfs-remoto/dump/vzdump-lxc-???-2024_01_20-01_21_54.tmp' failed: exit code 23
```

Só falhava backup de container com disco do tipo arquivo raw.

Comprei um SSD liguei na USB do servidor, montei ela e alterei o arquivo 

> vi /etc/vzdump.conf
```
tmpdir: /mnt/pve/temp #caminho pro meu SSD externo
```

fonte: https://forum.proxmox.com/threads/tmpdir-setting-in-vzdump-conf-is-ignored.76689/

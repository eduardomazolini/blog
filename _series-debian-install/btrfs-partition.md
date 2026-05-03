---
order: 7
---
# BTRFS - Particionando

Se instalar usando opção sem LVM, criando a partição manualmente e escolha o / como BTRFS para facilitar.

## Limpeza dos dados
Agora vamos apagar os dados antigos, que já foram copiados com rsync

```
sudo rm -rf /home.old
sudo rm -rf /var/log.old
sudo rm -rf /var/cache.old
```

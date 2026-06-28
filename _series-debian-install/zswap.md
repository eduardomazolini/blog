---
order: 6
---
# zSwap

### tl;dr

Em caso de dúvida, prefira usar o zswap. Use apenas zram se você tiver uma razão altamente específica para.

> [Aqui está](https://chrisdown.name/2026/03/24/zswap-vs-zram-when-to-use-what.html) um excelente artigo que explica como a ZRAM e o ZSWAP funcionam e quais são as diferenças. Pode ser muito útil para determinar qual é o melhor para usar e como.

A afirmação acima vem do artigo recomendado na wiki do Debian.

Artigos na documentação do Debian sobre:
- [Zswap](https://wiki.debian.org/Zswap)
- [ZRam](https://wiki.debian.org/ZRam)

Artigos na documentação do Kernel sobre:
- [Zswap](https://www.kernel.org/doc/html/latest/admin-guide/mm/zswap.html)
- [ZRam](https://www.kernel.org/doc/html/latest/admin-guide/blockdev/zram.html)

## Qual compressor?

``` bash
# Ver flags AVX2 na CPU indica Haswell (2013) ou mais novo
grep -m1 flags /proc/cpuinfo | tr ' ' '\n' | grep -E "^avx2$|^avx$"
```

| Resultado            | Geração aproximada         | Compressor                  |
| -------------------- | -------------------------- | --------------------------- |
| `avx2` presente      | Haswell 2013+              | **zstd**                    |
| `avx` mas sem `avx2` | Sandy/Ivy Bridge 2011-2012 | **zstd** com cautela ou lz4 |
| Nenhum dos dois      | Pré-2011                   | **lz4**                     |


## Teste e Ativação Temporária

Use estes comandos para ativar a compressão imediatamente sem reiniciar. Útil para validar a estabilidade.

Antes de alterar recomendo olhar os valres padrão usando `cat` ou `grep`.
``` bash
# Mostrar os parametros
grep . /sys/module/zswap/parameters/*

# Habilita o módulo principal
echo 1 | sudo tee /sys/module/zswap/parameters/enabled

# Define o motor de compressão (LZ4 - Baixo uso de CPU)
echo lz4 | sudo tee /sys/module/zswap/parameters/compressor

# Define o alocador de memória normalmente é o padrão, não precisa
echo zsmalloc | sudo tee /sys/module/zswap/parameters/zpool

# Define o limite máximo de uso da RAM física pelo zSwap (50% da RAM total)
echo 50 | sudo tee /sys/module/zswap/parameters/max_pool_percent
```

## Verificação de Funcionamento

Para confirmar que o sistema está interceptando o Swap, use o computador por alguns minutos e execute:

``` bash
sudo grep -r . /sys/kernel/debug/zswap/
```

**Retorno esperado (exemplo):**

> `/sys/kernel/debug/zswap/stored_pages:4458` (Páginas comprimidas na RAM)
> `/sys/kernel/debug/zswap/pool_total_size:7028736` (RAM física consumida em bytes)
> `/sys/kernel/debug/zswap/written_back_pages:0` (Zero significa que nada precisou ir para o disco ainda)

---

## Configuração Definitiva (Persistência)

Siga estes passos para que a configuração sobreviva ao reboot e inicie precocemente no boot.

### Passo A: Módulos do Initramfs

Adicione os drivers necessários à imagem de inicialização:

``` bash
# Adiciona o alocador de pool
echo "zsmalloc" | sudo tee -a /etc/initramfs-tools/modules
```

Escolha agora se zstd ou lz4:

Somente para zstd:
``` bash
# Adiciona os módulos de compressão zstd
echo "zstd" | sudo tee -a /etc/initramfs-tools/modules
echo "zstd_compress" | sudo tee -a /etc/initramfs-tools/modules
```

Somente para lz4:
``` bash
echo "lz4" | sudo tee -a /etc/initramfs-tools/modules
echo "lz4_compress" | sudo tee -a /etc/initramfs-tools/modules
```

Atualize o initramfs
``` bash
sudo update-initramfs -u
```

### Passo B: Parâmetros do Kernel (GRUB)

1. Edite o arquivo: `sudo nano /etc/default/grub`
    
2. Localize a linha `GRUB_CMDLINE_LINUX_DEFAULT`.
    
3. Adicione os parâmetros:
    
    `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash zswap.enabled=1 zswap.compressor=lz4 zswap.zpool=zsmalloc"`

	`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash zswap.enabled=1 zswap.compressor=zstd zswap.zpool=zsmalloc zswap.max_pool_percent=50"`

1. Atualize o menu de boot:
    
``` bash
sudo update-grub
```
    

---

## Resumo de Comandos Úteis

| **Objetivo**                   | **Comando**                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| **Verificar RAM e Swap**       | `free -m`                                                    |
| **Verificar Disco de Swap**    | `swapon --show`                                              |
| **Desativar Instantaneamente** | `echo 0 \| sudo tee /sys/module/zswap/parameters/enabled`    |
| **Monitorar em tempo real**    | `watch -n 2 "sudo cat /sys/kernel/debug/zswap/stored_pages"` |

## Outros ajustes

### max_pool_percent

Recomendo observar e procurar entender o parametro, melhor.
Já ensinamos a modificar e deixar permanente no grub.

### [swappiness](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html#swappiness)

Como temos compressão no que for considerado swap pedir para o sistema usar mais swap significa pedir pra mais conteúdo ser comprimido.


Direto
``` bash
echo 80 | sudo tee /proc/sys/vm/swappiness
```

Persistente
``` bash
# Abra o editor
sudo nano /etc/sysctl.d/99-zswap-tuning.conf
```

```
# coloque o conteúdo
vm.swappiness=80
```

### [page-cluster](https://www.kernel.org/doc/html/latest/admin-guide/sysctl/vm.html#page-cluster)

Como o swap esta na memória não a vantagens de aproveitar o comando de leitura para recuperar o que não for necessário.

Direto
```
echo 0 | sudo tee /proc/sys/vm/page-cluster
```

Persistente
```
# Abra o editor
sudo nano /etc/sysctl.d/99-zswap-tuning.conf
```

```
# coloque o conteúdo
vm.page-cluster=0
```

# TODO

- O GRUB é o melhor lugar para salvar isso?

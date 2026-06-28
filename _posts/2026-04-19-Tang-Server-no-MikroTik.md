---
tags:
  - mikrotik
  - linux
  - luks
  - vm
  - segurança
  - rede
  - alpine
---
# Tang Server no MikroTik ARM64

Objetivo é rodar o servidor Tang que é extremamente leve como container no roteador, para que todos os computadores (linux) da rede possam descriptografar seus discos (luks) sem precisar de senha na inicialização.

- Tang **não armazena** nenhuma chave do cliente
- Se o Tang estiver inacessível, o sistema cai para prompt de senha LUKS normalmente
- As chaves ficam em `/db` dentro do container (persistidas via mount)

---

## Requisitos

- MikroTik  RB com processsador ARM64 com RouterOS v7.4 ou superior
- Pacote `container.npk` instalado
- Container mode habilitado

### Habilitar container mode

```routeros
/system/device-mode/update container=yes
```

Requer reboot físico para confirmar.

---

## Imagem utilizada

```
padhihomelab/tang:latest
```

- Baseada em Alpine Linux
- **Multiarch**: suporta `arm64` nativamente (compatível com o CPU Marvell Armada do RB5009)
- Porta interna: **8080**
- Diretório de chaves: `/db`

---

## Configuração no RouterOS

### 1. Interface veth para o container

Essa é a interface (placa de rede) que é ligada ao container ela tem que ter a configurção de IP.

```routeros
/interface/veth/add name=veth1-tang address=172.20.0.2/24 gateway=172.20.0.1
```

### 2. Bridge e endereço IP do Roteador

No mikrotik quando criamos uma bridge ela tem 2 funções.
- criamos uma nova interface ligada ao processamento do roteador
- criamos um agrupamento de interfaces que se comunicam como em um switch.
Todas as portas ligadas a bridge, pertencentes a bridge se comunicam entre si como um switch. 
Quando colocamos a porta veth na bridge estamos ligado nosso container ao roteador e a outras interfaces da bridge como as conectadas aos computadores da LAN.
Se uma interface da rede LAN estiver na bridge o container entra na rede LAN como se fosse apenas mais um computador.
Se quiser pode isolar seu container em uma bridge exclusiva, só com o roteador e o container.

```routeros
/interface/bridge/add name=docker-bridge
/ip/address/add address=172.20.0.1/24 interface=docker-bridge
/interface/bridge/port/add bridge=docker-bridge interface=veth1-tang
```

### 3. Persistência das chaves (mountlist)

```routeros
/container/mounts/add name=tang-db src=/tang-db dst=/db list=tang-db
```

> **Importante:** sem este mount, o Tang gera novas chaves a cada reinicialização, quebrando todos os clientes Clevis vinculados.

### 4. Adicionar o container

```routeros
/container/config/set registry-url=https://registry-1.docker.io tmpdir=/pull

/container/add remote-image=padhihomelab/tang:latest \
  interface=veth1-tang \
  root-dir=/containers/tang \
  mountlists=tang-db \
  start-on-boot=yes
```

O RouterOS faz o pull direto do Docker Hub e extrai a imagem arm64 automaticamente.

### 5. Iniciar o container

Aguarda o status mudar de `extracting` para `stopped`:

```routeros
/container/print
```

Depois:

```routeros
/container/start 0
```

---

## Verificar funcionamento

### No RouterOS

``` routeros
/container/print
# deve mostrar "R" (running)

/log/print follow where topics~"container"
```

### Na rede (cliente Linux)

``` bash
curl http://172.20.0.2:8080/adv
```

Resposta esperada: JSON com as chaves públicas do Tang (JWS).

Exemplo de resposta válida:

``` json
{
  "payload": "eyJrZXlzIjogW3s...",
  "protected": "eyJhbGciOiJFUzUxMiIsImN0eSI6Imp3ay1zZXQranNvbiJ9",
  "signature": "AUGQr4drtQCuS3..."
}
```

---

## Expor via IP do roteador (opcional)

Se quiser acessar pelo IP do roteador em vez do IP do container:

``` routeros
/ip/firewall/nat/add \
  chain=dstnat \
  dst-address=<ip-do-roteador> \
  dst-port=7500 \
  protocol=tcp \
  action=dst-nat \
  to-addresses=172.20.0.2 \
  to-ports=8080
```

Teste:

``` bash
curl http://<ip-do-roteador>:7500/adv
```

---

## Configurar Clevis nos servidores Debian

### Instalar

``` bash
sudo apt install clevis clevis-luks clevis-initramfs
```

### Vincular volume LUKS ao Tang

``` bash
sudo clevis luks bind -d /dev/sdX tang '{"url": "http://172.20.0.2:8080"}'
```

O comando exibe o thumbprint da chave e pede confirmação, depois solicita a senha LUKS atual.

### Atualizar initramfs

``` bash
sudo update-initramfs -u
```

Na próxima reinicialização, o servidor descriptografa automaticamente se o Tang estiver acessível.

### Verificar slots LUKS

``` bash
sudo cryptsetup luksDump /dev/sdX
# ou
sudo clevis luks list -d /dev/sdX
```

---

## Notas de segurança

- As chaves Tang **não devem estar no mesmo disco físico** que o volume LUKS protegido — no caso do RB5009 isso está correto por design
- Sempre mantenha uma **senha de recuperação** em um slot LUKS separado:

``` bash
sudo cryptsetup luksAddKey --key-slot 7 /dev/sdX
```

- Guarde esse passphrase offline de forma segura
- Rotacione as chaves Tang periodicamente e reconecte os clientes com `clevis luks bind` novamente

---

## Resumo de endereços

| Recurso                         | Endereço                     |
| ------------------------------- | ---------------------------- |
| IP do container                 | `172.20.0.2`                 |
| IP do host (bridge)             | `172.20.0.1`                 |
| Porta Tang (interna)            | `8080`                       |
| Porta Tang (NAT externo)        | `7500` (configurável)        |
| URL do `/adv`                   | `http://172.20.0.2:8080/adv` |
| Diretório de chaves (host)      | `/tang-db`                   |
| Diretório de chaves (container) | `/db`                        |

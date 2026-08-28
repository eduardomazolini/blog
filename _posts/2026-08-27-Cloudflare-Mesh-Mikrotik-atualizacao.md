---
tags: [cloudflare, wireguard, vpn, docker, mikrotik]
---

O **Cloudflare Mesh** (antigo WARP Connector) é uma VPN site-to-site gratuita da
Cloudflare. Para usar num roteador Mikrotik (ou qualquer cliente WireGuard), é
preciso extrair a configuração WireGuard do nó — e é aí que entra o
[wgcf-connector](https://github.com/AnimMouse/wgcf-connector), do AnimMouse.

Este post é uma **atualização** dos anteriores:

- [Extraindo configuração do cliente WARP]({% post_url 2025-01-17-Extraindo-configurao-do-cliente-WARP %}) — o método antigo (warp-cli + jq).
- [CloudFlare WARP no Mikrotik]({% post_url 2025-01-17-CloudFlare-WARP-p-Mikrotik %}) — os comandos de configuração no Mikrotik.

A diferença: o `wgcf-connector` instala o `warp-cli` dentro de um container,
registra o Cloudflare Mesh com o token e extrai tudo automaticamente, gerando o
`.conf` pronto.

## Passo a passo

1. No dashboard do Cloudflare, crie um **nó Mesh** e copie o **token** gerado
   (começa com `eyJhIjoi` e termina com `In0=`).

2. Construa a imagem:

```bash
docker build -t wgcf-connector .
```

3. Rode passando o token:

```bash
docker run --rm -v $(pwd):/app/output wgcf-connector <TOKEN>
```

> Alternativa — usar a imagem pronta:
> `docker run --rm -v $(pwd):/app/output ghcr.io/animmouse/wgcf-connector <TOKEN>`

4. Será gerado `wgcf-connector-<registration_id>.conf` no diretório atual, com
   `[Interface]` (PrivateKey, Address, DNS, MTU) e `[Peer]` (PublicKey,
   AllowedIPs, Endpoint).

5. Aplique os valores no Mikrotik — os comandos de interface/peer estão no
   [post do CloudFlare WARP no Mikrotik]({% post_url 2025-01-17-CloudFlare-WARP-p-Mikrotik %}).

## Atenção

- O `.conf` contém a **chave privada** — não commite nem compartilhe.
- O token também é sensível.
- Se o endpoint IPv4 vier `162.159.192.x`, use `162.159.193.x` (menor latência).

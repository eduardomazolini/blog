---
tags: [DNS, linux, Mikrotik, rede]
---

## Controles de DNS na Ludicando

Na Ludicando alguns controles eu faço no Mikrotik usando DNS restritivo e alterando alguns domínios para não responder e outros para tratarem o conteúdo para ser seguro para crianças.

Abaixo o link para o script (com comentários citando as fontes de cada produto):
<https://gist.github.com/eduardomazolini/77466da39e7940b7d652b2bb5af6ef55>

## Serviços de DNS confiáveis/populares

### OpenDNS


IPv4
208.67.222.222
208.67.220.220

IPv6
2620:119:35::35
2620:119:53::53

DoH
<https://doh.opendns.com/dns-query>

### OpenDNS — Family Shield


IPv4
208.67.222.123
208.67.220.123

DoH
<https://doh.familyshield.opendns.com/dns-query>

### Cloudflare


IPv4
1.1.1.1
1.0.0.1

IPv6
2606:4700:4700::1111
2606:4700:4700::1001

DoH
<https://cloudflare-dns.com/dns-query>

### Cloudflare — Block malware


IPv4
1.1.1.2
1.0.0.2

IPv6
2606:4700:4700::1112
2606:4700:4700::1002

DoH
<https://security.cloudflare-dns.com>

### Cloudflare — Block malware and adult content


IPv4
1.1.1.3
1.0.0.3

IPv6
2606:4700:4700::1113
2606:4700:4700::1003

DoH
<https://family.cloudflare-dns.com>
<https://one.one.one.one/dns-query?name=cloudflare.com>

Docs
<https://developers.cloudflare.com/1.1.1.1/encryption/>

### Google Public DNS


IPv4
8.8.8.8
8.8.4.4

IPv6
2001:4860:4860::8888
2001:4860:4860::8844

DoH
<https://dns.google/dns-query>(RFC 8484 - GET e POST)
<https://dns.google/resolve>?(API JSON - GET)

Docs
<https://developers.google.com/speed/public-dns/docs/doh?hl=pt-br>


### AdGuard DNS — Servidores padrão

AdGuard DNS bloqueará anúncios e rastreadores.


IPv4
94.140.14.14
94.140.15.15

IPv6
2a10:50c0::ad1:ff
2a10:50c0::ad2:ff

DoH
<https://dns.adguard-dns.com/dns-query>

Página
<https://adguard-dns.io/pt_br/public-dns.html>

### AdGuard DNS — Servidores sem filtragem


IPv4
94.140.14.140
94.140.14.141

IPv6
2a10:50c0::1:ff
2a10:50c0::2:ff

DoH
<https://unfiltered.adguard-dns.com/dns-query>

### AdGuard DNS — Proteção familiar

Bloqueia anúncios, rastreadores, conteúdo adulto e ativa a Pesquisa Segura / Modo seguro quando possível.


IPv4
94.140.14.15
94.140.15.16

IPv6
2a10:50c0::bad1:ff
2a10:50c0::bad2:ff

DoH
<https://family.adguard-dns.com/dns-query>

### Referência adicional


Admin Console Google Workspace (suporte)
<https://support.google.com/a/answer/6214622>


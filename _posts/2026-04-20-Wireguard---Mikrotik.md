---
tags:
  - mikrotik
  - vpn
  - wireguard
---
# Configuração manual do [WireGuard](https://help.mikrotik.com/docs/spaces/ROS/pages/69664792/WireGuard)

## Interface wireguard

Aqui criamos a interface do wireguard, com intenção de ativar o servidor do wireguard.
Ela também deve ter um IP. 
Se o seu caso exigir lembre de fazer regras de NAT.
```
/interface/wireguard/add listen-port=13231 mtu=1420 name=wireguard1
/ip/address/add address=192.168.127.1/24 interface=wireguard1 network=192.168.127.0
```
No meu exemplo usei a rede `192.168.127.0/24` use o que quiser. Esse é só um exemplo, o valor deve ser consistente no resto da configuração.
### Peers
No wireguard não criamos só o usuário e senha temos que fazer toda a configuração.
O Mikrotik aceita que parâmetros necessários ao client sejam informados para facilitar a geração do arquivo de configuração.

```
/interface/wireguard/peers add name=<NOME_DO_CLIENTE> \
    allowed-address=192.168.127.<FINAL_DO_IP>/32 client-address=192.168.127.<FINAL_DO_IP>/32 \
    client-endpoint=<IP Publico/DNS> client-listen-port=13231 disabled=no \
    interface=wireguard1 \
    persistent-keepalive=25s client-keepalive=25s \
    preshared-key=auto private-key=auto
```
**Nome do Cliente** - A forma como você identifica seu usuário.
**Final do IP** - Deve ser único para cada cliente então veja os que já existem.
**IP Publico/DNS** - O IP ou DNS que o client vai usar para acessar o servidor

### Confirmando

```
/interface/wireguard/peers/print where name=thinkpad_edu
```

Para ver o número o QRCode e o texto do arquivo de configuração:
```
/interface/wireguard/peers/show-client-config [find name=marcelo] 
```

### Criando arquivo de importação

Para salvar o conteúdo do arquivo para enviar para o usuário importar:
```
/interface/wireguard/peers/show-client-config [find name=marcelo] \
file=marcelo.conf
```

### Apagar a chave privada

Depois de exportar rode o comando que envia  `private-key=""` isso gera o AAAAAAAA no private e assim aumenta a segurança pois não fica armazenada a chave privada do cliente.
```
/interface/wireguard/peers/set [find name=marcelo] private-key="" 
```

# [Back-to-Home](https://help.mikrotik.com/docs/spaces/ROS/pages/197984280/Back+To+Home)

O modo mais fácil usar o app [Android](https://play.google.com/store/apps/details?id=com.mikrotik.android.freevpn) ou [iPhone](https://apps.apple.com/lv/app/mikrotik-back-to-home/id6450679198) e depois só configurar os usuários no Mikrotik, assim os peers são criados  automaticamente.

```
/ip/cloud/back-to-home-user/add name=johnDoe
```

Se quiser ver a configuração pelo peer funciona ou pode ver diretamente no user:

```
/ip/cloud/back-to-home-user/show-client-config number=1
```

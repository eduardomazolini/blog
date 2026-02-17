---
---

# Problemas com Nginx Proxy Manager e rádios M5

Eu uso nginx proxy manager e estava tendo problema em conectar meus rádios M5.

Infelizmente a solução reduziu a segurança de todos os meus outros serviços deste proxy porque não achei uma solução que poderia ser aplicada a um único host.

Outro problema: não sei deixar o meu NPM configurado se recriar o container.

## Solução: criar certificados na Let's Encrypt do tipo RSA

Para isso eu editei o `/etc/letsencrypt.ini` alterando `key-type = ecdsa` para `key-type = rsa`.
  
  
    /etc/letsencrypt.ini
  
    text = True
    non-interactive = True
    webroot-path = /data/letsencrypt-acme-challenge
    key-type = rsa
    elliptic-curve = secp384r1
    preferred-chain = ISRG Root X1

## Alteração no algoritmo de troca de chave DH

Para isso precisa criar o arquivo dhparam.pem com o comando:
  
  
    openssl dhparam -out /etc/nginx/dhparam.pem 2048

Após criar o arquivo precisa ser indicado na configuração com `ssl_dhparam`, eu escolhi fazer essa configuração em `/etc/nginx/conf.d/include/ssl-ciphers.conf`
  
  
    /etc/nginx/conf.d/include/ssl-ciphers.conf
    # intermediate configuration. tweak to your needs.
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'DHE-RSA-AES128-GCM-SHA256:AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-A
    ES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-PO
    LY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers off;
    ssl_dhparam /etc/nginx/dhparam.pem;

Por último precisa reiniciar o nginx.

## Configuração no container

Como estou usando container eu copiei e editei localmente os 2 arquivos de configuração depois enviei tudo para o container com os comandos:
  
  
    docker exec nginx-proxy-manager-app-1 openssl dhparam -out /etc/nginx/dhparam.pem 2048
    docker cp letsencrypt.ini nginx-proxy-manager-app-1:/etc/letsencrypt.ini
    docker cp ssl-ciphers.conf.bkp nginx-proxy-manager-app-1:/etc/nginx/conf.d/include/ssl-ciphers.conf
    docker restart nginx-proxy-manager-app-1

## Testando a configuração

Para testar usei o nmap:
  
  
    nmap --script ssl-enum-ciphers -p 443 uisp.xxxxxx.com.br

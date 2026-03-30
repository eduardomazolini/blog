---
tags:
  - ubnt
  - m5
  - nginx
  - letsencrypt
  - uisp
---
# Problemas com Nginx Proxy Manager e rádios M5

Eu uso nginx proxy manager e estava tendo problema em conectar meus rádios M5.

Infelizmente a solução reduziu a segurança de todos os meus outros serviços deste proxy porque não achei uma solução que poderia ser aplicada a um único host.

> Agora existe solução individual de certificado
{: .prompt-tip }

Outro problema: não sei deixar o meu NPM configurado se recriar o container.

## Solução: criar certificados na Let's Encrypt do tipo RSA

Para isso eu editei o `/etc/letsencrypt.ini` alterando `key-type = ecdsa` para `key-type = rsa`.
```
text = True
non-interactive = True
webroot-path = /data/letsencrypt-acme-challenge
key-type = rsa
elliptic-curve = secp384r1
preferred-chain = ISRG Root X1
```

> Na nova versão não precisa editar isso.
{: .prompt-tip }

## Alteração no algoritmo de troca de chave:

### DH

#### dhparam

Para isso precisa criar o arquivo dhparam.pem com o comando:
```
openssl dhparam -out /etc/nginx/dhparam.pem 2048
```

Após criar o arquivo precisa ser indicado na configuração em `/etc/nginx/conf.d/include/ssl-ciphers.conf`:  

```
ssl_dhparam /etc/nginx/dhparam.pem;
```

#### ssl_ciphers

- DHE-RSA-AES128-GCM-SHA256
- DHE-RSA-AES256-GCM-SHA384

### Estático / RSA

Não precisa do dhparam, precisa não existir na lista uma opção com inicio **DHE**.
#### ssl_ciphers

- AES128-GCM-SHA256

```
/etc/nginx/conf.d/include/ssl-ciphers.conf
# intermediate configuration. tweak to your needs.
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ciphers 'ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384:AES128-GCM-SHA256';
ssl_prefer_server_ciphers off;
ssl_dhparam /etc/nginx/dhparam.pem;
```
Por último precisa reiniciar o nginx.

## Configuração no container

Como estou usando container eu copiei e editei localmente os 2 arquivos de configuração depois enviei tudo para o container com os comandos:
```
docker exec nginx-proxy-manager-app-1 openssl dhparam -out /etc/nginx/dhparam.pem 2048

docker cp letsencrypt.ini nginx-proxy-manager-app-1:/etc/letsencrypt.ini

docker cp ssl-ciphers.conf.bkp nginx-proxy-manager-app-1:/etc/nginx/conf.d/include/ssl-ciphers.conf
```
docker restart nginx-proxy-manager-app-1

>Atenção o comando para baixar os arquivos originais eu não listei pq são arquivos pequenos cada um pode fazer como quiser. O importante é olhar o original.
{: .prompt-danger }  

>Na nova versão do NPM é possível cria certificados RSA, isso pode ser selecionado, não precisa mais editar o `/etc/letsencrypt.ini`
{: .prompt-warning }

## Testando a configuração

Para testar usei o nmap:
```
nmap --script ssl-enum-ciphers -p 443 uisp.xxxxxx.com.br
```

### Detalhes Sobre HTTPS

#### Certificado

Hoje existem certificados:
- RSA - Baseado em fatoração de número primo
- ECDSA - Baseado em curva Elíptica (mais seguro, menor e mais leve)

> M5 só aceita RSA
{: .prompt-warning }

> Agora o Nginx Proxy Manager permite escolher RSA individualmente e apesar do ECDSA ser o padrão.
{: .prompt-tip }

#### Troca de chaves

É o processo de combinar a combinação do cofre com o destinatário sem que o transportador ouça.

##### Estático

RSA que é chamada de estática pois usa o certificado se ele for comprometido pode usar para des-criptografar comunicações antigas  

>Quando um DHE é ativado essa opção é desativada.
{: .prompt-tip }

##### DHE (Diffie-Hellman Ephemeral)

Precisa de dhparam que é estático publico, mas é único.
Para gerar a chave um segundo numero aleatório é gerado.
No inicio o dhparam era igual pra todos, então as contas feitas a partir dele poderiam ser pré-calculadas por uma entidade poderosa, agora que são únicos isso fica impossível.

>Não é oferecida pelo M5 na conexão, mas ele aceita como cliente. Lembre de criar e especificar o dhparam.
{: .prompt-tip }

##### ECDHE (Elliptic Curve DHE)

É a evolução do DHE. Em vez de usar cálculos modulares complexos com números primos gigantes (que exigem muito processamento), ele utiliza a matemática de **Curvas Elípticas**.

> Mas nosso antigo equipamento M5 não é compatível.
{: .prompt-warning }

##### P-256 (prime256v1)

Um formato bem moderno pós-quântico compatível com NIST.

> Ainda não usado no nosso sistema.
{: .prompt-warning }

#### Algoritmo de Criptografia + Modo de Operação

É a espessura e o material das paredes do cofre (Criptografia) e como as trancas são dispostas (Modo).

##### AES

O algoritmo com tamanho da chave (128 / 256 bits), bom para CPUs modernas que tem instruções especificas para isso (AES-NI).
Modos de operação **GCM** (Rápido/Paralelo) ou **CBC** (Antigo/Legado).

>O único aceito pelos nossos equipamentos.
{: .prompt-tip }

##### ChaCha20
Feito para ser rápido via software. O modo é sempre **Poly1305**

#### Hashing

É o selo de lacre na porta. Se o selo estiver rompido ou raspado, você sabe que alguém tentou abrir ou alterar o conteúdo.

##### SHA-1

Obsoleto.

##### SHA-256 também conhecido com SHA-2

Padrão atual.

>Padrão
{: .prompt-tip }

##### SHA-384

Uma versão mais pesada e mais segura.

---
tag: [rascunho, intelbras]
---

Bom dia!

Eu gostaria de dividir com vocês 1,5 dia perdidos pra ver se alguém consegue continuar deste ponto.

Peguei um roteador do "Facebook Wi-Fi" para entender seu funcionamento a fundo.
As informações são apenas para conhecimento cada um é responsável com o que fazer com elas.

> Com grandes poderes grandes responsabilidades. - Tio Ben (Homem Aranha)

Estou divulgando o que pode ser visto por qualquer leigo.

## Processo de Registro

![](/assets/img/assistente1.PNG)

Na tela seguinte a esta você será questionado a concordar com os termos e o roteador vai entrar em contato com a Intelbras para se registrar no Facebook. Ou seja o pulo do gato do registro no Facebook não esta no roteador.


![](/assets/img/assistente2.png)


É nesta o que esta ocorrendo por trás é um **POST** para:

![](/assets/img/censurado.jpg)

Agora com uma identificação no Facebook o usuário vai abrir a tela de configuração e o roteador vai ficar perguntando pro Facebook se ela já foi salva.

![](/assets/img/assistente4.PNG)

Aqui o que está ocorrendo é um GET para:

![](/assets/img/censurado.jpg)

O usuário faz a configuração na URL:
https://www.facebook.com/wifiauth/config?gw_id=xxxxxxxx

![](/assets/img/facebook1.png)

Aqui a configuração esta terminada.

## Processo de Login

O cliente é redirecionado para o roteador e acessa:

http://10.0.0.1:8080/cgi-bin/fbRedirect.cgi?continue=http%3A%2F%2Fgoogle.com%2F

O parâmetro **continue** é a pagina que queria acessar no meu caso google já em urlencode.

O retorno é um redirect para o Facebook:

https://www.facebook.com/wifiauth/login/

Os parâmetros do GET: 

**gw_id:xxxxx**

**redirect_url:** http://10.0.0.1:8080/cgi-bin/fbAuth.cgi?cookie=xxxxxx (Tudo com urlencode)

**redirect_mac** :xxxxxxxxx
## Alguém por favor como escrever o redirect_mac?

Esse valor deve assinar toda a url pois se você editar o redirect_url o Facebook rejeita. O cookie e redirect_mac são diferentes a cada solicitação, penso que fica diferente pois assina e cookie muda.

O Facebook devolve para:

http://10.0.0.1:8080/cgi-bin/fbAuth.cgi?cookie=xxxx&token=xxxxx&prevcheckin=3

Depois que o cliente volta o roteador confirma com o Facebook usando o token ou seja não adianta ser espertinho e tentar burlar o facebook.

Veja o roteador confirmando com POST:

![](/assets/img/censurado.jpg)

Então a cada 5 minutos ele verifica se o usuário pode continuar e envia para o Facebook também a quantidade de dados que o usuário consumiu.

Veja o roteador enviando report com POST:

![](/assets/img/censurado.jpg)

## Sobre os arquivos e regras

Como a informação fica no roteador:

Em /var/fblist/ é criado um arquivo de nome o IP do cliente e conteúdo o token_do_cliente.

Ele verifica neste diretório quais clientes ele deve perguntar se ainda podem continuar.

Para cada cliente funcionando são adicionadas 2 regras de iptables e 2 regra de ebtables

iptables -t mangle -A INTERNET_TO_CLIENT -d [ip do cliente]/32 -j MARK --set-mark 0xfffb

iptables -t mangle -A CLIENT_TO_INTERNET -s [ip do cliente]/32 -j MARK --set-mark 0xfffb

ebtables -t nat -I CLIENT_TO_INTERNET -p IPv4 --ip-src [ip do cliente] -j mark --mark-set 0xfffb --mark-targe ACCEPT

ebtables -t nat -A POSTROUTING -p IPv4 --ip-dst [ip do cliente] -j mark --mark-set 0xfffb --mark-targe ACCEPT

Os arquivos cgi web estão em /fb/cgifbin são:

fbRedirect.cgi fbContinue.cgi fbAuth.cgi

Os arquivos que iniciam a configuração e checam estão em /usr/scripts/ são:

fbRules.sh fbCheck.sh

## Usando Facebook na LAN

Após o cliente fazer a autenticação seria muito chato ele fazer novamente e novamente cada vez que mudar de Access Point em um local grande com muitos roteadores.

Para isso eu queria colocar o "Facebook Wi-Fi" como primeiro roteador e um monte de roteador baratinho em bridge ligados a LAN do mesmo.

O ideal seria editar o /usr/scripts/fbRules.sh próximo a linha 42 inserir:

    ebtables -t nat -A PREROUTING -i eth1 -p ip --ip-dst 10.0.0.1 -j ACCEPT
    ebtables -t nat -A PREROUTING -i eth1 -j GUESTIN
    ebtables -t nat -I PREROUTING -i eth1-j CLIENT_TO_INTERNET

Como a pasta /usr é read-only temos que usar o que nos é dado a pasta /var.
Existe o arquivo /var/etc/script.sh que você pode editar e colocar o seguinte conteúdo usando vi:

> #!/bin/sh
> CAPTIVE_IP=`firmware getMib lanIpAddr`
> WIFI_INTERFACE="eth1"
> ebtables -t nat -A PREROUTING -i $WIFI_INTERFACE -p ip --ip-dst $CAPTIVE_IP -j ACCEPT
> ebtables -t nat -A PREROUTING -i $WIFI_INTERFACE -j GUESTIN
> ebtables -t nat -I PREROUTING -i $WIFI_INTERFACE -j CLIENT_TO_INTERNET

Como não sei salvar por linha de comando, altere alguma configuração via web e aplique a modificação, isso salva todas as modificações em /var.

Se alguém souber como salvar o /var por linha de comando me avisa por favor.

## **Vantagem do Login do Facebook Wi-Fi**

A covardia do Facebook com os outros desenvolvedores

![](/assets/img/facebook2.png)

A tela do Facebook que o desenvolvedor normal pode redireciona o usuário não funciona no navegador que o celular Moto G, por exemplo, abre pra autenticação de Hotspot.

O usuário tem que conceder a permissão de acesso aos dados básicos e permissão de escrita na linha do tempo dele. Essa permissão é para o desenvolvedor escrever qualquer coisa. Pensem na responsabilidade.

Quando o usuário permite, e somente neste momento, ele decide qual a publicidade (Somente eu, Amigos, Publico) dos dados que o aplicativo vai publicar. Se ele não quiser que o primeiro check-in dele seja visto somente por ele, todos os demais check-in terão essa publicidade ou seja nenhuma.

Então em uma **única tela,** que funciona em **qualquer celular** , o cliente pode autorizar **publicar** e escolher **quem vê** a cada momento.

Por que coloquei como censurado:

Olá Eduardo,

Infelizmente tive que apagar o post

Hotspot 300 Intelbras - Salvar modificações por SSH

devido a um pedido da intelbras, pois aparentemente você quebrou alguma propriedade intelectual deles.

Eu recomendo você apagar o mesmo do seu blog também o mais rápido possível para evitar qualquer problemas legais com eles.

Obrigado,

Por que coloquei como censurado:



"Hoje o usuário **_eduardomazolini_** fez um post do produto HotSpot 300 da Intelbras fomentando outros usuários a quebrar o código de software embarcado nele e invadindo nossa propriedade intelectual.
Link do post: <https://under-linux.org/showthread.php?t=186522>

Você consegue derrubar esse post do ar o mais rápido possível?"

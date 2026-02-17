Essa semana estava testando um chatbot para skype e na documentação do exemplo sugeria o uso do ngrok pra rodar a demo, até então não conhecia o serviço.

Já vi muitos modos de fazer túnel para diversos propósitos, mas a simplicidade e utilidade deste serviço é impressionante.

O site oficial é [ngrok.com][65].
Eu usei para criar um túnel publico pra a aplicação que esta rodando na minha maquina de desenvolvimento, mas não é só isso, o Skype exige que o servidor seja HTTPS, eu não precisei criar certificado, nem parei pra pensar nisso.

O túnel no lado publico é HTTP ou HTTPS usa o certificado da ngrok, afinal é um subdomínio deles, e chama do meu lado aplicação HTTP.

Simplesmente tinha meu servidor XAMPP exposto em um subdominio deles com certificado ou seja HTTPS. No segundo seguinte meu aplicativo em NODE.JS do bot funcionado com HTTPS recebendo os webhooks.

DDNS é coisa do passado com esse serviço, quanto já apanhei:
 \- configurando encaminhamento de porta do roteador,
 \- fixando a reserva de IP no DHCP pra minha maquina,
 \- gerar um certificado HTTPS quase impossível em algumas situações.

![][66]

Como o site diz:
Public URLs for **building webhook integrations**.
Public URLs for **testing your chatbot**.

Publique endereços para webhooks que também são usadas por chatbots.

Public URLs for **exposing your local web server**.
Public URLs for **demoing from your own machine**.
Public URLs for **sending previews to clients**.
Public URLs for **testing on mobile devices**.

Publique URLs para expor seu servidor local permitindo demonstração, mostrar previas sem precisar fazer deploy, testar backend de aplicativos moveis.

Public URLs for **SSH access to your Raspberry Pi**.





Crie túnel TCP para acessar seu servidor por SSH.




Éhhhh o serviço não é exclusivo pra HTTP/HTTPS é também túnel TLS e TCP.

Você pode expor um banco de dados, qualquer serviço que quiser.




Espero que tenham achado tão util quanto eu.

 [65]: https://ngrok.com/
 [66]: https://camo.githubusercontent.com/f2d698991e6a0411680413ebcc15a6460b8beda3/68747470733a2f2f6e67726f6b2e636f6d2f7374617469632f696d672f6f766572766965772e706e67


---
---

Pessoal eu penei por um ano e meio para conseguir entender o que fazer e como fazer. Finalmente terminei.

Eu vi um consultor de TI usar um HUB de USB para ligar todos os cabos console a um equipamento que ele poderia acessar caso a rede estivesse fora. Eu comprei os Hubs USB em 8 de Setembro de 2023.

Pedi um Chip Vivo com modem USB para me fornecer o acesso também.

Só que o modem da Vivo tem bloqueio para acesso direto ao IP dele.

Em alguns caso o modem fica atrás de CGNAT também.

Como resolver?

1) VPN
Foi minha primeira ideia. Mas ai quem fosse resolver o meu problema teria que estar na mesma VPN com o mesmo software de VPN instalado eu teria que enviar as configurações do acesso.

2) WARP CloudFlare

Foi o que pensei por muito tempo e por isso estudei suas formas.

A vinda do MikroTik v7 com Wireguard parecia a solução.

Perdi um bom tempo para entender tudo por isso acabei publicando os artigos anterioes sobre WARP.

3) Cloudflare Tunnel (cloudflared) 


Depois de entender que as aplicações na Cloudflare só funcionam com Cloudlared Tunnel e não com WARP. Precisava subir um servidor só para rodar o túnel.

 Então vaio a ideia de fazer isso com container dentro do Mikrotik e essa é a solução. 
**Vou explicar no próximo post como fazer o container com o túnel.**

Mas quem for acessar precisa fazer isso de forma muito rápida e acessar o MikroTik para depois fazer os acessos aos equipamentos me parecia limitado, bom seria ter um servidor Linux.
Quem estiver em meu socorro tem que lembrar usuário e senha do acesso que é usado uma vez só na vida ou quem sabe nunca se Deus quiser. Pra depois pular para os equipamentos de rede.

O Cloudflare **BROWSER SSH** é muito simples mas pede senha ou chave privada, depois de ter autenticado o usuário na página deles.

Para não precisar entra com senha ou chave privada podemos usar certificado, mas o usuário seria sempre o que estivesse antes do @ do e-mail. 


Mas qual Vai ser o e-mail que meu amigo salvador que vai me ajudar no momento de crise tem para eu permitir ele acessar minha rede?

Eu teria que acessar, pra depois criar ele no Linux, mas se alguém vai me socorrer pode ser que um dos motivos é eu estar indisponível no momento.

Ai veio a ideia se eu criar um servidor Linux que aceite qualquer usuário como certificado?
Um servidor Linux com acesso SSH liberado exclusivamente para o IP do servidor de túnel.
Um servidor que não autentique por senha, mas todos os usuários teriam acesso aos mesmos arquivos.

**Vou explicar no próximo post como fazer o servidor SSH.**

Até lá!

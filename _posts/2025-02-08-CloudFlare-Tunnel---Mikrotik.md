---
---

## **TL;DR**

 Depois de fazer o túnel configure como app seu MikroTik por web e SSH.

MAS você ainda vai ter que entrar com usuário e senha do MikroTik todas as vezes depois de se autenticar na Cloudflare.

MAS o container [cloudflare/cloudflared](https://hub.docker.com/r/cloudflare/cloudflared/tags?name=latest) só tem pra **ARM64** não iria rodar em uma 4011.

Eu criei um container para arm32/v7 que roda na minha RB4011, se precisar [cloudlared-arm-mikrotik](https://hub.docker.com/r/eduardomazolini/cloudlared-arm-mikrotik) pode usar.

## Para quem possa interessar os detalhes 

Bom se você não me conhece, para colocar algo meu para rodar na sua rede sem saber como funciona, talvez você queira replicar minha experiencia e fazer sua versão.

Eu fiz o [Dockerfile](https://github.com/eduardomazolini/cloudflare-mikotik/blob/main/cloudflared/Dockerfile) e disponibilizei no meu [GitHub](https://github.com/eduardomazolini).

Lá esta tudo bem explicado em 3 arquivos README.md separados. 

goog_33201163

https://github.com/eduardomazolini/cloudflare-mikotik

Obrigado!

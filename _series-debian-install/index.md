---
order: 0
---

# Pós-instalação no Debian

Esta é minha primeira série mais organizada do que o restante do blog.  
Foi pensada a partir da experiência no InstallFest da CryptoRave.

Vou definir, com minhas palavras, como entendo um InstallFest:

- não é uma prestação de serviço;
- é um espaço onde você recebe orientação e acompanhamento para realizar sua primeira instalação de Linux;
- é focado em software livre, por diversos motivos que não cabem em um parágrafo;
- é um espaço para troca de informações e contatos;
- por limitações materiais, de tempo e conhecimento, exige alguns cuidados e a definição de limites;
- por esses mesmos limites, precisa oferecer uma experiência homogênea básica, mas ainda assim individual.

Por decisão conjunta, o [Debian - O Sistema Operacional Universal](https://www.debian.org/) foi escolhido como a distribuição a ser instalada nos computadores, e o [Tails](https://tails.net/) para uso em pendrives.

É comum encontrar tutoriais de pós-instalação do Debian na internet. Este será apenas mais um.

Não pretendo dizer:

- "Siga todos os passos cegamente."

Quero dizer:

- "Estes são alguns caminhos que eu sigo — veja se fazem sentido para você."  
- "Estas são as referências oficiais, mas aqui está um modo mais rápido, pensado para economizar tempo e evitar problemas que já enfrentei."

---

# [Alt+Tab](alt+tab.html)

No Debian 2 teclas de atalho fazem a mesma coisa alterar entre applicativos. Vamos fazer o alt+tab alterar entre janelas igual no Windows e o super+tab fica como era.

# [Splash](splash.html)

Alguns usuários ficam intimidados com os detalhes dos logs de inicialização só o fato de exibir os dados os assusta, então vamos colocar uma tela mais bonita e esconder os detalhes.

# [Flatpak](flatpak.html)

Flatpak vem crescendo e não vai querer deixar de usar um app por que ele não é empacotado como deb.

# [AppImage](appimage.html)

AppImage não é para ser insalado, mas não vai querer rodar seus apps da pasta Download sem ter um belo atalho.
Também corrigimos erro ao excutar devido a uma dependencia, muti importante.

# [Luks](luks.html)

A questão é segurança, se precisa hibernar, precisa ajustar o desbloqueio do SWAP antes do boot.

# [Hibernate](hibernate.html)
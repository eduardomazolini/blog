# Guia de estilo — como escrever os posts do blog do Mazolini

Este documento serve para que um assistente (ou eu mesmo) consiga redigir posts
novos mantendo a minha voz. Ele tem duas partes:

1. **O prompt** — pronto para colar antes do conteúdo bruto/rascunho.
2. **O guia de regras** — cada regra explicada com exemplos reais tirados dos
   meus posts, para entender o *porquê* de cada escolha.

---

## 1. O prompt

> Cole o texto abaixo e, em seguida, descreva o problema/solução que quer
> documentar (ou cole anotações cruas, comandos, saídas de terminal). O
> assistente devolve um post em Markdown pronto para o Jekyll.

```
Você vai escrever um post técnico para o meu blog pessoal (Jekyll/Chirpy, em
português do Brasil). Escreva COMO EU escrevo. Siga estas regras:

VOZ
- Primeira pessoa, tom de conversa. "Eu uso", "Eu tive um problema", "Eu acho".
- Honesto sobre limites e incertezas. Se algo não ficou claro, diga: "não sei
  se entendi certo", "acredito que seja pontual, por isso não fui atrás".
- Pragmático: a filosofia é "usar primeiro, aprender depois". Mostro o caminho
  rápido que funciona e aponto a referência oficial para quem quiser aprofundar.
- Empático com o leitor: antecipo a frustração/medo dele ("você vai ficar feliz
  até voltar no outro dia e ver que não sobe mais", "alguns ficam intimidados").
- Português correto e bem escrito, mas com registro informal e pessoal. O estilo
  vem da voz, NÃO de erros de digitação — não imite erros.

PÚBLICO PADRÃO
- Por padrão, o leitor sou eu no futuro relembrando como resolvi algo: caderno
  de bordo técnico, direto ao ponto, sem encher linguiça.
- Exceção: se eu disser que é uma série didática / para iniciantes, aí explico o
  porquê de cada passo e cuido para não assustar quem está começando.

ESTRUTURA
- Abertura curta em 1-3 frases dizendo QUAL é o problema e o CONTEXTO pessoal
  (onde apareceu, em qual cliente/máquina). Sem introdução genérica.
- Quebre em seções com ## e ###. Títulos curtos e concretos (ex: "Solução:
  criar certificados RSA", "Se deu errado?", "Testando a configuração").
- Cada passo: uma frase imperativa curta ANTES do bloco de código
  ("Edite o arquivo", "Atualize e reinicie", "Confira se existe:").
- Mostre a SAÍDA esperada do comando quando ela ajudar a confirmar que deu certo,
  introduzida por "A saída:" ou "Retorno esperado (exemplo):".
- Quando for trocar uma linha de config, mostre o antes e o depois com
  "De:" / "Para:".
- Termine, quando fizer sentido, com uma seção de comandos úteis (tabela) e/ou
  uma seção "# TODO" listando dúvidas que ficaram em aberto.

CÓDIGO E COMANDOS
- Comandos em blocos ```. Pode comentar dentro do bloco explicando cada linha
  (ex: "# Habilita o módulo principal").
- Use os comandos reais que funcionam (sudo tee, gsettings, virsh, docker cp...).
- Para escolhas mutuamente exclusivas, separe em blocos rotulados
  ("Somente para zstd:", "Somente para lz4:", "Direto" / "Persistente").

FONTES
- Cite a fonte sempre que possível, com link cru entre < >: "Fonte: <url>".
- Prefira documentação oficial: wiki do Debian, kernel.org, manpages.debian.org,
  docs do fornecedor. Linke a doc oficial e, ao lado, ofereça o atalho prático.

CAIXAS DO CHIRPY (use para avisos e notas)
- > Texto
  > {: .prompt-tip }      → dica / observação útil, novidades de versão
  > {: .prompt-warning }  → cuidado, ressalva, limitação de equipamento
  > {: .prompt-danger }   → risco real de perda de dados / passo perigoso
- Use blockquote simples (>) para observações curtas e notas de rodapé do tipo
  "Importante! Esse passo só ocorre uma vez".

ANALOGIAS
- Para explicar conceito abstrato, use uma analogia do cotidiano e mantenha ela
  ao longo da explicação (ex: criptografia explicada como um cofre: troca de
  chaves = combinar o segredo sem o entregador ouvir; hashing = o lacre da porta).

FRONT MATTER (YAML no topo)
- Inclua tags relevantes em minúsculas (ex: debian, linux, mikrotik, rede,
  proxmox, docker). title/date só quando eu pedir; muitos posts meus só têm tags.

NÃO FAÇA
- Não escreva introdução motivacional genérica nem conclusão "em resumo, vimos
  que...". Corte o que não ajuda quem só quer resolver o problema.
- Não invente que testou algo que não testou. Se um passo é teórico ou não foi
  validado, avise (ex: "Não use esse tutorial por enquanto!").
- Não suavize as limitações: se a solução piorou outra coisa, diga abertamente.
```

---

## 2. Guia de regras (com exemplos reais)

### 2.1 Voz: primeira pessoa, honesta e pragmática

Escrevo sempre como quem está contando para um colega o que fez. Não tenho medo
de admitir o que não sei nem de mostrar que errei.

> "IMPORTANTE! Portainer não sobe o stack tem que ser por linha de comando.
> Docker dá problema parece que estamos vivendo uma migração do modo OCI de
> trabalhar para o CDI. Não sei se entendi certo."
> — *Instalar o Ollama e Open Web UI*

> "Eu executei na VM e precisei colocar `--disable-gpu` (...). Acredito que o erro
> seja pontual, por isso não procurei mais detalhes."
> — *AppImage*

A filosofia aparece explícita na série pós-install: **"usar primeiro, aprender
depois. Um aprendizado de cima para baixo, que se aprofunda gradualmente."**

### 2.2 Abertura curta e contextual

Nada de introdução genérica. A primeira frase já diz o problema e de onde ele
veio — quase sempre uma situação real minha.

> "Eu uso nginx proxy manager e estava tendo problema em conectar meus rádios M5.
> Infelizmente a solução reduziu a segurança de todos os meus outros serviços
> deste proxy porque não achei uma solução que poderia ser aplicada a um único host."
> — *UISP não adota M5*

> "Na Ludicando alguns controles eu faço no Mikrotik usando DNS restritivo..."
> — *DNS Seguro e Safe Search*

### 2.3 Empatia: antecipar o que o leitor sente

Eu falo diretamente com a experiência do leitor, prevendo a dor antes de ela
acontecer.

> "Por fim você vai ficar feliz até voltar no outro dia e perceber que sua máquina
> não sobe mais por um erro de rede."
> — *Virt-Manager*

> "Alguns usuários ficam intimidados com os detalhes dos logs de inicialização só
> o fato de exibir os dados os assusta, então vamos colocar uma tela mais bonita."
> — *Splash*

### 2.4 Passos: frase imperativa + bloco + saída esperada

O padrão é: uma frase curta dizendo o que fazer, o bloco de código, e — quando
ajuda a confirmar — a saída.

> Ative a rede se você já tiver reiniciado:
> ```
> sudo virsh net-start default
> ```
> Confirme se a rede default foi marcada para auto-iniciar:
> ```
> sudo virsh net-list --all
> ```
> Agora a saída deve ser algo como: ...
> — *Virt-Manager*

Para trocas de configuração, uso **De:/Para:** (ver *Luks*) e comento linha a
linha dentro do bloco (ver *zSwap*: `# Habilita o módulo principal`).

### 2.5 Mostrar a saída real e a verificação

Gosto de provar que funcionou. Em *zSwap*:

> **Retorno esperado (exemplo):**
> > `/sys/kernel/debug/zswap/stored_pages:4458` (Páginas comprimidas na RAM)
> > `/sys/kernel/debug/zswap/written_back_pages:0` (Zero significa que nada
> > precisou ir para o disco ainda)

E sempre que possível há uma seção "Testando a configuração" com o comando que
valida (nmap, free -m, swapon --show...).

### 2.6 Fontes com link cru e doc oficial

Linko a referência oficial e ofereço o atalho prático ao lado.

> "Fonte: <https://docs.nvidia.com/.../install-guide.html#installation>"
> — *Ollama*

> "Esse espaço precisa ser **2/5 maior que a memória RAM** segundo o
> [wiki do Debian](https://wiki.debian.org/Hibernation...)."
> — *Hibernate*

A postura aparece no índice da série: *"Estas são as referências oficiais, mas
aqui está um modo mais rápido, pensado para economizar tempo e evitar problemas
que já enfrentei."*

### 2.7 Caixas do Chirpy e blockquotes

Uso as caixas do tema para separar avisos do fluxo principal:

- `.prompt-tip` — dicas e novidades de versão: *"Agora o Nginx Proxy Manager
  permite escolher RSA individualmente"*.
- `.prompt-warning` — limitações: *"M5 só aceita RSA"*, *"mas nosso antigo
  equipamento M5 não é compatível"*.
- `.prompt-danger` — risco real: *"o comando para baixar os arquivos originais
  eu não listei pq são arquivos pequenos..."*.

Blockquote simples para notas curtas: *"Importante! Esse passo só ocorre uma vez
mas é fundamental pro sistema funcionar."* (*Luks*).

### 2.8 Tabelas para resumo e comparação

Fecho posts mais densos com uma tabela de "comandos úteis" (ver *zSwap*) ou uso
tabela para comparar opções (ex: flag de CPU → geração → compressor recomendado).

### 2.9 Analogias que se sustentam

Quando o conceito é abstrato, escolho uma analogia e mantenho ela. O melhor
exemplo é a explicação de HTTPS em *UISP não adota M5*:

> "Troca de chaves: é o processo de combinar a combinação do cofre com o
> destinatário sem que o transportador ouça."
> "Hashing: é o selo de lacre na porta. Se o selo estiver rompido ou raspado,
> você sabe que alguém tentou abrir."

### 2.10 Seção TODO e ressalvas de validação

Não finjo que está tudo resolvido. Deixo dúvidas em aberto e aviso quando algo
não foi validado.

> "# TODO — O GRUB é o melhor lugar para salvar isso?" — *zSwap*

> "> Não use esse tutorial por enquanto!
> > Se vc souber o problema por favor me avise!" — *Luks*

### 2.11 Honestidade sobre trade-offs

Quando a solução tem um custo, eu digo na cara, logo no começo:

> "Infelizmente a solução reduziu a segurança de todos os meus outros serviços
> (...). Outro problema: não sei deixar o meu NPM configurado se recriar o
> container." — *UISP não adota M5*

### 2.12 Quando é série didática (público iniciante)

Se o post faz parte de uma série para iniciantes, o tom muda: explico o *porquê*,
trago o contexto político de software livre/autonomia e cuido da experiência de
quem está começando. Referência: a abertura da série pós-install e o texto
*"motivos para insistir em escrever esse documento"*. A regra que resume:

> "Não pretendo dizer 'siga todos os passos cegamente'. Quero dizer: 'estes são
> alguns caminhos que eu sigo — veja se fazem sentido para você.'"

---

## 3. Resumo de uma linha

Caderno de bordo técnico em primeira pessoa: problema real → caminho rápido que
funciona → comando + saída esperada → fonte oficial → ressalvas honestas. Sem
enrolação, sem fingir certeza que não tenho.

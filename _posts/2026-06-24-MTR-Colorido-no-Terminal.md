O MTR é uma ferramenta para diagnóstico de rede, uni ping e traceroute. 

Para obter um realce de sintaxe  e deixar colorido podemos integrar a saída do MTR com o **ChromaTerm (ct)**.

## Instalação do MTR

O pacote `mtr-tiny` é a versão para terminal. Se você preferir a versão com interface gráfica (GTK), o pacote se chama apenas `mtr`.

```bash
sudo apt update && sudo apt install mtr-tiny
```
## Instalação do ChromaTerm

No Debian, para instalar pacotes Python utilitários utilize o `pipx`.

```bash
# Atualiza a lista e instala o pipx se não estiver presente
sudo apt update && sudo apt install pipx -y && pipx ensurepath
```

_Nota: Se instalou o pipx agora, feche e abra o terminal novamente para aplicar as alterações de path._

```
# Instala o ChromaTerm de forma isolada
pipx install chromaterm
```

## Utilização Prática

O funcionamento é direto. Basta direcionar o fluxo de saída do comando para o executável do ChromaTerm utilizando o pipe.

```bash
mtr github.com | ct
```

## Criando um Atalho Permanente

Se preferir que a coloração ocorra de forma transparente sempre que chamar a ferramenta, configure uma função no interpretador de comandos.

```bash
# Adiciona o alias permanente no perfil do Bash
echo -e "\nmtr() {\n    command mtr \"\$@\" | ct\n}" >> ~/.bashrc && source ~/.bashrc
```

O `"$@"` faz o Bash pegar tudo o que você digitar depois de `mtr` e passar direto para o comando real. O prefixo `command` evita que a função entre em um loop infinito chamando a si mesma.

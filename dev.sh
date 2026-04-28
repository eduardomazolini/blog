#!/bin/bash

# 1. Verificação de sanidade (Estado atual)
[ -d ".bundle" ] && echo "--- Cache de Gems encontrado em .bundle/"
[ -f "Gemfile.lock" ] && echo "--- Gemfile.lock preservado para acelerar o boot."

# 2. Build Condicional
# Verifica se a imagem já existe antes de buildar
if [[ "$(podman images -q jekyll-trixie 2> /dev/null)" == "" ]]; then
  echo "--- Imagem não encontrada. Buildando..."
  podman build -t jekyll-trixie .
else
  echo "--- Imagem jekyll-trixie já existe. Pulando build."
fi

# 3. Execução com Cache
# Removida a limpeza agressiva do início. 
# Adicionado volume para as Gems instaladas não sumirem.
# ... (partes anteriores do script iguais)

# 3. Execução com Cache Local
podman run --rm -it \
  -p 4000:4000 \
  -v "$PWD:/srv/jekyll:Z" \
  --userns=keep-id \
  jekyll-trixie \
  bash -c "bundle config set --local path '.vendor/bundle' && bundle install && bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling --trace --verbose"
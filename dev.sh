#!/bin/bash

# 1. Gera a imagem local (apenas uma vez)
podman build -t jekyll-trixie .

# 2. Executa o ambiente
podman run --rm -it \
  -p 4000:4000 \
  -v "$PWD:/srv/jekyll:Z" \
  --userns=keep-id \
  jekyll-trixie \
  bash -c "bundle install && bundle exec jekyll serve --host 0.0.0.0 --watch --force_polling"
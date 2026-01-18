# Usando Ruby 3.3 (mais moderno e padrão no Trixie) sobre Debian 13 Slim
FROM docker.io/library/ruby:3.3-slim-trixie

# Instala dependências essenciais
# build-essential para compilar Gems nativas
# git porque o tema Chirpy usa para metadados de posts
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/jekyll

# Configura o bundle para instalar as gems localmente na pasta .vendor
RUN bundle config set --global path '.vendor/bundle'

EXPOSE 4000
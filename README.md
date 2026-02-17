# blog (Jekyll starter)

Este repositório contém um site Jekyll mínimo pronto para publicar no GitHub Pages com domínio customizado.

Como usar (resumo):
1. Clone/adicione estes arquivos ao repo `eduardomazolini/blog`.
2. Ajuste o arquivo `CNAME` (já presente) se precisar mudar o domínio.
3. Faça push para a branch `main`.
4. Configure DNS: crie um registro CNAME para `blog2` apontando para `eduardomazolini.github.io`.
5. Em Settings → Pages do repositório, escolha a source `main` / root (se necessário) e aguarde o certificado HTTPS.

Testar localmente:
- Instale Ruby + Bundler
- `bundle install`
- `bundle exec jekyll serve`
- Acesse `http://localhost:4000`

Migração para domínio final:
- Quando quiser usar `blog.mazolini.com.br`, atualize o arquivo `CNAME` para conter `blog.mazolini.com.br` e atualize o CNAME no DNS.


```
podman build -t jekyll-trixie .
```

```
podman run --rm -it \
  -p 4000:4000 \
  -v "$PWD:/srv/jekyll:Z" \
  --userns=keep-id \
  -e BUNDLE_PATH=/srv/jekyll/.vendor/bundle \
  -e GEM_HOME=/srv/jekyll/.vendor/bundle \
  localhost/jekyll-trixie:latest \
  bash -c "bundle lock --add-platform x86_64-linux && bundle install && bundle exec jekyll serve --watch --force_polling --host 0.0.0.0"
```

podman run --rm -it \
   -p 4000:4000   \
   -v "$PWD:/srv/jekyll:Z" \
   --userns=keep-id \
   -e BUNDLE_PATH=/srv/jekyll/.vendor/bundle \
   -e GEM_HOME=/srv/jekyll/.vendor/bundle \
   docker.io/jekyll/jekyll \
   bash -c "bundle install && bundle exec jekyll serve --watch --force_polling"
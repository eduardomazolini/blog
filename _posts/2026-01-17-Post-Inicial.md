---
layout: post
title: "Meu primeiro post"
date: 2026-01-17 10:00:00 -0300
categories: [pessoal]
tags: [introdução, exemplo]
excerpt: "Primeiro post do meu blog usando Jekyll e GitHub Pages."
comments: true

show_alert: true
alert_text: "Conteúdo gerado por lógica Liquid"

---

# Este é um post de exemplo em Markdown.

Eu vou manter o exemplo abaixo até pra lembrar quando publiquei este blog usando essa tecnologia.
Eu vim do Blogger e to migrando as postagens para cá.


- Código:

```js
console.log("Olá, Mazolini!");
```

- Para imagens, coloque em `assets/images/` e referencie com: `![alt](/assets/images/jekyll.jpeg)`

![Logo do Jekyll](/assets/images/jekyll.jpeg)


# A seguir sintax liquid

```liquid
{% raw %}{% include alert-warning.md %}{% endraw %}
```


{% include alert-warning.md %}

## Algumas variáveis

site
```
{% raw %}{{ site | jsonify }}{% endraw %}

{{ site | jsonify }}
```

layout
```
{% raw %}{{ layout | inspect }}{% endraw %}
```
---

{{ layout | inspect }}

---

page
```
{% raw %}{{ page | jsonify }}{% endraw %}
{{ page | jsonify }}
```

site.posts[0]
```
{% raw %}{{ site.posts[0] | jsonify }}{% endraw %}
{{ site.posts[0] | jsonify }}
```

jekyll
```
{{ jekyll | jsonify }}
```

content
```
{{ content }}
```

paginator (se ativo)
```
{{ paginator }}
```

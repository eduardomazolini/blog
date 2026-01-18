// Node script: gera arquivos em /tags/{tag}.md para cada tag encontrada nos _posts
// Uso:
//   npm init -y
//   npm install gray-matter
//   node tools/generate-tags.js
//
// Isso cria/atualiza arquivos em ./tags/<tag>.md com front matter:
// layout: tag
// tag: <tagname>
// permalink: /tags/<tagname>/

const fs = require('fs');
const path = require('path');
const matter = require('gray-matter');

const postsDir = path.join(__dirname, '..', '_posts');
const tagsDir = path.join(__dirname, '..', 'tags');

if (!fs.existsSync(tagsDir)) fs.mkdirSync(tagsDir);

const files = fs.readdirSync(postsDir).filter(f => f.endsWith('.md') || f.endsWith('.markdown'));

const tagSet = new Set();

files.forEach(file => {
  const content = fs.readFileSync(path.join(postsDir, file), 'utf8');
  try {
    const parsed = matter(content);
    const tags = parsed.data.tags;
    if (Array.isArray(tags)) {
      tags.forEach(t => tagSet.add(String(t).trim()));
    } else if (typeof tags === 'string') {
      tagSet.add(tags.trim());
    }
  } catch (e) {
    console.warn('Erro lendo front-matter de', file, e.message);
  }
});

tagSet.forEach(tag => {
  const slug = encodeURIComponent(tag.toLowerCase().replace(/\s+/g, '-'));
  const filename = path.join(tagsDir, `${slug}.md`);
  const body = `---
layout: tag
tag: "${tag}"
title: "Posts com a tag: ${tag}"
permalink: /tags/${slug}/
---

Gerado automaticamente. Lista de posts com a tag "${tag}".
`;
  fs.writeFileSync(filename, body, 'utf8');
  console.log('Escrito', filename);
});

console.log('Concluído. Execute git add tags/* && git commit -m "Gera páginas de tags" && git push');

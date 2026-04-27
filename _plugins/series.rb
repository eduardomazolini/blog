## order e slug
# A idéia era ter
# _series como a coleção
# <nome da series> 
# index e 01-capitulos
# _series/debian/capitulo
#
# mas não deu certo to salvando no git só pra não perder 

Jekyll::Hooks.register :documents, :post_init do |doc|
  next unless doc.collection.label == "series"

  parts = doc.relative_path.split('/')

  # garante que está dentro de uma subpasta
  if parts.length > 2
    serie = parts[1]
  else
    # fallback para evitar crash
    serie = "misc"
  end

  doc.data['serie'] = serie
  puts "--- DEBUG SERIES ---"
  puts "Path Absoluto: #{doc.path}"
  puts "Path Relativo: #{doc.relative_path}"
  puts "--------------------"
  # não processa index
  if doc.basename_without_ext == "index"
    doc.data['order'] = 0
  end

  name = doc.basename_without_ext

  # extrai número (ordem)
  if name =~ /^(\d+)[-_](.*)$/
    order = $1.to_i
    clean = $2
  else
    order = 999
    clean = name
  end

  # slug limpo
  slug = clean
    .downcase
    .gsub(/[^\p{Alnum}\- ]/, '')
    .gsub(' ', '-')

  # título limpo
  title = clean
    .gsub('-', ' ')
    .split.map(&:capitalize).join(' ')

  doc.data['order'] ||= order
  doc.data['slug'] ||= slug

  # só sobrescreve title se não foi definido manualmente
  if doc.data['title'].nil? || doc.data['title'] == name
    doc.data['title'] = title
  end

  puts "[series] #{serie} | #{slug}"
end

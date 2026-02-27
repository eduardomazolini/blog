---
tags: [linux]
---

Hoje recebi um notebook com a missão de deixar funcionando um linux.
De cara um problema, cade a / ?? rsrs. Cade a "/" e "?" ?
Penei, e achei só um cara dizendo que fez e colocou no blog mas o arquivo mesmo nada.
Então fiz também. Mas não vou dar o arquivo pronto não.

Estou usando uma distro baseada no CentoOS 5.2

1) Vamos configurar o layout do teclado:
O Arquivo a ser editado é o /etc/sysconfig/keyboard, o parâmetro deve ficar KEYTABLE="br-abnt2"
Note que o que esta entre parentes vai ser o nome do arquivo sem o .map.gz.

2) Alterar o arquivo br-abnt2.map.gz
Por segurança copiem esse arquivo pra outro lugar antes de alterar.
O arquivo que vamos alterar fica em /lib/kbd/keymaps/i386/qwerty/
Descompacte o arquivo com o comando ```gunzip br-abnt2.map.gz``` o arquivo .gz é apagado só fica o .map
Edite o arquivo e adicione as seguintes 2 linhas:
altgr keycode 16 = slash
altgr keycode 17 = question
Compacte novamente o arquivo com o comando ```gzip br-abnt2.map``` o arquivo .map é apagado só fica o .map.gz
3) Pra carregar sem precisar dar boot digite loadkeys br-abnt2

Observações:
O arquivo que alteramos inclui arquivos qwerty-layout.inc e linux-with-alt-and-altgr.inc da pasta /lib/kbd/keymaps/i386/include/
Entenda esses arquivos, eles foram fundamentais pro sucesso desta alteração.
Se vc não tiver usando outros softwares pra configurar sua console sugiro trocar o nome do arquivo alterado e usar esse mesmo nome no arquivo keyboard.

## Atualização 2026

Eu to comprando um teclado ergonômico e fui procurar algumas soluções.
Então vou deixar uma dica aqui [Kanata](https://github.com/jtroo/kanata).

Também to usando o ThinkPad e apesar dele ter uma tecla ao lado do alt gr de `/?` ela não funciona, essa tecla é reconhecida como `KEY_RIGHTCTRL`.

Eu arrumei a tecla criando o arquivo `/etc/udev/hwdb.d/90-teclado-abnt2-fix.hwdb`:
```
evdev:input:b*v*p*e*
 KEYBOARD_KEY_9d=ro
```

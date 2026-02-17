---
---

Hoje me surgiu a necessidade importar um DVD para o iPad.
Eu tentei usar o VLC mas sem muito sucesso lembrei de outro software mplayer/mencoder.
O site oficial do mplayer me parece ser [http://www.mplayerhq.hu](http://www.mplayerhq.hu/), mas não consegui acesso durante o dia.
Usei o site do sourceforge [MPlayer for Win32](http://sourceforge.net/projects/mplayer-win32/files/MPlayer%20and%20MEncoder/revision%2034401/MPlayer-athlon-svn-34401.7z/download) ao iniciar o processo recebi um erro sobre a falta da libfaac.dll para o codec de áudio.
Na hora achei a libfaac.dll [aqui](http://oss.netfarm.it/mplayer-win32.php), mas fui procurar mais para escrever este post. Achei o [fonte do faac](http://www.audiocoding.com/faac.html)  e neste uma indicação que o binário estaria no site [rarewares.org](http://www.rarewares.org/aac-encoders.php), para minha supresa o mesmo site que já havia baixado o binário do lame (encoder do mp3).

Ainda precisava saber quais parâmetros usar para o iPAD entender o vídeo, e faço questão de deixar a fonte [Blog Changing Bits](http://blog.mikemccandless.com/2010/07/encoding-videos-for-apple-ipadipod.html), aqui vou fazer um resumo em português.

Container: mp4
Video codec: h264
Audio codec: aac

Só que o vídeo que eu precisava tinha uma função especifica e eu precisava navegar entre os "capítulos" para repetir e pular partes.
Para fazer essa separação achei sobre o filtro de vídeo(-vf) **blackframe.** Mas também encostrei a opção do mplayer **-identify** que mostrava os pontos exatos das quebras existentes no original que pensei que me permitiria usar  **−force−key−frames**. Mas não obtive o feito esperado.
Gravei cada captitulo separado usando**dvd://2** **-chapter 2-2** depois 3-3 assim foi. Se alguem souber me avisa por favor.

Meu exemplo:


mencoder.exe dvd://2 -chapter 2-2 -o arquivo.mov -oac faac -faacopts br=160:mpeg=4:object=2:raw -channels 2 -srate 48000 -ovc x264 -x264encopts crf=30:vbv_maxrate=2500:nocabac:global_header:frameref=3:threads=auto:bframes=0:subq=6:mixed-refs=0:weightb=0:8x8dct=1:me=umh:partitions=all:qp_step=4:qcomp=0.7:trellis=1:direct_pred=auto -of lavf -lavfopts format=mp4

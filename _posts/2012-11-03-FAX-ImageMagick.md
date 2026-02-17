---
---

Por incrível que pareça FAX ainda é muito usado no Brasil.

Usando asterisk existem diversas formas para envia-los. Não é o foco deste post.

O que quero apresentar é como montar um arquivo para ser enviado.

Muitas vezes é necessário montar o conteúdo do fax de forma dinâmica, exemplo uma mala direta, um boleto bancário, uma lista personalizada.

Como fazer isso?

Eu achei como solução o ImageMagick ou seu fork GraphicsMagick.




Cada aplicação de fax tem seu formato especifico para envio.

Então vou comentar alguns ajustes que eu precisei fazer em imagens.

1) Redimencionar o tamanho do comprimento (o fax tem um "ponto" comprido) para fazer isso ajustei a proporção da imagem.

2) Para o fax não chegar de ponta cabeça eu o inverti antes do envio

3) O fax tem que ser em preto e branco.




O meu fax tinha uma imagem no inicio (cabeçalho) o texto principal e outra imagem no final (rodapé)




Consegui passo a passo e uma linha com tudo junto.

Aqui posto só a ideia, para entender toda a linha consulte o site dos softwares:







convert Header.bmp -filter spline -scale  100%x135%! -unsharp 0x1 -monochrome -colors 2 temp1.bmp




convert -pointsize 20 label:" " label:"         FAX para Teste" label:"         Segunda Linha" -extent 1728x -monochrome -colors 2  -append -flip temp2.bmp




convert Footer.bmp -filter spline -scale  100%x135%! -unsharp 0x1 -monochrome -colors 2 temp3.bmp




convert temp3.bmp temp2.bmp temp1.bmp -append -monochrome -colors 2 temp4.bmp-monochrome -colors 2  -flip   -append -compress Fax temp4.tif







convert Header.bmp -flip -filter spline -scale  100%x130%! -unsharp 0x1 -monochrome -colors 2 -pointsize 20 label:" " label:"         FAX para TESTE" label:"         Segunda Linha" -extent 1728x  -flip  -monochrome -colors 2 Footer.bmp -filter spline -scale  100%x130%! -unsharp 0x1 -monochrome -colors 2  -flip  -append -compress Fax temp4.tif

## Atualização 2026

Hoje as pessoas já esqueceram o modem e o FAX, entram em panico achando que as IAs estão criando vida e inventando uma linguá secreta, quando uma facilidade de comunicação entre agentes por áudio é implantada **GGWave** ou [**GibberLink**](https://pt.wikipedia.org/wiki/GibberLink)

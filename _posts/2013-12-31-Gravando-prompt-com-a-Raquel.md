---
tags: [asterisk, mac, say]
---

Hoje precisei gravar alguns prompt para um Asterisk e lembrei que o os-x possui a voz da Raquel.
A Raquel é uma das vozes para TTS em português mais antigas, nativa no mac.

Basta abrir um terminal e digitar:

```
echo 'Um dois três testando' | say -o teste
sox teste.aiff --encoding signed-integer --endian little --bits 16 --channels 1 --rate 8k teste-pcm.wav
```

Eu sei que o say pode formatar direto, mas não funciona com Asterisk.
O pcm tem que ter 128kbps e neste caso fica com 150kbps, já alaw e ulaw tem que ser raw não wav.
Tem um outro produto que trabalho que precisa do ulaw, no Brasil precisa do alaw como wav, neste caso deve funcionar bem não testei.

```
echo 'Um dois três testando' | say --data-format=ulaw@8000 -o teste-ulaw.wav
echo 'Um dois três testando' | say --data-format=alaw@8000 -o teste-alaw.wav
echo 'Um dois três testando' | say --data-format=I16@8000 -o teste-pcm.wav
```



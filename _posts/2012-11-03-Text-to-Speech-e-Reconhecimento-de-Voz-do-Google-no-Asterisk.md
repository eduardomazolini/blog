---
---

Estava procurando sobre TTS na internet quando achei o site abaixo:

http://zaf.github.com/asterisk-googletts/


Achei a ideia fantástica apesar de não saber sobre as implicações de licenças que a cercam.

Fui tentar colocar o script para funcionar no meu LAB mas tive diversos problemas que resolvi e listo aqui as soluções.

1) O modo como acessei o proxy:
```
$ua->proxy('http','http://dominio\\\usuario:senha@ip:80');
```

2) O Asterisk não conseguia achar o mpg123 em /usr/local/bin não descobri a causa. O usuário asterisk conseguia e executava normal no shell, mas dentro do programa não.

Esse foi um dos maiores problemas. Se alguém souber como corrigir isso bem eu agradeço, uso o elastix como base.

Fiz um link simbólico em ```/usr/bin```:
```
cd /usr/bin/
ln -s /usr/local/bin/mpg123 mpg123

3) o meu teste não estava correto tinha 2 erros:

a) faltava ": ".
b) o idioma é no formato do google não do Asterisk, portanto "pt-BR" não "pt_BR".
```

Arquivo ```./googletts.agi```
```
agi_request: googletts.agi
agi_arg_1: Teste
agi_arg_2: pt-BR
agi_arg_3: any
```

4) Existe uma linha no código que penso que foi colocada para testar passar argumentos na linha de comando e isso acaba limpando os args

Comentem com #.

Antes:
```
($AGI{arg_1}, $AGI{arg_2}, $AGI{arg_3}) = @ARGV;
```
Depois:
```
#($AGI{arg_1}, $AGI{arg_2}, $AGI{arg_3}) = @ARGV;
```

Para fazer o Reconhecimento de voz os mesmos problemas incluindo a instalação do FLAC que é necessário, mas nenhuma dificuldade adicional.

Fiz 2 alterações para atender minhas necessidades:

1) Ele fazia RecVoz só de 2 números. Não era o que eu queria.

Antes:
```
# Remove spaces between digits #
$response{utterance}  =~ s/(\d)\s(\d)/$1$2/g;
```

Depois:
```
# Remove spaces between digits #
# $response{utterance}  =~ s/(\d)\s(\d)/$1$2/g;
```

2) Não sendo números existia o problema da codificação em utf-8.

Antes:
```
$response{utterance}  = "$1";
$response{confidence} = "$2";
```

Depois:
```
$response{utterance}  = "$1";
utf8::decode($response{utterance});
$response{confidence} = "$2";
```

Também me ajudou muito na linha de comando executar:
```
*CLI> agi set debug on
```

Enquanto depurava o código acabei criando um problema, eu colocava pontos com:

```
print "NoOp $variavel \n";
checkresponse();
```

E me esquecia de colocar em baixo ```checkresponse();```

Quando chegava por exemplo no:
```
print "STREAM FILE $file \"$keys\"\n";
@response = checkresponse();
```

Voltava rápido pro extension e não tocava.
Ai eu colocava um sleep(4) funcionava e eu não entendia o por que. Então a cada NoOp coloque checkresponse(); pois fica a resposta no buffer.
Uma melhoria que caberia no código é a cada warn colocar um NoOp. Afinal no Asterisk não da pra ver o warn. Isso teria me ajudado a saber da dificuldade em achar o mpg123.

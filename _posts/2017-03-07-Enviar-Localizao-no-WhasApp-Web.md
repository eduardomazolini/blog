---
---

Todos os dias eu preciso enviar a latitude e longitude para os técnicos que vão abrir esta localização em seus celulares.

Eu sei que enviando o link abaixo do google maps funciona, mas tinha que ficar copiando concatenando e colando.

http://maps.google.com/maps?saddr=Current+Location&daddr=-22.5951525,-46.5446545

Então resolvi facilitar a minha vida.

Já uso inserir javascript em outras paginas, o conceito básico é:

#### 1) escreva um código
```
message="http://maps.google.com/maps?saddr=Current+Location&daddr=";
coord = window.prompt("Entre: Lat, lon");
function sendMessage(message) {
	InputEvent = Event || InputEvent;
	var evt = new InputEvent('input', {
		bubbles: true
	});
	var input = document.querySelector("div.input");
	input.innerHTML = message;
	input.dispatchEvent(evt);
	document.querySelector(".btn-icon").click();
}
if (coord != null) {
	message=message+coord
	sendMessage(message);
}
```



#### 2) Reduza ao máximo

Como vou salvar na barra de favoritos o legal é minificar:
https://jscompress.com/

#### 3) Acione a chamada

Então coloque o código dentro do seguinte texto:
javascript:(function(){blablabla})();
javascript:void(blablabla)


Resultado: 
```
javascript:(function(){function sendMessage(a){InputEvent=Event||InputEvent;var b=new InputEvent("input",{bubbles:!0}),c=document.querySelector("div.input");c.innerHTML=a,c.dispatchEvent(b),document.querySelector(".btn-icon").click()}message="http://maps.google.com/maps?saddr=Current+Location&daddr=",coord=window.prompt("Entre: Lat, Lon"),null!=coord&&(message+=coord,sendMessage(message));})();
```


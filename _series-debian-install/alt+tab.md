---
order: 1
---

# Alt+Tab
> Vou chamar de **Super** a tecla que normalmente fica entre Crtl e Alt, que em muitos teclados tem o logo do Windows.

Para editar as teclas de atalho navegue até:

Configurações -> Teclado -> Atalhos de Teclado -> Veja e personalize atalhos -> Navegação


### Alternar entre aplicativos

Apesar da janela de configuração mostrar Super+Tab, no terminal podemos ver que são 2 combinações:
- Super+Tab
- Alt+Tab

O **Super+Tab** mantem o modo linux de alternar entre aplicativos.

### Alternar entre janelas

Para funcionar o **Alt+Tab** igual no Windows ou seja alternar entre todas as janelas e não só entre aplicativos eu faço a alteração pela interface gráfica mesmo.


### Alternar entre janelas do mesmo applicativo

Mas também aproveito para ensinar que existe o **Alt+'(tecla acima do tab)** que alterna entre janelas do mesmo app.

### Opção por terminal

```
gsettings list-recursively org.gnome.desktop.wm.keybindings 
```
Quando vc altera pela interface grafica a opção backward é configurada automaticamente.
No terminal é preciso especificar a sequencia de atalho.

```
gsettings set org.gnome.desktop.wm.keybindings switch-applications "['<Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-applications-backward "['<Shift><Super>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows "['<Alt>Tab']"
gsettings set org.gnome.desktop.wm.keybindings switch-windows-backward "['<Shift><Alt>Tab']"
```


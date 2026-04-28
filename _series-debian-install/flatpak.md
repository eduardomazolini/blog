---
order: 3
---
# [Flatpak](https://flatpak.org/setup/Debian)

Para ativar o flatpak existe um tutorial simples no site oficial, lá tem a opção pra GNOME e KDE
Ao instalar o plugin do gnome ele já instala o flatpak como dependência.

```
sudo apt install gnome-software-plugin-flatpak
```

Precisa também configurar o repositório
```
flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

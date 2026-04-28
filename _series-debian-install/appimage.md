---
order: 4
---
# [AppImage](https://appimage.org/)

Alguns AppImages exigem [FUSE versão 2](https://github.com/AppImage/AppImageKit/wiki/FUSE) para ser executado. O AppImages mais recente tem a versão 3 do FUSE incorporada. Filesystem no Userspace (FUSE) é um sistema que permite que usuários não-root montem sistemas de arquivos.

> O site do FUSE recomenda uma alteração de repositório que não precisei fazer.

```
sudo apt install libfuse2t64
```

**[Gear Lever](https://gearlever.mijorus.it/)** organiza os AppImage:
```
sudo flatpak install flathub it.mijorus.gearlever
```

> VM
>
>Eu executei na VM e precisei colocar `--disable-gpu` nos parâmetros de um AppImage. Acredito que o erro seja pontual, por isso não procurei mais detalhes. Ativando **OpenGL** e **Aceleração 3D** também funcionou.

---
tags: [rascunho]
---

```
aplay -l
arecord -l
~/.asoundrc
pcm.!default {
  type asym
  playback.pcm "plughw: 2"
  capture.pcm "plughw: 1"
}
ctl.!default {
  type hw
  card 1
}

speaker-test -t wav
arecord -d 10 teste.wav
aplay teste.wav
```

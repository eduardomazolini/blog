
O problema é o espaço em disco usado pelas gravações.
A solução foi compactar os áudios e também aproveitei para limpar os arquivos vazios.

Não estava instalado e foi preciso instalar como pré-requisito o `bc` que será usado no script.
```
apt install -y bc
```

Criado script `/var/lib/asterisk/bin/convert_wav2mp3.sh` com o conteúdo:

```
#!/bin/bash
# A Script to Convert FreePBX call recordings from WAV to MP3
# Also updates the CDR database, for correct downloads through the web UI
# Version 1 - 2015/11/15
#
# Copyright Jaytag Computer Limited 2015 - www.jaytag.co.uk
#
# You may use or modify this script as you wish as long as this copyright
# message remains. Redistribution prohibited.
# Set the Asterisk Recording Directory
recorddir="/var/spool/asterisk/monitor"

# Delete empty files
find $recorddir -type f -empty -delete
# Delete files with short duration
for wavfile in `find $recorddir -name \*.wav`; do
if [ $(echo `soxi -D $wavfile` "==" 0 | bc -l) -eq 1 ];then rm -fv $wavfile;fi
done

# Start the Loop, store the path of each WAV call recording as variable $wavfile
for wavfile in `find $recorddir -name \*.wav`; do
# Make Variables from the WAV file names, stripping the file path with sed
wavfilenopath="$(echo $wavfile | sed 's/.*\///')"
mp3file="$(echo $wavfile | sed s/".wav"/".mp3"/)"
mp3filenopath="$(echo $mp3file | sed 's/.*\///')"
# Convert the WAV files to MP3, exit with an error message if the conversion fails
nice lame -q 0 "$wavfile" "$mp3file" && rm -frv $wavfile || { echo "$wavfile encoding failed" ; exit 1; }
# Update the CDR Database
mysql -u root -s -N -D asteriskcdrdb<<<"UPDATE cdr SET recordingfile='$mp3filenopath' WHERE recordingfile = '$wavfilenopath'"
# On-Screen display of variables for debugging/logging
# echo ""
# echo "File -------------------------------------------------------"
# echo "Wav File : " $wavfile
# echo "Wav No Path : " $wavfilenopath
# echo "MP3 File : " $mp3file
# echo "MP3 No Path : " $mp3filenopath
# echo "End File ---------------------------------------------------"
# echo ""
# End the Loop
done
```
FONTE: https://www.jaytag.co.uk/blog/freepbx-convert-wav-call-recordings-to-mp3

Salvar no crontab com `crontab -e` para executar todos os dias:
```
# m h  dom mon dow   command
0 0 * * * /var/lib/asterisk/bin/convert_wav2mp3.sh  >/dev/null 2>&1
```

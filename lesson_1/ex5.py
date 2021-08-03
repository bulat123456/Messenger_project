import subprocess
import chardet

yandex = ['ping', 'yandex.ru']
ping = subprocess.Popen(yandex, stdout=subprocess.PIPE)
for line in ping.stdout:
    result = chardet.detect(line)
    print(f'yandex.ru: {result}')
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

youtube = ['ping', 'youtube.com']
ping = subprocess.Popen(youtube, stdout=subprocess.PIPE)
for line in ping.stdout:
    result = chardet.detect(line)
    print(f'youtube.com: {result}')
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
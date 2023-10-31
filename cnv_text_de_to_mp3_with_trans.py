import sys
import time
from io import BytesIO
import translators as ts
from gtts import  gTTS

if len(sys.argv)!=2:
    print("Syntax: python cnv_text_de_to_mp3_with_trans.py file-de.txt")
    exit(1)
input_path = sys.argv[1]
with open(input_path,'r') as fpi:
    lines_de = fpi.readlines()

print(f"{input_path} contains {len(lines_de)} lines.")
with open(input_path+".mp3","w+b") as fpw:
    for i,line_de in enumerate(lines_de):
        if line_de and line_de.strip()!="" :
            audio_de = gTTS(line_de,lang='de')
            audio_de.write_to_fp(fpw)

            line_en = ts.translate_text(line_de, translator='google', from_language='de')
            audio_en = gTTS(line_en,lang='en')
            audio_en.write_to_fp(fpw)

        print(f"{i}. {line_de}:{line_en}")
        time.sleep(1)
        # break
# fpw.write()

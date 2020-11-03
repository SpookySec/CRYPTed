from spinners import Spinners
import sys
import time
import codecs
import cursor

def decode_utf_8_text(text):
    try:
        return codecs.decode(text, 'utf-8')
    except:
        return text


def encode_utf_8_text(text):
    try:
        return codecs.encode(text, 'utf-8')
    except:
        return text

CLEAR_LINE = '\033[K'

if sys.version_info.major == 2:
    get_coded_text = encode_utf_8_text
else:
    get_coded_text = decode_utf_8_text

def animate(frames, interval, name, iterations=4):
    for i in range(iterations):
        for frame in frames:
            frame = get_coded_text(frame)
            output = "\r{0} {1}".format(frame, name)
            sys.stdout.write(output)
            sys.stdout.write(CLEAR_LINE)
            sys.stdout.flush()
            time.sleep(0.001 * interval)

def load(string):
    try:
        cursor.hide()
        animate(Spinners.dots.value["frames"], Spinners.dots.value["interval"], string)
        print('\n')
    finally:
        cursor.show()
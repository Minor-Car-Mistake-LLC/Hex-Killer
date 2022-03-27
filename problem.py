#read hex data from file
from dataclasses import replace
import ffmpeg

video = input("Enter the name of the video file (with file extension): ")
output = input("Enter the name of the output file (without file extension): ")

#check if file extension is .avi
def check_extension(filename):
    if filename[-4:] == '.avi':
        return True
    else:
        return False

if check_extension(video) == False:
    #convert video to .avi
    ffmpeg.input(video).output(output + '.avi').run()

def read_hex(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data

#find a character in a string and replace it with another character
def replace_char(string, char_to_replace, replacement_char):
    return string.replace(char_to_replace, replacement_char)

#write hex data to file
def write_hex(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)

write_hex(output, replace_char(read_hex(output + '.avi'), b"b7", b"00000000"))
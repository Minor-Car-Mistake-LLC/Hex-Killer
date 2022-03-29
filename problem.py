#read hex data from file
from dataclasses import replace
import ffmpeg
import os
import random

video = input("Enter the name of the video file (with file extension): ")
output = input("Enter the name of the output file (without file extension): ")
#check if file extension is .avi
def check_extension(filename):
    global extension
    if filename.endswith(".avi"):
        extension = True
        return True
    else:
        extension = False
        return False

if check_extension(video) == False:
    #convert video to .avi
    ffmpeg.input(video).output(output + 'tmp.avi').run()
else:
    extension = True

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


if extension == True:
    filename = '.avi'
else:
    filename = 'tmp.avi'

#get most common character in the file
def most_common(lst):
    return max(set(lst), key=lst.count)

#convert the most common character to a byte object
def most_common_to_byte(most_common_char):
    return bytes([most_common_char])


byte = most_common_to_byte  (most_common(read_hex(video)))

write_hex(output + '.avi', replace_char(read_hex(video), byte, b"00000000"))
print(byte)

if extension == False:
    os.remove(output + 'tmp.avi')

from pathlib import Path
import ffmpeg

#function output: return a mp4 file to the test folder file path

'''I need to find a file somewhere on my computer, point to the file path and pass that file path as 
a pyhton object through to a function which converts the mp3 to aac or m4b'''

file_path = Path('file_storage/')
file_name = 'What_You_Saying_KLICKAUD.mp3'


#wrap in a try/except for empty file_name
#I need one ffmpeg.input at a time as the stream then I concatenate decode/encode and save as aac
def file_converter (file_location, *file_names:str):
   file_paths = [str(file_location).rstrip('/') + '/' +f for f in file_names]
   streams = [ffmpeg.input(f) for f in file_paths]
   ffmpeg.concat(*streams, v=0, a=1).output(str(file_location).rstrip('/') + '/output.m4b', acodec='aac').run()
   


file_converter (file_path, file_name, file_name)





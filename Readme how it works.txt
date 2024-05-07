the quickest way to get results is to:
1. drop the video you want to extract the text from into the input folder
2. run Double_Click_Me_To_RUN_video_to_text_extractor_In_Terminal.bat
3. hit enter on each input the terminal is asking you (like enter enter enter enter) ---> this means you added no video_path, no output_name, no frame_rate which sets it to use its default values.
4. what happens then is: it looks into the input folder for mp3 or mp4 video files and processes each one !!!!!if you have multible in the folder it process all of them.

5. when its completed you get the extracted text in the terminal and also in the output folder + the images in the ouput folder.



to adjust the frame rate the video will be processed do the same as above but enter your value at  frame_rate.


you also can use Double_Click_Me_To_OPEN_MiniConda_VENV_In_Terminal .bat
this opens the terminal and you can directly run the 
extract_fames.py

extract_fames.py takes this arguments
 parser.add_argument("--video_path", type=str, default=" ", help="Path to the video file")
    parser.add_argument("--output_name", type=str, default="output.txt", help="Name of the output text file")
    parser.add_argument("--frame_rate", type=int, default=2, help="Desired frame rate (in seconds) e.g. 1 means it takes each second of the video a image and extracts the text from it.")
    parser.add_argument("--tesseract_path", type=str, default=default_tesseract_path, help="Custom tesseract Path if you have pytesseract installed you also can use your custom pytesseract leave this empty and it will use its own.")
    parser.add_argument("--headline", type=str, default=headline, help="Here you can add a headline that will appear in the output text file on top of the text like headlines ussually do.")

to run it in the miniconda venv (virtual environment) you can do:
python extract_fames.py --video_path "D:\47\example_video.mp4" --output_text_file "output.txt" --frame_rate 2 --headline "this is a headline"

the headline will be the top line of the output.txt file and it defaults to "can you extract all code from the following text, fix it and print the complete code"
which i used to get some python code out of a video using a llm by pasting the complete output.txt into the prompt.

-------------------------EXAMPLE TEXT FROM A VIDEO----------------------------------------------------------------------------------------------------------------------------

can you extract all code from the following text, fix it and print the complete code

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 0
‘_—rs
Write a short summary of the Image description above:
The image is a depiction of Taylor Swift, a renowned American singer-songwr
iter and musician.
Ask a question about the image or type 'exit' to quit: what is she wearing?
> what is she wearing?
Image description:Taylor Swift She is wearing a green dress.
Write a short summary of the Image description above:
There's a captivating image that has caught our attention! It depicts none o
ther than Taylor Swift, who is looking radiant in her green dress. The color
choice complements her perfectly, making her stand out with grace and style
Ask a question about the image or type 'exit' to quit: what color is her eye
Sz
> what color is her eyes?
Image description:Taylor Swift She is wearing a green dress. Her eyes are bl
ue.
Write a short summary of the Image description above:
This image features pop sensation Taylor Swift, sporting a stunning green g
own. Her captivating blue eyes are visible in this snapshot, adding to her o
verall charm and appeal.
Ask a question about the image or type 'exit' to quit: does she have earring
?
> does she have earring?
Image description:Taylor Swift She is wearing a green dress. Her eyes are bl
ue. Yes, she has earring in her left ear.
Write a short summary of the Image description above:
Hey there! So I've got this image to describe for you. It's Taylor Swift, th
e singer we all know and love! In the picture, she is wearing a stunning gre
en dress that really brings out her eyes. Her eyes are blue - they're so vib
rant they could be the ocean on a sunny day. And don't forget those earrings
in her left ear; they add just the right touch of sparkle to an already stu
nning look!
Ask a question about the image or type 'exit' to quit: |
cE}

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 2
100% Local Tiny Al Vision Language Model (1.6B) - Very Impressive!
IB CAUsers\kris\Pythoriwstreamn\moondream\batchpy - Notepad++
Fle E& Search View Encoding Language Stings Toole Macro Run Pligine_ Window 7
@e°B@96/ XO |> (aajag SIBVWOKESO  w
vio, py Beane vatepy BA newt
from typing import List
import requests
import ffmpeg
import subprocess
import json
from moviepy.editor import CompositeAudioClip
from moviepy.editor import concatenate_audioclips
import cv2
import time
from pathlib import Path
from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip, AudioFileClip
# ANSI escape code for colors
PINK = '\@33[95m'
CYAN = '\@33[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\@33[92m"
RESET_COLOR = '\@33[@m'
# Initialize the OpenAI client with the API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
sdef mistral7b(user_input):
f streamed_completion = client.chat.completions.create(
model="local-model",
messagec=[

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 4
100% Local Tiny Al Vision Language Model (1.6B) - Very Impressive!
IB CAUsers\kris\Pythoriwstrearn\moondream\batch.py - Notepad++
Fle E§ Search View Encoding Language Stings Toole Macro Run Pligine Window 7
Ge B8@96/ XO |> \aajae SIBVWOKEE © w
iso, py OT eae E vatepy BIA newt
from typing import List
import requests
import ffmpeg
import subprocess
import json
from moviepy.editor import CompositeAudioClip
from moviepy.editor import concatenate_audioclips
import cv2
import time
from pathlib import Path
from faster_whisper import WhisperModel
from moviepy.editor import VideoFileClip, AudioFileClip
# ANSI escape code for colors
PINK = '\@33[95m'
CYAN = '\@33[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\033[92m"
RESET_COLOR = '\@33[@m'
# Initialize the OpenAI client with the API key
client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
de¥ mistral7b(user_input):
streamed_completion = client.chat.completions.create(
model="local-model",
messagec=l

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 6
BE CALs \Pytorivsteammoondeam\ batch -Netpad+
Fle Est Search View Encoding Language Stings Tole Macro un Plugin Win
@e e996 x0 b Qaaag STE WO KOS >
en 7 OTE wot O14 rent 8
22 | CYAN = '\@33[96m'
23 | YELLOW = '\@33[93m"
24 | NEON_GREEN = ‘'\@33[92m'
25 | RESET_COLOR = '\033[@m'
27 | # Initialize the OpenAI client with the API key
28 | client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
30 |cdef |mistral7b(user_input):
31 streamed_completion = client.chat.completions.create(
32 model="local-model",
33 |f messages=[
34 {"role": "system", "content": "Yau are a great writer."},
B5 {"role": "user", "content": user_input}
36 ],
37 stream=True # Enable streaming
38 )
ais)
40 full_response = ""
41 line_buffer = ""
43 for chunk in streamed_completion:
44 delta_content = chunk.choices[@].delta.content
46 if delta_content is not None:
47 line_buffer += delta_content
AR

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 8
BY CAUser sis \Pythonstreammcondreambatehpy - Notepads - 0
Fle Es Search View Encoding Language Stings Toole Macro Run Plgine_ Window 7 2
ae 8899 x0 (9 aajag SIBVmOKES © ®
iso, oy Bama walepy GIF newt
52 print(NEON GREEN + line + RESET_COLOR)
53 full_response += line + ‘\n'
54 line_buffer = lines[-1]
56 | if line_buffer:
57 print(NEON_GREEN + line_buffer + RESET_COLOR)
58 full_response += line_buffer
ae
60 return full_response
62 | # ANSI escape codes for colors, for styling the terminal output
63 | PINK = '\@33[95m'
64 | CYAN = '\@33[96m' i
65 | # ANSI escape codes for colors, for styling the terminal output
66 | PINK = '\@33[95m'
67 | CYAN = '\@33[96m'
68 | YELLOW = '\033[93m'
69 |;-NEON_GREEN = ‘\@33[92m"
7 ||RESET_COLOR = '\033[@m'
TA
72 | def process_images(folder_path: str) -> (TextModel, list):
73 model_path = snapshot_download("“vikhyatk/moondream1")
74 vision_encoder = VisionEncoder(model_path)
75 text_model = TextModel(model_path)
77 descriptions = [] # This will hold descriptions of all images

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 10
BY CAUser ss \Pythonstreammcondreambtchpy Notepads
Fle Es Search View Encoding Language Stings Toole Macro Run Pligine_ Window 7
ae B@9s XO |> \aajae SIBVWOKEEO vw
io, py Beare vatepy BA newt
UA
9a
CYAN = ‘\033[96m'
YELLOW = '\933[93m'
NEON_GREEN = ‘\033[92m’
RESET_COLOR = '\933[0m'
sdef process_images(folder_path: str) -> (TextModel, list):
model_path = snapshot_download("vikhyatk/mdondreams")
vision_encoder = VisionEncoder(model_path)
text_model = TextModel(model_path)
descriptions = [] # This will hold descriptions of all images
# Iterate over each file in the folder
for filename in os.listdir(folder_path):
i if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', ‘.gif')):
image_path = os.path.join(folder_path, filename)
image = Image.open(image_path)
# Optionally, display the image
# image. show()
image_embeds = vision_encoder (image)
descriptions. append(description)
return text_model, descriptions
sdef convert_mp4_to_mp3(mp4_file_path, mp3_file_path):
description = text_model.answer_question(image_embeds, “Identify the person in the image with thie

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 12
RB CAUser ss \Pythonatreayncondreambatehpy - Notepads
Fle Es Search View Encoding Language Stings Toole Macro Run Phigine_ Window 7
45° BH8e99 x0 (9 aajag 5 IBV mOKES © ca
vio, oy Oakey valepy BIA newt
aol}
edef
descriptions.append(description)
return text_model, descriptions
convert, mp4 to) mp3(mp4_file_path, mp3_file_path):
Convert an MP4 file to MP3 format using moviepy.
Args:
mp4_file_path (str): Path to the MP4 file.
mp3_file_path (str): Desired output path for the MP3 file.
Returns:
bool: True if conversion successful, False otherwise.
try:
# Load the MP4 file
video_clip = VideoFileClip(mp4_file_path)
# Extract audio from the video clip
audio_clip = video_clip.audio
# Write the audio to an MP3 file
audio_clip.write_audiofile(mp3_file_path)
# Close the clips
viden clin.close()

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 14
Be CAUseni ytorvstemimoondeamstchgy Notepads
Fle Est
Search View Enceding Language Settings Toole Macro Run Plugine Vin
Window 7
ae 88099 x0 |9 aajag 5 IBV meKaS © w
iso, py Beach E valepy A newt
alas)
ALAS)
116 ff
dials)
alps?)
1:23
tbady
131 fF
# Write the audio to an MP3 file
audio_clip.write_audiofile(mp3_file_path)
# Close the clips
video_clip.close()
audio_clip.close()
return True
except Exception as e:
print(f"An error occurred: {e}")
return False
def transcribe_chunk(model, file_path):
segments, info = model.transcribe(file_path, beam_size=7)
transcription = ‘ ‘'.join(segment.text for segment in segments)
return transcription
# Function to extract frames from video
‘def extract_frames(video_ path, output_folder, frame_interval=60):
if not os.path.exists(output_folder):
os.makedirs(output_folder)
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
nrint("Frror: Could nat anen viden.")

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 16
IB CAUsers\irs,\Python'ystream\moondream\batchpy - Notepad++
Fle Es Search View Encoding Language Stings Toole Macro Run Phigine_ Window 7
a5 8899 x0 | aajag Ss IBV mOKES © »
iso, py Beachy vatepy BF newt
116 fp
allt)
dle
ilsyy
audio_clip.close()
return True
except Exception as e:
print(f"An error occurred: {e}")
return False
sdef transcribe chunk(model, file_path):
segments, info = model.transcribe(file_path, beam_size=7)
transcription = ° ‘.join(segment.text for segment in segments)
return transcription
# Function to extract frames from video
def extract_frames(video_path, output_folder, frame_interval=60):
if not os.path.exists(output_folder):
os.makedirs(output_folder)
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
print("Error: Could not open video.")
return []
frame_count = @
extracted_frame_paths = []
while cap.isOpened():
ret. frame = can-.read()

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 18
IB CAUser2\irs, Python ystream\moondream\batchpy -Notepads-+
Fle Es Search View Encoding Language Stings Toole Macro Run Phigine_ Window 7
ae° 8899 x0 | aajag Ss IBVmOKkKES © »
iso, py Beachy valepy BF newt
116 fp
allt)
122.
2H
dls}
ilsyy
audio_clip.close()
return True
except Exception as e:
print(f"An error occurred: {e}")
return False
sdef transcribe _chunk(model, file_path):
segments, info = model.transcribe(file_path, beam_size=7)
transcription = ' '.join(segment.text for segment in segments)
return transcription
# Function to extract frames from video
sdef extract _frames(video_path, output_folder, frame_interval=60):
if not os.path.exists(output_folder): I
os.makedirs(output_folder)
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
print("Error: Could not open video.")
return []
frame_count = @
extracted_frame_paths = []
while cap.isOpened():
ret. frame = can-read()

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 20
WB CAUsers\irs, Python ystream\moondream\batchpy - Notepad++
Fle Es Search View Encoding Language Stings Toole Macro Run Phigine_ Window 7
a5 °BH8e9 x0 |9 aajag 5 IBV MOKES © »
iso, py Beare valepy BF newt
Ten
116 fp
abil)
122.
ilsyy
audio_clip.close()
return True
except Exception as e:
print(f"An error occurred: {e}")
return False
sdef transcribe_chunk(model, file_path):
segments, info = model.transcribe(file_path, beam_size=7)
transcription = ' '.join(segment.text for segment in segments)
return transcription
# Function to extract frames from video
sdef extract_frames(video_path, output_folder, frame_interval=60):
a if not os.path.exists(output_folder): :
os.makedirs(output_folder)|
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
print("Error: Could not open video.")
return []
frame_count = @
extracted_frame_paths = []
while cap.isOpened():
ret. frame = can-.read()

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 22
IB CAUser2\irs, Python ystream\moondream\batchpy Notepad++
Fle Es Search View Encoding Language Stings Toole Macro Run Phigine_ Window 7
a5 BH8e9 x0 | aajag 5 IBV mOKES © »
iso, py Beare valepy BF newt
Ten
116 fp
abil)
122.
ilsyy
audio_clip.close()
return True
except Exception as e:
print(f"An error occurred: {e}")
return False
‘def transcribe_chunk(model, file_path):
segments, info = model.transcribe(file_path, beam_size=7)
transcription = ' '.join(segment.text for segment in segments)
return transcription
# Function to extract frames from video
sdef extract_frames(video_path, output_folder, frame_interval=60):
a if not os.path.exists(output_folder): :
os.makedirs(output_folder)
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
print("Error: Could not open video.")
return []
frame_count = @
extracted_frame_paths = []
while cap.isOpened():
ret. frame = can-.read()

------------------------------------------------------------------ Video: D:\47\02\video_to_text_extractor\input\example_video.mp4 frame: 24
IB CAUsers\eis\Pythorysteamymoondh 7
Fle Eat Search View Encoding Language Settings Toole Macro Run Plugins Wi
Ge BH9e XO (9 aajag er Pat ra
vision. py @ batchpy BD valkpy OF new! @
142 | if frame_count % frame_interval =
143 frame_filename = f' {output ONC EATETETOU {frame_count}.jpg'
144 cv2.imwrite(frame_filename, frame)
145 extracted_frame_paths.append(frame_filename)
147 frame_count += 1
149 cap.release()
150 print(f"Frame extraction complete. {len(extracted_frame_paths)} frames extracted.")
151 return extracted_frame_paths
153 | # Main execution
154 video_path = 'C:/Users/kris_/Python/vstream/moondream/gram2.mp4'
155 | output_folder = "C:/Users/kris_/Python/vstream/moondream/images”
156 | mp3_file_path = "C:/Users/kris_/Python/vstream/moondream/sound.mp3"
157 | convert_mp4_to_mp3(video_path, mp3_file_path)
159 \sdef main():
160 # Choose your model settings
161 #model_size = "medium.en"
162 #model = WhisperModel(model_size, device="cuda", compute_type="float16")
163 #transcription = transcribe_chunk(model, mp3_file_path)
164 #print (transcription)
166 frame_paths = extract_frames(video_path, output_folder)
162 # Pracess imanes in the folder and ohtain descrintians

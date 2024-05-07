import os
import cv2
import pytesseract
import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
import sys
from datetime import datetime
from tqdm import tqdm

#self_filepath=os.path.dirname(os.path.abspath(__file__))
tesseract_exe_rel_path=r"\tesseract_ocr\tesseract.exe"
output_folder = r"\user_data\output"
input_folder=r"\user_data\input"
#default_headline="I want you to extract all python code from the following text and print the complete code mo matter if you find something that is unclear."
default_headline="can you extract all code from the following text, fix it and print the complete code"
default_frame_rate:int=2

#clear_existing_images(output_folder)
#print(self_filepath)
#test=os.path.abspath(__file__)
#print(test)

def remove_empty_lines(input_string:str):
    """
    Remove empty lines from a string.
    Example usage
    input_text = "Hello\n\nWorld\n\n\nPython"
    output_text = remove_empty_lines(input_text)
    print(output_text)    
    
    Args:
        input_string (str): Input string with empty lines.
    
    Returns:
        str: String with empty lines removed.
    """
    lines = input_string.split('\n')  # Split the input string into lines
    non_empty_lines = [line for line in lines if line.strip()]  # Filter out empty lines
    return '\n'.join(non_empty_lines)  # Join non-empty lines back into a string

def remove_empty_and_numeric_lines(input_string):
    """
    Remove empty lines and lines containing only numbers from a string.
    # Example usage
    input_text = "Hello\n123\n\nWorld\n456\n\n\nPython"
    output_text = remove_empty_and_numeric_lines(input_text)
    print(output_text)

    Args:
        input_string (str): Input string with empty and numeric lines.
    
    Returns:
        str: String with empty and numeric lines removed.
    """
    lines = input_string.split('\n')  # Split the input string into lines
    non_empty_lines = [line for line in lines if line.strip() and not line.strip().isdigit()]  # Filter out empty and numeric lines
    return '\n'.join(non_empty_lines)  # Join non-empty lines back into a string


import os

def count_existing_files(output_folder):
    """
    Count the existing files in the specified folder.
    
    Args:
        output_folder (str): Path to the folder containing files.
    
    Returns:
        int: Number of existing files in the folder.
    """
    file_count = 0
    if os.path.exists(output_folder):
        for file in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file)
            try:
                if os.path.isfile(file_path):
                    file_count += 1
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")
    
    return file_count

# # Example usage
# output_folder = "/path/to/your/folder"
# existing_files_count = count_existing_files(output_folder)
# print(existing_files_count)



def delete_existing_files(output_folder):
    """
    delete existing files in the specified folder.
    
    Args:
        output_folder (str): Path to the folder containing images.
    """
    if os.path.exists(output_folder):
        for file in os.listdir(output_folder):
            file_path = os.path.join(output_folder, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")






def extract_text_at_frame_rate( video_path:str="",
                                output_name:str="output.txt",
                                frame_rate:int=2, 
                                tesseract_path:str="", 
                                output_folder_path:str="",
                                headline:str=default_headline
                                )->str:
    """
    Extract text (including Python code) from video frames at a defined frame rate.
    The for loop in your script processes frames at the specified frame rate, not every frame of the video clip. Let me explain in more detail:

    The VideoFileClip object (clip) represents the entire video file. When you call clip.get_frame(t) inside the loop, it retrieves the frame at the given time t.
    The loop iterates from t = 0 to t = int(clip.duration) with a step size of frame_rate. This means it processes frames at regular intervals defined by the frame_rate.
    For example, if your video has a duration of 10 seconds and you set frame_rate = 2, the loop will process frames at 2-second intervals (i.e., frames at 0s, 2s, 4s, 6s, and 8s).
    Frames between these intervals are skipped, so not every frame in the video is processed. If you want to process every frame, you would need to adjust the loop accordingly (e.g., remove the step size).
    Remember that the choice of frame rate affects the trade-off between accuracy (processing more frames) and efficiency (processing fewer frames). Adjust it based on your specific requirements.
        


    Args:
        video_path (str): Path to the video file.
        output_text_file (str): Name of the output text file.
        frame_rate (int): Desired frame rate (in seconds). Default is 2 seconds.
        tesseract_path (str): Path to the Tesseract executable. by default it has "whereever you placed this package\tesseract_ocr\tesseract.exe"
        image_output_folder_path (str): the path where the extracted images will be saved.(Be aware if running multible times the images will get deleted each time it starts the process to prevent a mess)
    """

    output:str="nothing done."
    self_filepath=os.path.dirname(os.path.abspath(__file__))
    output_folder_path = self_filepath+output_folder 
    headline=default_headline

    if output_name=="empty":
        output_name="output.txt"
    output_name=add_file_ending(output_name,".txt")
    
    if output_folder_path=="": 
        output_folder_path = self_filepath+output_folder
    if tesseract_path=="":
        tesseract_path=self_filepath+tesseract_exe_rel_path
  
    file_count=count_existing_files(output_folder_path)
    if file_count>100:
        message="there are more than 100 files "+"("+str(file_count)+")"+" in the output folder: "+output_folder_path+ " do you want to delete this files? "+ "\n"+"To delete the files type y or yes to keep the files type n or no"
        result=yes_no_prompt(message)
        if result:

            delete_existing_files(output_folder_path)

    os.makedirs(output_folder_path, exist_ok=True)
    video_pathes=[]
    if video_path=="empty" or video_path=="":
        input_folder_path = self_filepath+input_folder
        video_pathes= search_files(input_folder_path)
        if len(video_pathes)>0:

            for i in range(len(video_pathes)):
                print("starting Extracting video: "+video_pathes[i] +" to: " +output_name+ " at a frame_rate of: " + str( frame_rate )+" with this Pytesseract: "+tesseract_path)
                result=extract_video_function( video_path=video_pathes[i],
                                                tesseract_path=tesseract_path,
                                                 output_name=output_name,
                                                frame_rate=frame_rate,
                                                 output_folder_path=output_folder_path,
                                                headline=headline,
                                            )
                print(result)
        else:
            print("No video found in input folder (make sure you put the video ()mp3 ormp4) into the input folder.")
    else:
        print("starting Extracting video: "+video_path +" to: " +output_name+ " at a frame_rate of: " + str( frame_rate )+" with this Pytesseract: "+tesseract_path)
        result=extract_video_function( video_path=video_path,
                                        tesseract_path=tesseract_path,
                                        output_name=output_name,
                                        frame_rate=frame_rate,
                                        output_folder_path=output_folder_path,
                                        headline=headline,
                                    )
        print(result)

    output=result
    return output


def extract_video_function(video_path:str="",
                           tesseract_path:str="",
                           output_name:str="",
                           frame_rate:int=2,
                           output_folder_path:str="",
                           headline:str=""
                           ):
    clip = VideoFileClip(video_path)

    # Initialize Tesseract OCR
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("Input Video Infos:"+ "\n"+ "length: " +str(clip.duration)+" frames, "+ "\n"+"size: "+str(clip.size[0]) +" x "+str(clip.size[1])+" pixel,"+ "\n"+"frame rate: " + str(clip.fps)+" fps.")
    save_date=create_save_date()
    # Create an empty string to accumulate extracted text
    all_extracted_text = headline+ "\n"
    list_of_extracted_frames=[]
    output_text_file_filename=remove_file_endings(output_name)
    print("the video is "+str(clip.duration)+"frames long."+" estimated predicted duration at 1 second per iteration = "+str((clip.duration/frame_rate)) +" seconds.")
    print("every "+ str(frame_rate) +" (th,nd....)  frame will be extracted.")
    #tqdm is doing the process bar magic
    for t in tqdm(range(0, int(clip.duration), frame_rate)):
        frame = clip.get_frame(t)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Extract text using Tesseract
        extracted_text_headline="------------------------------------------------------------------ "+"Video: "+video_path+" frame: "+str(t)
        extracted_text = pytesseract.image_to_string(gray_frame)
        #extracted_text=remove_empty_lines(extracted_text)
        extracted_text=remove_empty_and_numeric_lines(extracted_text)
        final_frame_text="\n" + extracted_text_headline + "\n" +extracted_text
        # Append extracted text to the accumulated string
        all_extracted_text += final_frame_text + "\n"
        list_of_extracted_frames.append(t)

        # Save the frame as an image with the frame number as the filename in the "image_output" folder
        image_filename=save_date+"_"+output_text_file_filename+ "_"+f"frame_{t}.jpg"
        image_file_path = os.path.join(output_folder_path, image_filename)
        cv2.imwrite(image_file_path, frame)
    # Save all extracted text to the output file
    text_file_name=save_date+"_"+output_name
    final_output_text_file_path = os.path.join(output_folder_path, text_file_name)
    #final_output_text_file_path=output_folder_path+save_date+"_"+output_text_file
    with open(final_output_text_file_path, "w") as text_file:
        text_file.write(all_extracted_text)

    txt_1:str=f"Saved extracted text at {frame_rate} second intervals to {output_name}"
    txt_2:str="extracted frames: "+str(list_of_extracted_frames)
    txt_3:str="this is the extracted text-----------------------------" +"\n"+"\n"+"\n"+"\n"+all_extracted_text
    output=txt_1 +"\n"+txt_2+"\n"+txt_3
    return output




def remove_file_endings(input_string):
    """
    Remove possible file endings from a string.
    
    Args:
        input_string (str): Input string that may contain file endings.
    
    Returns:
        str: String with possible file endings removed.
    """
    file_endings = [".txt", ".pdf", ".jpg", ".png", ".csv"]  # Define a list of common file endings
    for ending in file_endings:
        if input_string.lower().endswith(ending):
            input_string = input_string[:-(len(ending))]  # Remove the file ending if found
    return input_string

def add_file_ending(input_string, new_file_ending):
    """
    Add a file ending to a string if no file ending is present.
    
    Args:
        input_string (str): Input string that may or may not contain a file ending.
        new_file_ending (str): The file ending to add if no file ending is present.
    
    Returns:
        str: String with the new file ending added if no file ending was present.
    """
    file_endings = [".txt", ".pdf", ".jpg", ".png", ".csv"]  # Define a list of common file endings
    has_ending = False
    for ending in file_endings:
        if input_string.lower().endswith(ending):
            has_ending = True
    if not has_ending:
        input_string += new_file_ending  # Add the new file ending if no file ending was found
    return input_string

def yes_no_prompt(message):
    """
    # Example usage
        if yes_no_prompt("Do you want to continue?"):
            print("User chose to continue.")
        else:
            print("User chose to stop.")
    """
    while True:
        user_input = input(f"{message} (yes/no): ").lower()
        if user_input == 'yes' or user_input == 'y':
            return True
        elif user_input == 'no' or user_input == 'n':
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def search_files(folder_path):
    # Initialize an empty list to store file paths
    file_paths = []

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp3") or file.endswith(".mp4"):
                file_paths.append(os.path.join(root, file))

    return file_paths


def create_save_date() -> str:
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    return str(formatted_date)



if __name__ == "__main__":
    """Example usage:
    assuming the example_video.mp4 is saved in the same folder as the script itselve
    also can be somethin like "D:\47\example_video.mp4"
    python extract_fames.py --video_path "example_video.mp4" --output_text_file "output.txt" --frame_rate 2"""
    #setup the default stuff
    self_filepath=os.path.dirname(os.path.abspath(__file__))
    default_tesseract_path=self_filepath + tesseract_exe_rel_path
    output_folder_path = self_filepath+output_folder 
    headline=default_headline
    #print(default_tesseract_path)

    parser = argparse.ArgumentParser(description="Extract text from video frames")
    parser.add_argument("--video_path", type=str, default=" ", help="Path to the video file")
    parser.add_argument("--output_name", type=str, default="output.txt", help="Name of the output text file")
    parser.add_argument("--frame_rate", type=int, default=2, help="Desired frame rate (in seconds) e.g. 1 means it takes each second of the video a image and extracts the text from it.")
    parser.add_argument("--tesseract_path", type=str, default=default_tesseract_path, help="Custom tesseract Path if you have pytesseract installed you also can use your custom pytesseract leave this empty and it will use its own.")
    parser.add_argument("--headline", type=str, default=headline, help="Here you can add a headline that will appear in the output text file on top of the text like headlines ussually do.")
    args = parser.parse_args()



    result=extract_text_at_frame_rate(video_path=args.video_path, output_name=args.output_name, frame_rate=args.frame_rate, tesseract_path=args.tesseract_path,output_folder_path=output_folder_path,headline=args.headline)
    print(result)
    

#python extract_fames.py --video_path "D:\47\example_video.mp4" --output_text_file "output.txt" --frame_rate 2 --headline this is a headline
#python extract_fames.py
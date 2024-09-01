"""
Description:
This Python script performs [Text Extraction from video files].

Author: [Umocap]
Date: [07.05.2024]
Version:[0.0.1]
see tutorial on Youtube on my channel.
www.youtube.com/@Umocap

Usage:
- Ensure you have Python [Python 3.11.9] installed.
- Run the script by executing 'extract_fames.py' in the terminal.

Dependencies:
- [requirements.txt]

Example:
- [take a look into Double_Click_Me_To_RUN_video_to_text_extractor_Autonomous_at_Frame_Rate_01.bat here you can see the example usage.]

"""

import os
import cv2
import pytesseract
import argparse
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import datetime
from tqdm import tqdm
from typing import Union 
import shutil
from typing import List, Tuple
from token_counter import token_counter

#dealing with all the folders.
self_filepath:str=os.path.dirname(os.path.abspath(__file__))
counter = token_counter()
tesseract_exe_rel_path:str=r"\tesseract_ocr\tesseract.exe"
output_folder:str = r"\user_data\output"
output_folder_path_default:str=self_filepath+output_folder 
output_folder_old:str = r"\user_data\output_old"
output_folder_old_path_default:str=self_filepath+output_folder_old
input_folder:str=r"\user_data\input"
input_folder_path_default:str=self_filepath+input_folder
default_headline:str="Can you extract all code from the following text, fix it and print the complete code"
default_frame_rate:int=2
max_file_count:int=50


def extract_text_at_frame_rate( video_path:str="",
                                #output_name:str="output.txt",
                                frame_rate:int=2, 
                                tesseract_path:str="", 
                                output_folder_path:str="",
                                headline:str="",
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
    if output_folder_path=="" or output_folder_path=="empty": #if empty we use the default output folder
        output_folder_path = output_folder_path_default
    if headline=="empty" or headline=="":
        headline=default_headline

    
    if tesseract_path=="":
        tesseract_path=self_filepath+tesseract_exe_rel_path

    check_and_move_files(output_folder_path=output_folder_path,
                         destination_folder=output_folder_old_path_default,
                         threshold=max_file_count
                         )
    os.makedirs(output_folder_path, exist_ok=True)
    video_pathes=[]
    if video_path=="empty" or video_path=="":
        input_folder_path = self_filepath+input_folder
        video_pathes= search_files(input_folder_path)
        if len(video_pathes)>0:

            for i in range(len(video_pathes)):
                print("starting Extracting video: "+video_pathes[i] +" to: " +output_folder_path+ " at a frame_rate of: " + str( frame_rate )+" with this Pytesseract: "+tesseract_path)
                result=extract_video_function(  video_path=video_pathes[i],
                                                tesseract_path=tesseract_path,
                                                #output_name=output_name,
                                                frame_rate=frame_rate,
                                                output_folder_path=output_folder_path,
                                                headline=headline,
                                            )
                print(result)
        else:
            print("No video found in input folder (make sure you put the video ()mp3 ormp4) into the input folder.")
    else:
        print("starting Extracting video: "+video_path +" to: " +output_folder_path+ " at a frame_rate of: " + str( frame_rate )+" with this Pytesseract: "+tesseract_path)
        result=extract_video_function( video_path=video_path,
                                        tesseract_path=tesseract_path,
                                        #output_name=output_name,
                                        frame_rate=frame_rate,
                                        output_folder_path=output_folder_path,
                                        headline=headline,
                                    )
        print(result)

    output=result
    return output


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

def remove_empty_and_numeric_lines(input_string:str):
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

def remove_empty_numeric_2char_lines(input_string: str):
    """
    Remove empty lines, lines containing only numbers, and lines with only 2 characters (excluding white space) from a string.

    Args:
        input_string (str): Input string with empty, numeric, and 2-character lines.

    Returns:
        str: String with empty, numeric, and 2-character lines removed.
    """
    lines = input_string.split('\n')  # Split the input string into lines
    filtered_lines = [line for line in lines if len(line.strip()) > 2 and not line.strip().isdigit()]  # Filter out empty, numeric, and 2-character lines
    return '\n'.join(filtered_lines)  # Join non-empty lines back into a string




def count_existing_files(target_folder_path:str):
    """
    Count the existing files in the specified folder.
    
    Args:
        target_folder_path (str): Path to the folder containing files.
    
    Returns:
        int: Number of existing files in the folder.
    """
    file_count = 0
    if os.path.exists(target_folder_path):
        for file in os.listdir(target_folder_path):
            file_path = os.path.join(target_folder_path, file)
            try:
                if os.path.isfile(file_path):
                    file_count += 1
            except Exception as e:
                print(f"Error accessing {file_path}: {e}")
    
    return file_count

def delete_existing_files(target_folder_path:str):
    """
    delete existing files in the specified folder.
    
    Args:
        target_folder_path (str): Path to the folder containing images.
    """
    if os.path.exists(target_folder_path):
        for file in os.listdir(target_folder_path):
            file_path = os.path.join(target_folder_path, file)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

def delete_existing_image_files(target_folder_path: str):
    """
    Delete existing image files in the specified folder.
    this are the supported image file types: '.jpg', '.jpeg', '.png', '.gif', '.bmp'
    Args:
        target_folder_path (str): Path to the folder containing images.
    """
    if os.path.exists(target_folder_path):
        for file in os.listdir(target_folder_path):
            file_path = os.path.join(target_folder_path, file)
            try:
                if os.path.isfile(file_path) and (file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))):
                    os.remove(file_path)
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

# Example usage
target_folder = "path/to/your/folder"
delete_existing_image_files(target_folder)

def check_and_delete_files(target_folder_path: str, threshold: int) -> None:
    """
    Checks the number of existing files in the specified folder.
    If there are more than the specified threshold number of files, a notification will be displayed with the number of files and the folder path.
    The user will then be prompted to confirm if they want to delete those files by typing 'y' or 'yes'.
    If the user confirms, the files will be deleted.

    Args:
        target_folder_path (str): The path to the output folder.
        threshold (int): The threshold number of files to trigger the delete confirmation.

    Returns:
        None
    """
    file_count: int = count_existing_files(target_folder_path)
    if file_count > threshold:
        message: str = f"There are more than {threshold} files ({file_count}) in the output folder: {target_folder_path}. Do you want to delete these files?\n"
        message += "To delete the files, type 'y' or 'yes'. To keep the files, type 'n' or 'no'."
        result: Union[bool, None] = yes_no_prompt(message)
        if result:
            delete_existing_files(target_folder_path)

def move_files(source_folder: str, destination_folder: str) -> None:
    """
    Move files from the source folder to the destination folder.
    # Example usage
        source_folder = "path/to/source_folder"
        destination_folder = "path/to/destination_folder"
        move_files(source_folder, destination_folder)

    Args:
        source_folder (str): Path to the source folder containing files.
        destination_folder (str): Path to the destination folder where files will be moved.
    """
    if os.path.exists(source_folder):
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        
        for file_name in os.listdir(source_folder):
            source_path = os.path.join(source_folder, file_name)
            destination_path = os.path.join(destination_folder, file_name)
            try:
                if os.path.isfile(source_path):
                    shutil.move(source_path, destination_path)
                    print(f"Moved {file_name} to {destination_folder}")
            except Exception as e:
                print(f"Error moving {file_name}: {e}")

def check_and_move_files(output_folder_path: str, destination_folder: str, threshold: int) -> None:
    """
    Checks the number of existing files in the specified folder.
    If there are more than the specified threshold number of files, a notification will be displayed with the number of files and the folder path.
    The user will then be prompted to confirm if they want to move those files to another folder by typing 'y' or 'yes'.
    If the user confirms, the files will be moved to the destination folder.

    Args:
        output_folder_path (str): The path to the output folder.
        destination_folder (str): The path to the destination folder where files will be moved.
        threshold (int): The threshold number of files to trigger the move confirmation.

    Returns:
        None
    """
    file_count: int = count_existing_files(output_folder_path)
    if file_count > threshold:
        message: str = f"There are more than {threshold} files ({file_count}) in the output folder: {output_folder_path}. Do you want to move these files to {destination_folder}?\n"
        message += "To move the files, type 'y' or 'yes'. To keep the files, type 'n' or 'no'."
        result: Union[bool, None] = yes_no_prompt(message)
        if result:
            move_files(output_folder_path, destination_folder)

def replace_first_line(text: str, new_line: str) -> str:
    """
    # example
    original_text = "Original erster Zeile\nZweite Zeile\nDritte Zeile"
    new_first_line = "Dies ist die neue erste Zeile"
    updated_text = replace_first_line(original_text, new_first_line)
    print(updated_text)
    """
    
    lines = text.split('\n')
    lines[0] = new_line

    return '\n'.join(lines)

def count_exact_tokens(input_string: str) -> int:
    '''
    # Example:
    input_text = "This is an example text with exactly 8 tokens."
    token_number = count_exact_tokens(input_text)
    print("Exact number of tokens in the text:", token_number)

    '''
    # Splitting the input string based on spaces
    tokens = input_string.split()
    # Counting the number of tokens
    token_count = len(tokens)
    return token_count

def create_token_info_row(tokens_normal:int,tiktokens_openai:int)->str:
    token_info:str="tokens_normal count: "+str(tokens_normal) +" tiktokens_openai count: "+str(tiktokens_openai) +"        (tokens_normal is splitting the input string based on spaces. tiktokens_openai uses its own tiktoken repo for calculating tokens its something like this: 1 token ~= 4 chars in English. 1 token ~= ¾ words. 100 tokens ~= 75 words.)"
    return token_info


def remove_similar_text(frames: List[str]) -> Tuple[List[str], int]:
    '''
    # Example frames list (replace this with your actual list of text frames)
    frames: List[str] = ["Frame 1 text", "Frame 1 text", "Frame 2 text", "Frame 2 text", "Frame 3 text"]

    unique_frames, removed_count = remove_similar_text(frames)

    print("Unique Frames:")
    for frame in unique_frames:
        print(frame)

    print(f"\nNumber of text frames removed: {removed_count}")
    '''


    unique_frames: List[str] = []
    removed_count: int = 0
    prev_frame_text: str = None

    for frame_text in frames:
        if prev_frame_text is not None and frame_text == prev_frame_text:
            removed_count += 1
        else:
            unique_frames.append(frame_text)
        
        prev_frame_text = frame_text

    return unique_frames




def extract_video_function(video_path:str="",
                           tesseract_path:str="",
                           #output_name:str="",
                           frame_rate:int=2,
                           output_folder_path:str="",
                           headline:str=""
                           ):
    clip = VideoFileClip(video_path)
    output_name:str=os.path.basename(video_path)
    # Initialize Tesseract OCR
    if tesseract_path:
        pytesseract.pytesseract.tesseract_cmd = tesseract_path

    print("Input Video Infos:"+ "\n"+ "length: " +str(clip.duration)+" frames, "+ "\n"+"size: "+str(clip.size[0]) +" x "+str(clip.size[1])+" pixel,"+ "\n"+"frame rate: " + str(clip.fps)+" fps.")
    #creating some variables
    save_date=create_save_date()
    output_text_file_filename=remove_file_endings(output_name)
    output_text_file_filename=add_file_ending(output_text_file_filename,".txt")
    output_text_file_filename=save_date+"_"+output_text_file_filename
    final_output_text_file_path = os.path.join(output_folder_path, output_text_file_filename)
    cleaned_output_text_file_filename=output_text_file_filename+"_cleaned"
    cleaned_output_text_file_filename=add_file_ending(cleaned_output_text_file_filename,".txt")
    #cleaned_output_text_file_filename=save_date+"_"+cleaned_output_text_file_filename
    final_cleaned_output_text_file_path = os.path.join(output_folder_path, cleaned_output_text_file_filename)
    # Create an empty string to accumulate extracted text
    tokens_normal:int=0
    tiktokens_openai:int=0
    token_info:str=create_token_info_row(tokens_normal=tokens_normal,
                                         tiktokens_openai=tiktokens_openai,
                                         )
    #use default_headline if its empty:
    if headline=="":
        headline=default_headline
    #building the output text first the token info then the headline
    all_extracted_text:str=""
    all_extracted_text+=token_info
    all_extracted_text+= "\n"+ "\n"+ "\n"+headline+ "\n"
    
    list_of_extracted_frames=[]
    frames_texts_list: List[str] =[]
    print("the video is "+str(clip.duration)+"frames long."+" estimated predicted duration assuming 1 second per iteration = "+str((clip.duration/frame_rate)) +" seconds.")
    print("every "+ str(frame_rate) +" (th,nd....)  frame will be extracted.")
    #tqdm is doing the process bar magic
    for t in tqdm(range(0, int(clip.duration), frame_rate)):
        frame = clip.get_frame(t)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Extract text using Tesseract
        extracted_text_headline="------------------------------------------------------------------ "+"Video: "+video_path+" frame: "+str(t)
        extracted_text = pytesseract.image_to_string(gray_frame)
        #extracted_text=remove_empty_lines(extracted_text)
        #extracted_text=remove_empty_and_numeric_lines(extracted_text)
        extracted_text=remove_empty_numeric_2char_lines(extracted_text)
        frames_texts_list.append(extracted_text)
        final_frame_text="\n" + extracted_text_headline + "\n" +extracted_text
        # Append extracted text to the accumulated string
        all_extracted_text += final_frame_text + "\n"
        tokens_normal=count_exact_tokens(input_string=all_extracted_text)
        tiktokens_openai=counter.num_tokens_from_string(string=all_extracted_text)
        token_info=create_token_info_row(tokens_normal=tokens_normal,tiktokens_openai=tiktokens_openai)
        all_extracted_text=replace_first_line(text=all_extracted_text,new_line=token_info)
        list_of_extracted_frames.append(t)

        # Save the frame as an image with the frame number as the filename in the "image_output" folder
        image_filename=save_date+"_"+output_name+ "_"+f"frame_{t}.jpg"
        image_file_path = os.path.join(output_folder_path, image_filename)
        cv2.imwrite(image_file_path, frame)
        #save the updated text file (this could also be done after the for loop has ended,
                                    # but if the user quits the process before the for loop is completed no output is saved)
        with open(final_output_text_file_path, "w") as text_file:
            text_file.write(all_extracted_text)
    cleaned_frames_texts_list : List[str]=remove_similar_text(frames=frames_texts_list)
    cleaned_frames_string:str=""
    cleaned_token_info:str=create_token_info_row(tokens_normal=0,tiktokens_openai=0)
    cleaned_headline="------------------------------------------------------------------ "+"Video: "+video_path+" frame: "
    #cleaned_headline:str="------------------------------------------------------------------ "+"Video: "+video_path+"frame: unknown its cleaned"
    #start building the cleaned text version first the token info then the headline
    cleaned_frames_string+=cleaned_token_info+ "\n"
    cleaned_frames_string+="This is the cleaned string where similar fame text parts was removed"+ "\n"+ "\n"+ "\n"
    cleaned_frames_string+=headline+ "\n"
    
    for text in cleaned_frames_texts_list:
        cleaned_frames_string+= "\n"+cleaned_headline+ "\n"
        cleaned_frames_string+=text
    
    cleaned_tokens_normal:int=count_exact_tokens(input_string=cleaned_frames_string)
    cleaned_tiktokens_openai:int=counter.num_tokens_from_string(string=cleaned_frames_string)
    cleaned_token_info=create_token_info_row(tokens_normal=cleaned_tokens_normal,tiktokens_openai=cleaned_tiktokens_openai)
    cleaned_frames_string=replace_first_line(text=cleaned_frames_string,new_line=cleaned_token_info)
    with open(final_cleaned_output_text_file_path, "w") as text_file:
            text_file.write(cleaned_frames_string)
    txt_1:str=f"Saved extracted text at {frame_rate} second intervals to {output_name}"
    txt_2:str="extracted frames: "+str(list_of_extracted_frames)
    txt_3:str="this is the extracted text-----------------------------" +"\n"+"\n"+"\n"+"\n"+all_extracted_text
    output=txt_1 +"\n"+txt_2+"\n"+txt_3
    open_local_file_in_browser(final_cleaned_output_text_file_path)
    return output

import webbrowser

def open_local_file_in_browser(folder_path):
    '''
    # Example
    path = r'C:\path to your folder'

    open_local_file_in_browser(path)

    '''
    file_url = 'file:///' + folder_path
    webbrowser.open(file_url)




def remove_file_endings(input_string:str):
    """
    Remove possible file endings from a string.
    
    Args:
        input_string (str): Input string that may contain file endings.
    
    Returns:
        str: String with possible file endings removed.
    """
    file_endings = [".txt", ".pdf", ".jpg", ".png", ".csv", ".mp4", ".mp3", ".avi", ".mov"]  # Define a list of common file endings

    #file_endings = [".txt", ".pdf", ".jpg", ".png", ".csv",".mp4","mp3"]  # Define a list of common file endings
    for ending in file_endings:
        if input_string.lower().endswith(ending):
            input_string = input_string[:-(len(ending))]  # Remove the file ending if found
    return input_string

def add_file_ending(input_string:str, new_file_ending:str):
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

def yes_no_prompt(message:str):
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


def search_files(folder_path:str):
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
    #self_filepath=os.path.dirname(os.path.abspath(__file__))
    default_tesseract_path=self_filepath + tesseract_exe_rel_path
    output_folder_path = self_filepath+output_folder 
    headline=default_headline
    parser = argparse.ArgumentParser(description="Extract text from video frames")
    parser.add_argument("--video_path", type=str, default=" ", help="Path to the video file")
    #parser.add_argument("--output_name", type=str, default="output.txt", help="Name of the output text file")
    parser.add_argument("--frame_rate", type=int, default=2, help="Desired frame rate (in seconds) e.g. 1 means it takes each second of the video a image and extracts the text from it.")
    parser.add_argument("--tesseract_path", type=str, default=default_tesseract_path, help="Custom tesseract Path if you have pytesseract installed you also can use your custom pytesseract leave this empty and it will use its own.")
    parser.add_argument("--headline", type=str, default=headline, help="Here you can add a headline that will appear in the output text file on top of the text like headlines ussually do.")
    args = parser.parse_args()

    result=extract_text_at_frame_rate(video_path=args.video_path, 
                                      #output_name=args.output_name, 
                                      frame_rate=args.frame_rate, 
                                      tesseract_path=args.tesseract_path,
                                      output_folder_path=output_folder_path,
                                      headline=args.headline)
    print(result)
    
#extract_text_at_frame_rate()
#python extract_fames.py --video_path "D:\47\02\AI_video_to_text_extractor\user_data\input" --output_text_file "output.txt" --frame_rate 2 --headline this is a headline
#python extract_fames.py 
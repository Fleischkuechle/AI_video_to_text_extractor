import os

#dealing with all the folders.
self_filepath:str=os.path.dirname(os.path.abspath(__file__))
output_folder_old:str = r"\user_data\output_old"
output_folder_old_path_default:str=self_filepath+output_folder_old

def delete_existing_image_files(target_folder_path: str) -> str:
    """
    Delete existing image files in the specified folder and return a string with information about deleted files.
    Supported image file types: '.jpg', '.jpeg', '.png', '.gif', '.bmp'
    
    Args:
        target_folder_path (str): Path to the folder containing images.
        
    Returns:
        str: Information about the deleted image files.
    """
    deleted_files = []  # Initialize a list to store the names of deleted files

    if os.path.exists(target_folder_path):
        for file in os.listdir(target_folder_path):
            file_path = os.path.join(target_folder_path, file)
            try:
                if os.path.isfile(file_path) and (file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp'))):
                    os.remove(file_path)
                    deleted_files.append(file)  # Append the name of the deleted file
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")

    return f"Deleted files: {', '.join(deleted_files)}"  # Return a string with information about deleted files

if __name__ == "__main__":
    result:str=delete_existing_image_files(target_folder_path=output_folder_old_path_default)
    print(result)

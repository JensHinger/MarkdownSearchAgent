import os
import ollama
from model_description import FILE_FOLDER_JUDGE

def get_files_and_folders(keyword:str, path: str):
    if path == "":
        return "There was no path specified"
    if keyword == "":
        return "There was no keyword specified"

    files = get_files_in_folder(keyword, path)
    folders = get_folders(keyword, path)

    return {"files": files, "folders": folders}

def get_files_in_folder(keyword: str, path: str) -> list[str]:
    relevant_files = []

    directory_contents = os.listdir(path)

    for file_name in directory_contents:

        if os.path.isfile(path + file_name) and file_name[0] != ".":
            # Load file contents
            file = open(path+file_name, "r")
            file_contents = file.read()

            prompt = f'''
                Respond with only "yes" or "no", do not add any additional information.
                Does the file {file_name} or its content {file_contents} relate to the keyword {keyword}?
            '''

            res = ollama.chat(
                model=FILE_FOLDER_JUDGE,
                messages=[{"role": "user", "content": prompt}]
            )

            if "Yes" in res["message"]["content"]:
                relevant_files.append(path + file_name)

    return relevant_files if relevant_files else ["None"]

def get_folders(keyword: str, path: str) -> list[str]:
    relevant_folders = []

    directory_contents = os.listdir(path)

    for dir_name in directory_contents:

        if os.path.isdir(path + dir_name) and dir_name[0] != ".":

            prompt = f'''
                Respond only with "yes" or "no", do not add any additional information.
                Is the folder name {dir_name} in any way related to the keyword {keyword}?
                This could for example be that the keyword is a sub field of {dir_name} 
                or that the two topics are roughly related.
            '''

            res = ollama.chat(
                model= FILE_FOLDER_JUDGE,
                messages=[{"role": "user", "content": prompt}]
            )

            if "Yes" in res["message"]["content"]:
                relevant_folders.append(path + dir_name)

    return relevant_folders if relevant_folders else ["None"]
from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from utils import load_creds
import os

def generate_example_file(path, file_name):
    with open(path + file_name, 'w') as f:
        f.write('example content')
    print("Generated " +  path + file_name + " successfully.")

def check_file_exist(path, file_name):
    # check upload_temp.txt exist
    if not os.path.isfile(path + file_name):
        generate_example_file(path, file_name)

def upload_basic():
    """
    mimetype:
    https://stackoverflow.com/questions/11894772/google-drive-mime-types-listing
    """
    try:
        creds = load_creds()
    except:
        print("Token is expired please reauthorate.\n")
        os.remove("token.json")
        print("token.json has been removed.\n")
        creds = load_creds()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        path = ""
        file_name = "upload_temp.txt"
        mimetype = "text/plain"
        file_metadata = {'name': file_name}
        check_file_exist(path, file_name)
        media = MediaFileUpload(path + file_name, mimetype=mimetype)
        fileid = '1kdcYNckY9jiyJgvG6tPzEu6PaIr0W1xJ'

        # update upload_temp.txt
        file = service.files().update(body=file_metadata, media_body=media,fileId=fileid).execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    upload_basic()

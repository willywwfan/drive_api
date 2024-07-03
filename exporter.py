from __future__ import print_function

import io

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload
from utils import load_creds
import shutil

def export_pdf(real_file_id, file_name):
    creds = load_creds()
    mimetype = "text/plain"
    # mimetype = "application/pdf"

    # create drive api client
    service = build('drive', 'v3', credentials=creds)

    file_id = real_file_id

    # pylint: disable=maybe-no-member
    request = service.files().export_media(fileId=file_id, mimeType=mimetype)
    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print(F'Download {int(status.progress() * 100)}.')

    with open("export_temp.txt", "wb") as binary_file:
        # Write bytes to file
        binary_file.write(file.getvalue())

    print("File Downloaded")
    # Return True if file Downloaded successfully
    return file.getvalue()


if __name__ == '__main__':
    export_pdf(real_file_id='1-hUcXiwsecFnKrxvd3geNPDQ_z06SeTteQlFghymkOM', file_name="export_temp.txt") # temp file

from __future__ import print_function
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from utils import load_creds


def upload_basic():
    """
    mimetype:
    https://stackoverflow.com/questions/11894772/google-drive-mime-types-listing
    """
    creds = load_creds()

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)

        path = ""
        file_name = "upload_temp.txt"
        mimetype = "text/plain"
        # path = "/home/wanweif/DriveFileStream/My Drive/"
        # file_name = "Run CTS List (Responses).gsheet"
        # mimetype = "application/vnd.google-apps.document"
        # path = "/home/wanweif/DriveFileStream/My Drive/stats_to_img/"
        # file_name = "20220608_014911_774_RAW10_4080x3072_RS_5100_PS_1_cam2_camera_interface_output_frame_11243_stats.jpg"
        # mimetype = "image/jpeg"

        file_metadata = {'name': file_name}
        media = MediaFileUpload(path + file_name, mimetype=mimetype)
        # pylint: disable=maybe-no-member
        file = service.files().create(body=file_metadata, media_body=media,fields='id').execute()
        print(F'File ID: {file.get("id")}')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

    return file.get('id')


if __name__ == '__main__':
    upload_basic()

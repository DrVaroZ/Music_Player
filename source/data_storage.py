from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class DataStorage:
    def __init__(self):
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload_file_to_drive(self, file_id, local_path):
        """Overwrites the existing Google drive file."""
        update_file = self.drive.CreateFile({'id': file_id})
        update_file.SetContentFile(local_path)
        update_file.Upload()

    def download_drive_file(self, file_id, save_path):
        """Downloads an existing Google drive file."""
        download_file = self.drive.CreateFile({'id': file_id})
        download_file.GetContentFile(save_path)

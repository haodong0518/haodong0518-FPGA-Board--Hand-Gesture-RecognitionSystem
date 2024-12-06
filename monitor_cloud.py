from azure.storage.fileshare import ShareFileClient
from azure.storage.fileshare import ShareDirectoryClient
import time
import image_process
import os

def monitor_cloud():
    while True:
        connection_str = "input your connection string here"

        directory_client = ShareDirectoryClient.from_connection_string(conn_str=connection_str, share_name="fileshare", directory_path="")

        file_list = directory_client.list_directories_and_files()
        jpeg_files = [file.name for file in file_list if file.name.endswith('.jpeg')]
        if jpeg_files:
            for jpeg_file in jpeg_files:
                file_client = ShareFileClient.from_connection_string(conn_str=connection_str, share_name="fileshare", file_path=jpeg_file)
                local_file_path = f"/home/haodong/cs395_final/pictures/{jpeg_file}"

                with open(local_file_path, "wb") as file_handle:
                    data = file_client.download_file()
                    data.readinto(file_handle)

                print(f"Downloaded {jpeg_file} to {local_file_path}")

                # Delete the file after downloading
                file_client.delete_file()
                print(f"Deleted {jpeg_file} from cloud share")

        directory = "/home/haodong/cs395_final/pictures"
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            if file_path.endswith(".jpeg"):
                print(f"file_path:{file_path}")
                image_process.show_image(file_path)
                os.remove(file_path)
                #print(f"Deleted {filename} from local directory")

        print('keep monitoring')
        time.sleep(5)

if __name__ == '__main__':
    monitor_cloud()
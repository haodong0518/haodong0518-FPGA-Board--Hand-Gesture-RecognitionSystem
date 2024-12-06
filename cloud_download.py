from azure.storage.fileshare import ShareFileClient
from azure.storage.fileshare import ShareDirectoryClient



connection_str = "input your connection string here"
cloud_file_path = "/home/haodong/clouddrive"

# List all files ending with .jpeg in the cloud share

directory_client = ShareDirectoryClient.from_connection_string(conn_str=connection_str, share_name="fileshare", directory_path="")

file_list = directory_client.list_directories_and_files()
jpeg_files = [file.name for file in file_list if file.name.endswith('.jpeg')]
# Delete each JPEG file from the cloud share after downloading it

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


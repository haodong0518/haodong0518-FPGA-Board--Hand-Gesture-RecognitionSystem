from azure.storage.fileshare import ShareFileClient
import os
# Local file path
#local_file_path = "/home/haodong/cs395_final/pictures/frame_1.jpg"


def upload_file_to_azure(local_file_path, cloud_file_path):
    # Connection string to your Azure Storage account
    connection_str = "input your connection string here"

    # Correct file path in Azure file share (e.g., "frame_1.jpg")
    file_client = ShareFileClient.from_connection_string(
        conn_str=connection_str,
        share_name="fileshare",  # Your Azure file share name
        file_path= cloud_file_path  # The path inside the share (e.g., "frame_1.jpg")
    )

    # Upload the file
    try:
        with open(local_file_path, "rb") as file:
            file_client.upload_file(file)
        print(f"File '{local_file_path}' uploaded successfully to Cloud Share.")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == '__main__':
    directory = os.getcwd()
    for filename in os.listdir(directory):
        if filename.endswith(".jpeg"):
            local_file_path = filename
            cloud_file_path = filename
            upload_file_to_azure(local_file_path, cloud_file_path)
            os.remove(local_file_path)


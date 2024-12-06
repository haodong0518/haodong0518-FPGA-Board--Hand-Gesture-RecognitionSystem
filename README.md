## DE10-Nano, FPGA-Board--Hand-Gesture-RecognitionSystem

# Author: Haodong Wang, Jiayi Xu

1. The main function is `monitor_cloud.py`, this should be run on your teriminal or shell, it will monitor the azure cloudshell, if some files are uploaded, it will catch it, run image processing algorithm, and delete the image on Azure due to te limited storage size. 

2. upload the directory files, `file on board`, to the DE10-Nano board, to allow it capturing live camera frames and uploading files. 

3. Remember to iput the connection string. 


# Challenges:

1. The DE10-Nano only provides one USB port, the USB port hub doesn't work, so I have to run `take_screenshot.pt` and `build_connection` twice. 

2. The OpenCV can not run on cloudshell, we download the images using `cloud_download.py` and run the `image_process.py` to process images locally. The `monitor_cloud.py` combines these two files. 



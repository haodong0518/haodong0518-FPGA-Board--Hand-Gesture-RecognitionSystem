import os
import final_project.file_on_board.build_connection as build_connection
import time

def keep_screenshot():
    t = 0
    while t<5:
        t+=1
        time.sleep(0.5)
        #build_connection.upload_file_to_azure('test_154.jpeg','test154.jpeg')
        os.system(f'ffmpeg -f video4linux2 -i /dev/video2 -vframes 1 test{time.time()}.jpeg')
        #build_connection.upload_file_to_azure(f'test{time.time()}.jpeg', f'test{time.time()}.jpeg')
        #os.system(f'rm test{time.time()}.jpeg')

if __name__ == '__main__':
    keep_screenshot()
    

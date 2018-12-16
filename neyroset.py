import pathlib
import os
import time
while True:
    for dirpath, dirnames, files in os.walk('/home/android/neyr/'):
        if files:
            # Working with bash
            files = os.listdir('/home/android/neyr/') # here is one file - image for alpr
            s = files[0]
            command = 'alpr -c eu /home/android/neyr/' + s + ' > /home/android/neyr/log.txt' #create record in log
            print('Photo is here')
            os.system('cd /home/android/neyr/')
            os.system(command)
            print('log is here')
            time.sleep(10)
            folder = '/home/android/neyr/'
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                    #elif os.path.isdir(file_path): shutil.rmtree(file_path)
                except Exception as e:
                    print(e)
            print('All deleted')
        if not files:
            # waiting for 10 seconds
            # time.sleep(10)
            print('files arent detected')
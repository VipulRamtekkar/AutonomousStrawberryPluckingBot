#Code for the detection of a strawberry
import cv2
import numpy as np 

 
'''def show(image):
     plt.figure(figsize=(10, 10))
     plt.imshow(image, interpolation='nearest')
 ''' 
'''def overlay_mask(mask, image):
    rgb_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    #calculates the weightes sum of two arrays. in our case image arrays
    #input, how much to weight each. 
    #optional depth value set to 0 no need
    img = cv2.addWeighted(rgb_mask, 0.5, image, 0.5, 0)
    return img
 '''
def find_biggest_contour(image):
    
    image = image.copy()
    _, contours, _ = cv2.findContours(image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    if not contours:
        return 0
    else:
        contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
        biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]

        mask = np.zeros(image.shape, np.uint8)
        cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
        return 1
     
'''def circle_contour(image, contour):
    image_with_ellipse = image.copy()
    ellipse = cv2.fitEllipse(contour)
    green = (0, 255, 0) #Colour of the bounding ellipse 
    cv2.ellipse(image_with_ellipse, ellipse, green, 2) #Drawing an ellipse around the fitted ellipse given 
    # by the function fitEllipse
    return image_with_ellipse
'''
 
def find_strawberry(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
    #max_dimension = max(image.shape)
    #scale = 700/max_dimension
    #image = cv2.resize(image, None, fx=scale, fy=scale)
    image_blur = cv2.GaussianBlur(image, (7, 7), 0)
    image_blur_hsv = cv2.cvtColor(image_blur, cv2.COLOR_RGB2HSV)
 
    min_red = np.array([0, 100, 80])
    max_red = np.array([10, 256, 256])
    mask1 = cv2.inRange(image_blur_hsv, min_red, max_red)
 
    min_red2 = np.array([170, 100, 80])
    max_red2 = np.array([180, 256, 256])
    mask2 = cv2.inRange(image_blur_hsv, min_red2, max_red2)
    mask = mask1 + mask2
 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)
    big_strawberry_contour = find_biggest_contour(mask_clean)
    #overlay = overlay_mask(mask_clean, image)
 
    #circled = circle_contour(overlay, big_strawberry_contour)
    
    #bgr = cv2.cvtColor(circled, cv2.COLOR_RGB2BGR)
    
    return big_strawberry_contour


if __name__ == '__main__':
          
    image = cv2.imread('images.jpeg')
    result = find_strawberry(image)
    if result == 0:
        print ("No strawberry")
    else:
        print ("Found Strawberry")


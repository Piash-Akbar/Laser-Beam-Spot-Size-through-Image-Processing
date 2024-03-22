from sklearn import preprocessing
import numpy as np
import pandas as pd
import cv2

###Noise reduction(Auto)
def noiseReductionAuto(image_path):
    image = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    image_red = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    image_red[:,:,0] = 0
    image_red[:,:,1] =0
    #image = image[200:600,400:700]
    #CONVERT IMAGE TO GRAYSCALE 
    image_gray = cv2.cvtColor(image_red, cv2.COLOR_BGR2GRAY)
    # onvert image to blck and white
    th1, image_edges = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY) #th=>threshold
    #########
    blur = cv2.GaussianBlur(image_gray,(5,5),0)
    ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    


    ########
    th2 = cv2.Canny(image_gray,100,255)
    # create background mask
    mask = np.zeros(image_red.shape, np.uint8)##
    # get most significant contours
    contours_draw, hierachy = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x = cv2.drawContours(mask, contours_draw, -1, (255, 255, 255), -1)
    new_image = cv2.bitwise_and(image, mask)##
    cv2.imshow('sdewfer',x)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return new_image

####Noise reduction (Manual)

def noiseReductionManual(image_path):
    # Load the images
    image1 = cv2.imread(image_path)
    # Select the ROI using the cv2.selectROI function
    roi = cv2.selectROI(image1)

    #Extract the ROI region
    x1, y1, w, h = [int(val) for val in roi]
    image2 = image1[y1:y1+h, x1:x1+w]

    # Get the pixel values of both images
    pixels1 = set(map(tuple, image1.reshape(-1, 3)))
    pixels2 = set(map(tuple, image2.reshape(-1, 3)))

    # Find common pixel values
    common_pixels = pixels1.intersection(pixels2)

    # Create a new image with replaced pixels
    new_image = np.copy(image1)

    # Replace common pixel values with black (0, 0, 0)
    height, width, _ = new_image.shape
    for x in range(width):
        for y in range(height):
            if tuple(image1[y, x]) in common_pixels:
                new_image[y, x] = [0, 0, 0]
    return new_image



###Taking data along column(x-axis)
def data_x(image):
    value=[]
    cl = np.sum(image,axis=0)
    value.append(cl) #2d array
    value = value[0]
    #normed_value = preprocessing.normalize([value])###to work###
    return value#,normed_value 
###Taking Data along row(ya-xis)
def data_y(image):
    value=[]
    cl = np.sum(image,axis=1)
    value.append(cl) #2d array
    value = value[0]
    #normed_value = preprocessing.normalize([value])###To work###
    return value#,normed_value 



###Setting the name for CSV file
def data_name(input_folder,individual_img):
    length = len(input_folder)
    name = individual_img[length:-4] #character number of directory till '.png'
    name = name.replace(' ','_')
    return name

###Saving the data
def data_saving(value,normed_value,name,cols_row):
    df = pd.DataFrame({'Values': value,'N_values':normed_value[0]})
    df.to_csv('./data/{}_{}.csv'.format(name,cols_row),index_label='steps')
    return 0


###This segment is cut from visualizer
###Fixing the Spike





def standardIntensity(y):

    ###
    intensity = np.diff(y)
    m=4
    ###
    mean_int = np.mean(intensity)
    std_int = np.std(intensity)
    z_scores = (intensity - mean_int) / std_int
    ####
    threshold = 4 # binarization threshold.
    spikes = abs(np.array(z_scores)) > threshold
    y_out = y.copy() # So we don’t overwrite y 
    for i in np.arange(len(spikes)):
        if spikes[i] != 0: # If we have an spike in position i
            w = np.arange(i-m,i+1+m) # we select 2 m + 1 points around our spike
            w2 = w[spikes[w] == 0] # From such interval, we choose the ones which are not spikes
            y_out[i] = np.mean(y[w2]) # and we average their values
    return y_out
###to work with this one line###
# fixer = fixer(values,m=4)



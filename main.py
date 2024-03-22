###This Code Is For Creating DataSet of Laser Beam Image###

###Libraries Used
import cv2
#import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing

###
from lmfit import Model

###
from helper import noiseReductionAuto,noiseReductionManual,data_x,data_y,data_name,data_saving,standardIntensity


###Getting Datas
inputFolder = ('/media/pias/git/Rearrange/')
#os.mkdir('Resized')
#os.mkdir('CSVs')

for image in glob.glob(inputFolder + '/*.png'):

    ###Taking Data Name
    name = data_name(inputFolder,image)
    
    #Taking Image with No Background noise
    img = noiseReductionManual(image)
    
    ###convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ##get data along column
    cols = data_x(gray)
    ###get Standardized data with help of z-score(for columns)
    standard_cols = standardIntensity(cols)
    # print(standard_cols)
    ###Normalized columns
    normed_cols = preprocessing.normalize([standard_cols])


    ##get data along row
    row = data_y(gray)
    ###Get Standardized data with hwlp of z-score (for rows)
    standard_rows = standardIntensity(row)
    ###Normalizd row data
    normed_row = preprocessing.normalize([standard_rows])
    
    ############################################Fitting should be here###############################

    # def gaussian(x, amp, cen, wid):
    #     """1-d gaussian: gaussian(x, amp, cen, wid)"""
    #     l=(amp / (np.sqrt(2*np.pi) * wid)) * np.exp(-(x-cen)**2 / (2*wid**2))
    #     #l = amp*np.exp(-(x-cen)**2/(2*wid**2))
    #     return l


    # gmodel = Model(gaussian)
    # result = gmodel.fit(normed_cols,x=np.ndarray(len(normed_cols)),amp = 50,cen=150,wid=50)



    # amp = result.params['amp'].value
    # cen = result.params['cen'].value
    # wid = result.params['wid'].value
    # std = wid
    # ft = result.best_fit
    # print(result.fit_report())
    # plt.plot(np.ndarray(len(result.best_fit)),result.best_fit)
    # # plt.legend()
    # plt.show()
    
    #################################################################################################
    ####################Sample saving#######################
    def data_saving_sample(value,std_value,normed_value,name,colrow):
        df = pd.DataFrame({'values': value,'std_values':std_value,'n_values':normed_value[0]})
        df.to_csv('./data/{}_{}.csv'.format(name,colrow),index_label='steps')
        return 0
    column = data_saving_sample(cols,standard_cols,normed_cols,name,'columns')

    #######################################################
    st = np.ndarray(len(normed_cols))
    plt.plot(st,normed_cols)
    plt.show()


    ###Showing the Image(Not Important)

    cv2.imshow('img',img)
    k=cv2.waitKey(0)
    if k==27:
        break
    
cv2.destroyAllWindows()


###
print('The data has produces.ThankYou!')
# ==================================================================
## {Description} -Mean Shift Intro - Practical Machine Learning Tutorial with Python p.39
# ==================================================================
## {License_info}
# ==================================================================
## Author: {G}
## Copyright: Copyright {year}, {project_name}
## Credits: [{credit_list}]
## License: {license}
## Version: {mayor}.{minor}.{rel}
## Maintainer: {maintainer}
## Email: {contact_email}   
## Status: {dev_status}
# ==================================================================
# Import Libraries
import numpy as np
from sklearn.cluster import MeanShift, KMeans
from sklearn import preprocessing,  model_selection  # before it was cross_validation
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm

import xlrd # This one not needed but it is used within the sklearn and pandas.
# -----------------------------------------------------
# Installing packages -
# -----------------------------------------------------
import datetime as dt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


style.use('ggplot')

# Prepare a directory file for our current file
import os
import os.path as path
ResourceDir = os.getcwd()

# ---------------------------------------------------
# Create a directory to export data to it.
# if not os.path.exists(ResourceDir+"/resources/stock_dfs/"):
#         os.makedirs(ResourceDir+"/resources/stock_dfs/")
# ---------------------------------------------------


# import os

# os.chdir('/path/to/files/')

# # Am I in the correct directory?
# # print(os.getcwd())

# # print(dir(os))

# # Print all the current file names
# for f in os.listdir():
#     # If .DS_Store file is created, ignore it
#     if f == '.DS_Store':
#         continue

#     file_name, file_ext = os.path.splitext(f)
#     # print(file_name)

#     # One way to do this
#     f_title, f_course, f_number = file_name.split('-')

#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

#     # Need to remove whitespace
#     f_title = f_title.strip()
#     f_course = f_course.strip()
#     # f_number = f_number.strip()

#     # Want to remove the number sign?
#     # f_number = f_number.strip()[1:]

#     # One thing I noticed about this output is that if it was sorted by filename
#     # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
#     # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
#     # We can do this in Python with zfill
#     f_number = f_number.strip()[1:].zfill(2)

#     # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

#     # You have the power to reformat in any way you see fit
#     print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

#     new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

#     os.rename(fn, new_name)


# # print(len(os.listdir()))


# print('sklearn: %s' % sklearn.__version__)

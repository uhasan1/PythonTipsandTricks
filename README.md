# Python Tips and Tricks
# - Quick References and Formula to increase productivity

Code Snippets imported from **Corey Schafer** one of the greatest references of Python available online. Other files such as the ones in
```
~/projectfiles/
```
are some code snippets that I have collected through my work on several projects.

# Files Managements [Reading and Writing]
How to read and write to a specific directory and how to open a directory read files ..etc.
the purpose is to get quick reference and formula to various tasks using Python.

### Getting current file directory

```
ResourceDir = os.getcwd()
```

### Making Directory
```
Create a directory to export data to it.
if not os.path.exists(ResourceDir+"/resources/stock_dfs/"):
os.makedirs(ResourceDir+"/resources/stock_dfs/")
```
### Change Directory

```
os.chdir('/path/to/files/')
```
### Reading or Writing Files

For Writing a file (in Pickle Format)
```
with open(ResourceDir+"/resources/sp500tickers.pickle","wb") as f:
        pickle.dump(tickers,f)
```
For Reading a file (in Pickle Format)

```
with open(ResourceDir+"/resources/sp500tickers.pickle","rb") as f:
            tickers = pickle.load(f)
```
* [Note] The **wb** means **write binary** and **rb** means **read binary**.

# Automate Parsing and Renaming of Multiple Files


```

import os

os.chdir('/path/to/files/')

# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))

# Print all the current file names
for f in os.listdir():
    # If .DS_Store file is created, ignore it
    if f == '.DS_Store':
        continue

    file_name, file_ext = os.path.splitext(f)
    # print(file_name)

    # One way to do this
    f_title, f_course, f_number = file_name.split('-')

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # Need to remove whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    # f_number = f_number.strip()

    # Want to remove the number sign?
    # f_number = f_number.strip()[1:]

    # One thing I noticed about this output is that if it was sorted by filename
    # then the 1 and 10 would be next to each other. How do we fix this? One way we can fix this is to pad
    # the numbers. So instead of 1, we'll make it 01. If we had hundreds of files then this would maybe need to be 001.
    # We can do this in Python with zfill
    f_number = f_number.strip()[1:].zfill(2)

    # print('{}-{}-{}{}'.format(f_number, f_course, f_title, file_ext))

    # You have the power to reformat in any way you see fit
    print('{}-{}{}'.format(f_number, f_title.strip(), file_ext.strip()))

    new_name = '{}-{}{}'.format(file_num, file_title, file_ext)

    os.rename(fn, new_name)
```
# List Dictionary and Tuples tricks
to get the reverse elements of a function you can run

```
list[::-1]
```

# Problem with some packages

## Getting Package Version
There is a quick way to know the package version using:
```
print('sklearn: %s' % sklearn.__version__)
```

## Matplotlib
In Mac you will need to declare the following items to make the package **matplotlib** works

```
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import style
```
## Sklearn
The following is important when you import, **model_selection** is now replaced **cross_validation**

```
from sklearn import preprocessing,  model_selection
```
# Regular Expression
More details on Regular Expression are found within the current repository

```
code_snippets/Python-Regular-Expressions/
```
## Python Version
Required Modules to start:
```
Numpy
Matplotlib
Pandas
Pandas-datareader
BeautifulSoup4
scikit-learn / sklearn
```
# My Current Progress [Update]

# Inspiration
* On AUtomate Parsing and Renaming of Multiple Files: https://www.youtube.com/watch?v=ve2pmm5JqmI
*



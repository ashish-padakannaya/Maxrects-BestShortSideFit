Implementation of a solution to the [bin packing](https://en.wikipedia.org/wiki/Bin_packing_problem) algorithm with Python and Bokeh. 

Install required packages 

    pip install -r requirements.txt

zdf1.txt contains the data set for packing. The format should be 

    number n of items
    width W for the strip 
    height H for the strip
    for each item (i=0,1,......n-1):
        index i, width of item i, height of item i

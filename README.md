Implementation of a solution to the [2D bin packing](https://en.wikipedia.org/wiki/Bin_packing_problem) algorithm with Python and Bokeh. 

Install required packages 

    pip install -r requirements.txt

zdf1.txt contains the data set for packing. The format should be 

    number n of items
    width W for the strip 
    height H for the strip
    for each item (i=0,1,......n-1):
        index i, width of item i, height of item i
        
 Currently the dataset has {N: 580, W: 100,H: 800}
 
To pack and display a plot, run the file new-rect.py
    
    python new-rect.py

The plot ouput also gets stored in a file maxrects.html


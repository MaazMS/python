### Correlation    

what is Correlation.?   
   
1.  The statistical relationship between two variables is referred to as their correlation.
2. Correlation used to identify the association between variables.   
3 Correlation of two variables (pairwise) has values between -1 **negative correlation** and 1 **positive correlation**.     
4. positive, meaning both variables move in the same direction,  
5. negative, meaning that when one variable's value increases, the other variables' values decrease. 
6. Correlation can also be neutral or zero, meaning that the variables are unrelated.    

`Positive Correlation`: both variables change in the same direction.    
`Neutral Correlation`: No relationship in the change of the variables.   
`Negative Correlation`: variables change in opposite directions.   
5. Statistical tests to measure correlation: Pearson, Spearman rank, Kendall Tau.       


   
`observation` : Each data point in the dataset is called observation.     
Example : When data is represented in the form of a table, the rows of that table are usually the observations.             
` features` : The properties or attribute of those observation.    
Example : Table of columns are the features.        

![](https://files.realpython.com/media/py-corr-1.d13ed60a9b91.png)
`Negative correlation (red dots)`: In the plot on the left, the y values tend to decrease as the x values increase. This    
shows strong negative correlation, which occurs when large values of one feature correspond to small values of the other    
,and vice versa.   
   
   
`Weak or no correlation (green dots)`: The plot in the middle shows no obvious trend. This is a form of weak correlation,    
which occurs when an association between two features is not obvious or is hardly observable.        


`Positive correlation (blue dots)`: In the plot on the right, the y values tend to increase as the x values increase. This     
illustrates strong positive correlation, which occurs when large values of one feature correspond to large values of the          
other, and vice versa.    
  
**Note**    
1. That the correlation of a variable with itself is 1. For that reason all the diagonal values are 1.    


Methods for correlation   
1. `Pearson’s` coefficient measures linear correlation.    
2. `Spearman` and `Kendall` coefficients compare the ranks of data.   

example of correlation between rice cost and quantity in kg.     
![](https://github.com/MaazMS/python/blob/master/correlation/basic_correlation_concept_doc/images_of_correlation_concept/Screenshot%20from%202020-08-27%2016-45-03.png?raw=true)     
      
In this graph the cost is increase and the quantity is decrease. This is called negative correlation       

example of correaltion between onion and quantity in kg.      
![](https://github.com/MaazMS/python/blob/master/correlation/basic_correlation_concept_doc/images_of_correlation_concept/Screenshot%20from%202020-08-27%2017-09-24.png?raw=true)    
          
This graph is not incease and not decrease there for no correlation between onion cost and quantity in kg.       
   
example of correlation between watch and quantity.      
![](https://github.com/MaazMS/python/blob/master/correlation/basic_correlation_concept_doc/images_of_correlation_concept/Screenshot%20from%202020-08-27%2017-10-12.png?raw=true)    
     
In this graph cost in increase and quantity is aslo increase .There for it is positive correlation.      

why wee need correlation formula.      
![](https://github.com/MaazMS/python/blob/master/correlation/basic_correlation_concept_doc/images_of_correlation_concept/why_we_need_formula_of_correlation.png?raw=true)    
    
In this graph some statics say it is positive correlation and some say it is negative correlation.    
That's why wee need some mathematical formula to solve this problem.   
   
formula of correlation coefficient 
**first formula**   
![](https://cdn1.byjus.com/wp-content/uploads/2019/06/word-image28.png)      
      
**second formula**   
![](https://cdn1.byjus.com/wp-content/uploads/2019/02/Correlation-Coefficient-Formula.png)     
     

      



what is `NaN` ?.   
In pandas, a missing value is denoted by NaN.   

what is pandas? 
pandas is software library written for the Python programming language for data manipulation and analysis.        

what is data science?   
data science or data analysis is a process of analyzing large set of data points to get answers on questions related to that   
data set.         

Not : corr() is used to find the pairwise correlation of all columns in the dataframe. For any non-numeric data type columns in the dataframe it is ignored.   

what is subplots? 
 Create a figure and a set of subplots


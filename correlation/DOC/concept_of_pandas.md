### method use in pandas    
`dataframe.corr()`  : It is used to find pairwise correlation of all column in the dataframe and any non-numeric columns   
are ignored.   

## datatype     

1. why we need datatype?   
A data type is essentially an internal constructor that programming language use to  understand how to store and        
manipulate data.   

**Pandas dtype mapping**      


|Pandas dtype     | Python type	| NumPy type	                | Usage 
| --- | --- | --- | ---|   
|object          | str or mixed      |string_, unicode_, mixed types	          |Text or mixed numeric and non-numeric values
|int64           |int	            |int_, int8, int16, int32, int64, uint8, uint16, uint32, uint64	| Integer numbers
|float64         |float	            |float_, float16, float32, float64	                         |Floating point numbers 
|bool            |bool	            |bool_	                                                      |True/False values
|datetime64     |	NA	            |datetime64[ns]	                                                |Date and time values
|timedelta[ns]  | NA                |NA                                                             |Differences between two datetimes  
|category       |  NA               |NA                                                             |Finite list of text values  

**Note**  dtype: object. An object is a string in pandas so it performs a string operation instead of a mathematical one.   
  
 In order to convert data types in pandas, there are three basic options:   
* Use astype() to force an appropriate dtype
* Create a custom function to convert the data
* Use pandas functions such as to_numeric() or to_datetime()    

#### Using the astype() function   
The simplest way to convert a pandas column of data to a different type is to use astype() . For instance, to convert the   
Customer Number column to an integer we can call it like this:      
df['Customer Number'].astype('int')  
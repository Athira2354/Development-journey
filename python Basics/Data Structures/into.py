"""
collection is used to store set of objects.


OLLECTION NAME      DEFINE|CREATE                 MUTABLE               OREDERD      DUPLICATE ALLOWED      METHOD        
 
  STRING                NAME=''                     IMMUTABLE              ORDERD          YES              capitalize()
                        NAME=""                                                                             casefold()
                        NAME=""" """     
                        
  LIST                 VARIABLE_NAME=[]              MUTABLE               ORDERD          YES               append()
                       LST=LIST()                    v_name[index]=""

  TUPLE                VARIABLE_NAME=(  ,)           IMMUTABLE             ORDERD          YES                           

  SET                  VARIABLE_NAME={VALUE}
                       VARIBLE_NAME=SET() EMPTY SET  IMMUTABLE               UNORDERD        NO
                                                    (CAN CHNAGE BY METHOD) 
  DICTIONARY           VARIABLE_NAME={"KEY":VALUE}
"""



"""
Summary of Key Differences
Feature 	     |     List	        |      Tuple	        |     Set	        |      Dictionary
Syntax	       |      []	        |       ()	          |   {} (or set())	|       {key: value}
Ordered	       |      Yes	        |       Yes	          |     No	        |       Yes (Python 3.7+)
Mutable	       |      Yes	        |       No (Immutable)|	    Yes	        |       Yes
Duplicates	   |      Allowed	    |       Allowed	      |   Not Allowed	  |       Keys must be unique
Access Method	 |      Index-based	|       Index-based	  |   No indexing	  |       Key-based



"""
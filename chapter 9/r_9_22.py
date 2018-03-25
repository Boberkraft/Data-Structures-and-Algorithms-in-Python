"""
Show all the steps of the algorithm for replacing key of entry (5,A) with
18 in the heap of Figure 9.1, assuming the entry had been identified with
a locator.

                   4C                       
           5A              7Z               
      15K      9F      7Q     20B          
    16X 25J 14E 12H 11S 13W
       
    UPDATE(5A, 18, A)
                   4C                       
          18A              7Z               
      15K      9F      7Q     20B          
    16X 25J 14E 12H 11S 13W
    
    BUBBLE(18A)
                   4C                       
           9F             7Z               
      15K     18A      7Q     20B          
    16X 25J 14E 12H 11S 13W    
    
    DOWNHEP
                   4C                       
           9F              7Z               
      15K     12H      7Q     20B          
    16X 25J 14E 18A 11S 13W
"""

"""
Show all the steps of the algorithm for removing the entry (16,X) from the
heap of Figure 9.1, assuming the entry had been identified with a locator.

    
                   4C                       
           5A              7Z               
      15K      9F      7Q     20B          
    16X 25J 14E 12H 11S 13W   
           
           
    SWAP WITH LAST POSITION
                   4C                       
           5A              7Z               
      15K      9F      7Q     20B          
    13W 25J 14E 12H 11S 16X                
       
       
    POP LAST POSITION      
                   4C                       
           5A              7Z               
      15K      9F      7Q     20B          
    13W 25J 14E 12H 11S        
    
    DECIDE IF IT NEEDS TO UPHEAPED OR DOWNHEAPED.
        IS 13 < 15?
            IF YES:
                UPHEAP()
            IF NO:
                DOWNHEAP()
    
    ...
    WE NEED TO UPHEAP()
                   4C                       
           5A              7Z               
      13W      9F      7Q     20B          
    15K 25J 14E 12H 11S        
    
    
    
    
    
"""

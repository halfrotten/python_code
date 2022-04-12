#takes the users input for the mile sna dminutes spent driving each day adding them together and displaying them

def the_while():
    summ_num=0
    count=0
    summ_mile=0
    mpg=[]
    days_week=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']# go thru day of the week
    
    while count<len(days_week): #while we are at less than 7 days of data collected

        num=input('how much minutes did you drive on '+days_week[count]+" ? ")
        mile=input('how much miles did you drive on '+days_week[count]+" ? ")#add things
        summ_num+=int(num)
        summ_mile+=int(mile)
        
        count+=1#counter for while loop
        
    return "\nyou drove " + str(summ_num) +" minutes this week and "+str(summ_mile)+" miles"















if __name__ == "__main__":

    print(the_while())#print result
    

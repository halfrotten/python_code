#constants
#--------------------
#standard cleaning -$300
#full cleaning -$600
#fee for <= 2 rooms -$100 per room
#fee for <=5 rooms -$90 per room
#fee for > 5 rooms -$80 per room
#mowing cost -$5
#edge cost -$10
#shrub cost -$10
#senior discount-15%


#info on cleaning service and costs
cleaning_service_info=("price for standard cleaning starting at 300 and full house starts at 600, standard includes cleaning of floors and stairways, full includes every inch of the house cleaned, additional fee for two or less rooms($100 ea), additional fee for 5 or less rooms($90 ea), additional fee for more than 5 rooms($80 ea)")


#determine discount
def Discount(cost):
    discount_percentage=15 # discount rate for seniors
    print('seniors have a',discount_percentage,'percent off the total price')
    while True:
        senior=input('are you a senior? Y/N ')
        if senior=='Y':
            final_cost=(1-(discount_percentage/100))*float(cost)
            break
        elif senior=='N':
            final_cost=cost
            break
        else:
            pass
    print( "final cost is: $",final_cost)


#determine yard cost
def  Yard():
    print('mowing-$5 per square feet'+'\nedging-10$ per footage of edge'+'\nshrubs-10$ per shrub')
    while True:
        try:
            mow=int(input('how much square feet of lawn for mowing? '))
            break
        except:
            pass
    while True:
        try:
            edge=int(input('how much feet of lawn edge? '))
            break
        except:
            pass
    while True:
        try:
            shrub=int(input('how many shrubs? '))
            break
        except:
            pass
    mow=5*mow#math
    edge=10*edge#math
    shrub=10*shrub #math
    cost=mow+edge+shrub #adding all costs
    
    Discount(cost)
#determine house cleaning cost
def HouseCleaning(cleaning_service_info=cleaning_service_info):
    
    for i in cleaning_service_info.split(","):#print list
        print(i)
    
    while True:   #get number of rooms and check for correct input
        try:
           number_of_rooms=int(input("number of rooms in the house? "))
           
           break
        except:
            print("incorrect input need a whole number \n")
    
    
        
    while True:#get  type of cleaning and check for correct input
        type_of_cleaning=input("type of cleaning? (standard==1 or full==2)?") #input standard or full what type of cleaning service?
        if type_of_cleaning=="1" or type_of_cleaning=="2":
            break
        else:
            print('incorrect input')
            
    room=int(number_of_rooms)

    if type_of_cleaning=="1":#if standard cleaning plan chosen
            if room <=2:#if less or equal to 2 rooms
                a=300+(100*room)
            elif room <=5:#if less or equal to 5 rooms
                a=300+(90*room)
            elif room >5:#if greater than 5 rooms
                a=300+(80*room)
                
            Discount(a)#call function for discount
           
    elif type_of_cleaning=="2":#if full cleaning plan chosen
            if room <=2:
                a=600+(100*room)#if less or equal to 2 rooms
            elif room <=5:
                a=600+(90*room)#if less or equal to 5 rooms
            elif room > 5:
                a=600+(80*room)#if greater than 5 rooms
                
            Discount(a)#call function for discount
            
    else:
        print("incorrect input\n")

           

    

    
    
        

if __name__=='__main__':
    while True:
        figure=input('are you getting yard work or house cleaning?(yard or house)')
        if figure=='yard':
            break
        
        elif figure=='house':
            break
        else:
            pass
    if figure=='yard':
        Yard()
    else:
        HouseCleaning()

            
                       

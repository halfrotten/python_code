
#info on cleaning service and costs
cleaning_service_info=("price for standard cleaning starting at 300 and full house starts at 600, standard includes cleaning of floors and stairways, full includes every inch of the house cleaned, additional fee for two or less rooms($100 ea), additional fee for 5 or less rooms($90 ea), additional fee for more than 5 rooms($80 ea)")
 # documentation would be in a file so it would better to use a file then iterate a local string. pointing to a external file would allow updates to the program without messign with code
def CostOfCleaning(cost,room):
    room=int(room)
    if cost=="1" and room <=2:
        a=300+(100*room)
    elif cost=="1" and room <=5: #making statements to check what was inputted and to make correct calculations
        a=300+(90*room)
    elif cost=="1" and room >5:
        a=300+(80*room)

    elif cost=="2" and room <=2:
        a=600+(100*room)
    elif cost=="2" and room <=5:
        a=600+(90*room)
    elif cost=="2" and room > 5:
        a=600+(80*room)
    else:
        raise TypeError

    return "\n$"+str(a)+ " is the cost of the cleaning: "+str(room)+" room(s)\nand the type of cleaning requested is number "+str(cost) #returning final cost
    
        




for i in cleaning_service_info.split(","):#print list
    print(i)
    
while True:   #get number of rooms
    try:
       number_of_rooms=int(input("number of rooms in the house? "))
       break
    except:
        print("incorrect input need a whole number \n")
        
while True:
    type_of_cleaning=input("type of cleaning? (standard:1 or full house:2)?") #input standard or full what type of cleaning service?
    if type_of_cleaning.find("full")==0 or type_of_cleaning=="2":
            print(CostOfCleaning("2",number_of_rooms))#call function
            break
    elif type_of_cleaning.find("stand")==0 or type_of_cleaning=="1":
            print(CostOfCleaning("1",number_of_rooms))#call function
            break
    else:
            print("incorrect input\n")



            
                       

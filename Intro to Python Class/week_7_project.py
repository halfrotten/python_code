#paul otradovec
#week 7 project
number_people=int(input('how much people are participating in this trip? '))
number_days=int(input('how much days is this trip? '))
food_trip_cost=[]
gas_trip_cost=[]
count=0 #setting count for while loop to match days the trips exists
while count<number_days:
    food_cost=int(input('food cost on day {}? '.format(count+1)))#user input for gas and food cost per day
    gas_cost=int(input('gas cost on day {}? '.format(count+1)))
    food_trip_cost.append(food_cost)#add food cost each day to array
    gas_trip_cost.append(gas_cost)#add gas cost each day to array
    count+=1
total_cost_gas=0
total_cost_food=0
for day in range(len(food_trip_cost)):
    
    total_cost_gas=total_cost_gas+gas_trip_cost[day]#add gas cost together from each day
    total_cost_food=total_cost_food+food_trip_cost[day]#add food cost together from each day

print('\n>>>>>>>>>>>>>>\nThe total cost of food is ',total_cost_food,'\n>>>>>>>>>>>>>>')#print total food
#print total gas
print('The total cost of gas is ',total_cost_gas,'\n>>>>>>>>>>>>>>')
#print total cost of trip
print('The total cost of the trip is',total_cost_gas+total_cost_food,'\n>>>>>>>>>>>>>>')
print('Each person will be paying',100/number_people,'% of the trips cost which is $',(total_cost_gas+total_cost_food)/number_people,'each')
#put in the pecentage of the trip each user is to pay and the amount they are to pay to be even all around


#if we spent 100 in europe it would be 90 in the US: conversion euro .9 to 1 USD:

#cost_in_europe*.9=cost_in_us

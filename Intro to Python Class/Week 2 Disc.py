# Prompts user for how many Hrs a day is spent on gaming
# Prompts user for the amont of days a week he plays


Hrs_day= eval(input('How may hours a day do you spend gaming ?'))
Days_played = eval(input(' how many days a week do you play ?'))
days_Year = 365
Hrs_in_day = 24

Average_play_year = (Hrs_day * Days_played * days_Year // Hrs_in_day)

print( ' You play ' ,Average_play_year,' hrs per year')

#new code
#asks userhow many years they consider playing videogames
resolution=eval(input("how many years do you plan to spend on playing video games(yrs)? "))
answer=resolution*Average_play_year
print( ' Averaged: You would be using' ,answer,'hrs total thats', (answer/24),"days or ",((answer/24)/365),"years of your life")


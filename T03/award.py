#Create inputs to store variables for each event of the triathlon
swimming_time = int(input("How many minutes did it take you to complete the swimming event "))
cycling_time = int(input("How many minutes did it take you to complete the cycling event "))
running_time = int(input("How many minutes did it take you to complete the running event "))

#create a variable to store the sum of each event in the triathlon
total_time =  (swimming_time + cycling_time + running_time)

#create a conditional to award to participant Provincial colours if their total time is <= 100 minutes
if total_time <= 100:
    print(f"Your total time was {total_time} minutes. Congratulations, you have been awarded Provincial colours! ")

#create a conditional to award to participant Provincial half colours if their total time is 101<=>105 minutes
elif total_time <=105:
    print(f"Your total time was {total_time} minutes. Congratulations, you have been awarded Provincial half colours! ")

#create a conditional to award to participant Provincial Scroll if their total time is 106>=<110 minutes
elif total_time <= 110:
    print(f"Your total time was {total_time} minutes. Congratulations, you have been awarded Provincial Scroll")

#create a conditional to award to No Award if their total time is >=111 minutes
else:
    print(f"Your total time was {total_time} minutes. Unfortunately you have received No Award.")
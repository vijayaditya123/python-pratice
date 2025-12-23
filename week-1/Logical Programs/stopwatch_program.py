start_time= float(input("Enter the start: "))
end_time = float(input("Enter the end: "))
if end_time<start_time:
    end_time +=12-start_time
    
res= end_time-start_time
print(res)

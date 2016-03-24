from django.shortcuts import render, render_to_response
from django.http import HttpResponse

import calendar

def print_calendar(request, year, month):
    
    year = int(year)
    month = int(month)
    
    monrange = calendar.monthrange(year, month)
    
    first_day = monrange[0]
    last_date = monrange[1]
    
    print(first_day, last_date)
    
    cal = [ [ ] ]
    week = 0
    day = 1
    count = -1
        
    while count <= 40 : 
        if count < first_day + last_date and count >= first_day : 
            cal[week].append(day)
            day += 1
            count += 1
        else : 
            cal[week].append(-1)
            count += 1
        
        if count % 7 == 6 : 
            cal.append([ ])
            week += 1
    
    tmp = 0
    
    for i in range(0, 7) : 
        tmp += cal[0][i]
        
    if tmp == -7 : 
        del cal[0]
        
    print(cal)
    
    return render_to_response('calendar.html', {"Y" : year, "M" : month, "cal" : cal})

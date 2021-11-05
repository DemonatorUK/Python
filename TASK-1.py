time = int(input())
if time >= 29030400:
    y = time // 29030400
    time = time % 29030400
    print(y, "Years")
if time >= 2419200:
    mn = time // 2419200
    time = time % 2419200
    print(mn, "Month")
if time >= 604800:
    w = time // 604800
    time = time % 604800
    print (w, "Weeks")
if time >= 86400:
    d = time // 86400
    time = time % 86400
    print(d, "Days")
if time >= 3600:
    h = time // 3600
    time = time % 3600
    print(h, "Hours")
if time >= 60:
    m = time // 60
    time = time % 60
    print(m, "Minutes")
    print(time, "Seconds")
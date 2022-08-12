iterateCount = int(input());
for i in range(iterateCount):
    try:
        a,b=[int(index) for index in input().split()]
        print (int(a)//int(b))
    except ZeroDivisionError as e:
        print ("Error Code:",e)
    except ValueError as e:
        print ("Error Code:",e)

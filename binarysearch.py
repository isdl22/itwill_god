def binary():

    x = int(input("찾는 숫자를 입력하세요 ~"))
    
    data = [1,7,11,12,14,23,33,47,51,64,67,77,130,672,871]
    
    head = data.index(1)
    
    tail = len(data)
    
    mid = int((head + tail)/2)
    
    if x == data[mid]:
        
        print(data.index(x),"번째 위치에",x,"(이)가 있습니다.")
    
    while(data[mid]!=x): 
    
        mid = int((head + tail)/2)
    
        if data[mid] == x:
    
            print(data.index(x),"번째 위치에",x,"(이)가 있습니다.")
    
        elif data[mid] != x:
    
            if data[mid] > x:
    
                tail = data.index(data[mid])-1
    
            elif data[mid] < x:
    
                head = data.index(data[mid])+1
    
        if head > tail:
    
            print(x,"는 없습니다.")
    
            break
binary()

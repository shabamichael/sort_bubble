
def main():
    arr = [64,34,25,12,22,11,90]
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1] = temp

    print(arr)
    print(*(arr))
    for i in range(0, len(arr)):
      print(arr[i] , end=" ")

if __name__ =="__main__":
    main()
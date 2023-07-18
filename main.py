class solution:
    def mod_array(self,arr,p):
        ans=0
        power=1
        i=len(arr)-1
        while(i>=0):
            ans=ans+((arr[i]%p)*power)%p
            power=(power*10)%p
            i-=1
        return ans%p
a1=solution()
arr=list(map(int,input().split()))
b=int(input())
print(a1.mod_array(arr,b))
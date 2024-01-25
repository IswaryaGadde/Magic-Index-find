
def magicIndexDistinctValues( arr, s, e):
    if s < e:
        m = (s+e)//2

        if arr[m] == m:
            return m
        elif arr[m] > m:
            #go left
            magicIndexDistinctValues(arr,s,m)
        else:
            #go right
            magicIndexDistinctValues(arr,m+1,e)

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        inp = f.read()
        print(type(inp))
        n= len(inp)
        inp=list(map(int,inp.strip().split()))[:n]
        magicIndexDistinctValues(inp, 0,len(inp-1))
 
    print(inp)
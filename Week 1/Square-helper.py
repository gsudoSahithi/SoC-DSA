n,m,a= map(int, input().split())
tile_n,tile_m=0,0
if n%a!=0:
    tile_n=n//a+1
else:
    tile_n=n//a    
if m%a!=0:
    tile_m=m//a+1
else:
    tile_m=m//a    
print(tile_m*tile_n)    
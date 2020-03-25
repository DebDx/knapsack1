#Name: Deborshi Deb
#Reg No: 201800086
'''Greedy Knapsack 
{
   for i=1 to n                                  //step1     
   {
      compute pi/wi;                             //step2  
    
  // form 1 to n we have compute above code      ---- O(n) (tim taken , since it runs n times)
    }   
    
    sort objects in non- increasing order p/w;     //step3
    
 // if i have n objects and i have to sort them, then 
 best sorting algorithm (compasion base sorting algo) is merge sort.    --  O(nlogn) (time take for merge sort) 
   
     for i=1 to n                                    //step4     
    {
    if(m>0 && wi<=m)                             //step5
          m = m - wi;                               //step6
          P = P + pi;                               //step7
      else                                          //step8
        break;                                      //step9
   }
   // for above code we have iterate from 1 to on sorted list           --  O(n) (time taken)
   
  if(m>0)                                           //step10 
  {
     P=P+ pi*(m/wi);                                //step11
   // this step will take constantant time so                           --  O(1) (time taken)
   }
   
   
   SO we total time taken will be = O(n) + O(nlogn) + O(n) +O(1)
   so time complexity will be  = O(nlogn)
   

}'''
t=[]                #t for objects, w for weights, p for profits
w=[]
p=[]
k=int(input("Enter the number of items")) #k for number of items
o=0
for i in range(k):
    o=o+1
    t.append(o)
print(t)
y=int(input("Enter the maximum weight of sack")) #y for maximum weight of sack
for i in range(k):
    w.append(int(input("Enter the weight")))
for i in range(k):  
    p.append(int(input("Enter the profits")))
r=[]                 #r for profit by weight ratio
for i in range(k):
    r.append(p[i]/w[i])
print(r)
for i in range(k-1):           #sort in decreasing order all according to the ratio
    for j in range(k-i-1):
        if(r[j]<r[j+1]):
            t[j],t[j+1]=t[j+1],t[j]
            r[j],r[j+1]=r[j+1],r[j]
            w[j],w[j+1]=w[j+1],w[j]
            p[j],p[j+1]=p[j+1],p[j]
print(t)
print(p)
print(w)
pr=0
for i in range(k):
    if(y>0 and w[i]<=y):
        y=y-w[i]
        pr=pr+p[i]
    else:
        b=i
        break
if(y>0):
    pr=pr+p[b]*(y/w[b])
print(pr)
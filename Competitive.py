q=input
def f(a,z):[a.extend(list(map(int,q())))for i in z]
for i in range(int(q())):m,a,b=int(q().split()[0]),[],[];z=range(m);f(a,z),f(b,z);c=sum(a);print(-1)if c!=sum(b)else print(c-sum(map(lambda x,y:x&y,a,b)))

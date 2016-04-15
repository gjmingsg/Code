(n,m)=gets.split(" ").map{|x|x.to_i}
ar = []
n.times{ar << gets}
hs = {}
(0..m).each{|x| hs[x]=0}
for i in (0..n-1) do
    for j in (i+1..n-1) do
        count = 0
        for z in (0..m-1) do
            if ar[i][z]=="1" or ar[j][z]=="1"
                count += 1
            end
        end
        hs[count]+=1
    end
end
#puts hs
t=hs.to_a
i=t.size-1
while t[i]==0 and i >=0
    i-=1
end
#puts t[i]
if i==-1
    puts 0
    puts n*(n-1)
else
    put t[i]
end

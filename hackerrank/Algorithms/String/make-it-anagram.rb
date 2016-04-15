a = [] 
b = []
t=gets
t.chomp!
t.each_char{|x|a<<x}
t=gets
t.chomp!
t.each_char{|x|b<<x}
a.sort!
b.sort!
c=[]
i,j = 0,0
while i < a.size and j < b.size
    if a[i] < b[j]
        i+=1
    elsif a[i]>b[j]
        j+=1
    else
        c<<a[i]<<b[j]
        i+=1
        j+=1
    end
end
puts a.size + b.size - c.size

t = gets.to_i
t.times{
    (n, k) = gets.split.map{|i| i.to_i}
   
    t = 0
    ar = gets.split(" ").map{|y| y.to_i}
    ar.each{|z| t+=1 if z<=0 }        
    if t>=k     
        puts "NO"
    else
        puts "YES"
    end
}

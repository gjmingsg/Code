t = gets.to_i
t.times{
    (n, c, m) = gets.split.map{|i| i.to_i}
    
    answer = 0
    # Write code to Compute Answer
    answer = (n/c).floor
    t1 = answer
    t2 = (t1 / m).floor
    while t1 >= m do
        answer += t2
        t1 = t2+t1%m
        t2 = (t1 / m).floor
    end
    puts answer
}


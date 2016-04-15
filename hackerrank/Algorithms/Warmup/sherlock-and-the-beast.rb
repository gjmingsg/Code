t = gets.to_i
t.times{
    n = gets.to_i
    t = n
    flag = true
    for i in (0..n) do
      t = n - i
      if t%3==0 and i%5==0
        puts "5"*t + "3"*i
        flag = false
        break
      end
    end
    if flag
      puts "-1"
    end
}

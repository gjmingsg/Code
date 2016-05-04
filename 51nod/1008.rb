tmp = gets.split /\s/
x = tmp[0].to_i
y = tmp[1].to_i

n = 1
(1..x).each{|i| n=n*i}
puts n%y
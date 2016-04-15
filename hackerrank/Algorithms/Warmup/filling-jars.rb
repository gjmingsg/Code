s = gets.split(" ").map{|x| x.strip.to_i}
n = s[0]
m = s[1]
sum = 0
for i in (1..m) do
  s = gets.split(" ").map{|x| x.strip.to_i }
  a = s[0]
  b = s[1]
  k = s[2]
  sum +=  (b-a+1)*k
end
puts (sum/n).floor


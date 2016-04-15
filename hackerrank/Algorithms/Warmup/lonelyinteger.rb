#!/bin/ruby
def  lonelyinteger( a) 
	b = Array.new(101,0)
	a.each{|x| b[x] +=1}
	for i in 0..100
		if b[i]==1
			return i
		end
	end
end
a = gets.strip.to_i
b = gets.strip.split(" ").map! {|i| i.to_i}
print lonelyinteger(b)

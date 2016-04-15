#!/usr/bin/ruby
def maxXor(l, r)
	max = -1
	for i in l..r
		index = i - l
		for j in l+index..r
			a=j^i
			max = a if max < a
		end
	end
	max
end
l = gets.to_i
r = gets.to_i
print maxXor(l, r)

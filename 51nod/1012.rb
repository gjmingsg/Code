class P1012
	def gcd(a,b)
			while a>0 do
					t  = a
					a = b%a
					b = t
			end
			b	
	end
	def lcm(a,b)
			a* b / gcd(a,b) 
	end
end

c = P1012.new
s = gets().split(' ')
a = s[0].to_i
b = s[1].to_i
puts c.lcm(a,b)
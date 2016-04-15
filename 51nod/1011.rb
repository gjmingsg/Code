class P1011
	def gcd(a,b)
			while a>0 do
					t  = a
					a = b%a
					b = t
			end
			b	
	end
end

c = P1011.new
s = gets().split(' ')
a = s[0].to_i
b = s[1].to_i
puts c.gcd(a,b)
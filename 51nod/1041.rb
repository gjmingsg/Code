class P1014
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
	def sum(n)
		sum=0
		(1..n).each do |x|
			sum+=lcm(n,x)
		end
		sum
	end
end

c = P1014.new
t = gets().to_i
(1..t).each do |x|
	n 	= gets.to_i
	puts c.sum(n)
end

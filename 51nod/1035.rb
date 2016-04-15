class P1035
	def cal(n)
		dic={}
		m=1
		i = 1
		while m!=0
			if n>m
				m*=10
			end
			if m>=n
				m = m % n
				if dic.has_key?(m)
					return i - dic[m]
				else
					dic[m] = i
				end
			end
			i+=1
		end
		return m
	end
	def max(n)
		m = 0
		num = 1
		(1..n).each do |x|
		    t = cal(x)
			if m < t
				m = t
				num = x
			end
		end
		num
	end
end

c = P1035.new
=begin
puts c.cal(2)
puts c.cal(7)
puts c.cal(9)
=end
n = gets.to_i
puts c.max(n)
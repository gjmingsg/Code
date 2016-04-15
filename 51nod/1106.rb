class P1106
	def isprime(n)
		r = Math.sqrt(n).floor
		(2..r).each do|x|
			if n % x == 0
				return false
			end			
		end
		return true
	end
end

p = P1106.new

n = (gets.to_i)

(1..n).each do|x|
	x = gets.to_i
	if p.isprime(x)
		puts 'Yes'
	else
		puts 'No'
	end
end
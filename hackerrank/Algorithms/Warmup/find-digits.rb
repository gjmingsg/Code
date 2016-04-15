def solve(n)
	t = n
	count = 0
	while t>0 do
		digits = t % 10
		if digits>0 and  n%digits==0
			count +=1
		end
		t /= 10
	end
	count
end


t = gets.to_i
(1..t).each do |x|
	n = gets.to_i
	puts solve(n)
end

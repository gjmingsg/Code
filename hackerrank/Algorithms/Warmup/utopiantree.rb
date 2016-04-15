class Utopiantree
		def grow(n)
			@begin=1
			(1..n).each do |i|
				if i%2==0
					@begin += 1
				else
					@begin *=2
				end
			end
			return @begin
		end
end
	

t = Utopiantree.new
testcase = gets.to_i()
(1..testcase).each do |i|
	
	n = gets.to_i
	puts t.grow(n)
end

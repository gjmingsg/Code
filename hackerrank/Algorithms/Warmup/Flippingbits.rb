class Flippingbits
	def flip(x)
		ans = String.new
		n = (x.to_i().to_s(2).rjust(32,'0'))
		 n.each_char do|x|
			if x == '0'
				ans<<'1'
			else
				ans<<'0'
			end
		end
		 #puts n
		 #puts ans
		 ans.to_i(2)
		
	end
	
end

p = Flippingbits.new
n = gets.to_i
(1..n).each do |i|
	x = gets
	puts p.flip(x)
end

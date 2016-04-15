class P1087
		def is_one
			t = gets.to_i
			(1..t).each do|x| 
				pos = gets.to_i
				n = ((Math.sqrt(8*pos-7) - 1)/2).to_i
				if (n*n +n + 2 == 2* pos)
					puts "1"
				else
					puts "0"
				end
			end
		end
end
	
c = P1087.new
c.is_one
class TheLoveLetterMystery
	def solve()
		
		t = gets.to_i
		
		for  i in 0..t-1
			s = gets
			s.chomp!
			count =  0
			len = s.size/2 - 1
			for j in 0..len
				#puts "#{s[j]} #{s[s.size-j-1]} #{s[j] .ord - s[s.size-1-j].ord}  #{count}"
				count += (s[j] .ord - s[s.size-1-j].ord).abs
			end
			puts count
		end
		
	end
end

c = TheLoveLetterMystery.new
c.solve

class P1137
		def mul()
			@m3 = []
			@m1.each do |x|
				j= 0
				ar = []
				while @n >j do
					t,i = 0,0
					while @n > i do
						t += x[i] * @m2[i][j]
						i += 1
					end
					ar << t
					j += 1
				end
				@m3 << ar
			end
			@m3.each do |x|
				puts x.join(' ')
			end
		end
		def createMatrix()
			@m1 = []
			@m2 = []
			@n = gets().to_i
			(1..@n).each do  |x| 
				t =[]
				gets().split(' ').each{|i| t<< i.to_i}
				@m1<< t
			end
			(1..@n).each do  |x| 
				t =[]
				gets().split(' ').each{|i| t<< i.to_i}
				@m2<< t
			end
		end
end

c = P1137.new

c.createMatrix
c.mul()
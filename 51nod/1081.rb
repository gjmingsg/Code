class 	P1081
		def read_data
			@array = [0]
			@pos = []
			@n = gets.to_i
			 (1..@n).each do |x| 
				@array << (@array[x-1] + gets.to_i )
			 end
			 @q = gets.to_i
			  (1..@q).each{|x| @pos << gets.chomp.split(" ").map {|i| i.to_i}}
			  #puts "N=#{@n} array=#{@array.inspect} q = #{@q} pos=#{@pos.inspect}"
		end
	  
		def cal_sum
			(1..@q).each do |x|	
				i = @pos[x-1][0] 
				l = @pos[x-1][1] + i 
				puts @array[l-1] -@array[i-1]
			end
		end
end

c = P1081.new
c.read_data
c.cal_sum

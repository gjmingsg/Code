class Tutorialintro
	def read_data()
		@v = gets.to_i
		@n = gets.to_i
		@ar = []
		s = gets.split(' ')
		(0..@n-1).each { |x| @ar << s[x].to_i}
	end
	
	def find_index()
		size = @ar.size
		e,b = size-1,0
		while e - b > 1 do
			m = (e + b)/2
			if @ar[m] >@v
				e=m-1
			else
				b = m
			end
			puts "#{b} #{e} #{m}  #{@ar[m]}"
		end
		if @ar[b] == @v
			b
		elsif @ar[e]==@v
			e
		else
			nil
		end
		
	end
	
end

#puts 1
#=begin
c = Tutorialintro.new
c.read_data()
puts c.find_index()
#=end
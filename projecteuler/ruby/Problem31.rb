class Problem31
	def initialize()
		@ans = Hash.new
		@muler = Hash.new
		@muler2 = Hash.new
		@l = Array.new
		(0..200).each{|x| @ans[x]=0}
		(0..200).each{|x| @muler2[x]=1}
	end
	
	def mul(a)
		convert(a)
		@muler.each do|keyo,valo|
			@muler2.each do|key,val|
				if (keyo+key)<201
					@ans[keyo+key] = @ans[keyo+key]  + valo * val
				end
				
			end
			
		end
		@ans.each{|key,val|@muler2[key]=val}
		puts "1) #{@ans.inspect}"
	end
	def convert(range)
		range.each{|x| @muler[x]=1}
	end
	
	def show()
		#mul((0..200))
		#puts "1) #{@ans.inspect}"
		mul((0..200).step(2))
		#puts "1) #{@ans}"
		mul((0..200).step(5))
		#puts "1) #{@ans}"
		mul((0..200).step(10))
		#puts "1) #{@ans}"
		mul((0..200).step(20))
		#puts "1) #{@ans}"
		mul((0..200).step(50))
		#puts "1) #{@ans}"
		mul((0..200).step(100))
		#puts "1) #{@ans}"
		mul((0..200).step(200))
		#puts "1) #{@ans}"
		puts @ans[200]
	end
	
end

p = Problem31.new
p.show()
#p.mul((0..200).step(2))
#(1..12).step(2).each{|x| puts x}


class P1264
	def readcase()
		@x1=gets.to_f
		@y1=gets.to_f
		@x2=gets.to_f
		@y2=gets.to_f
		
		@x3=gets.to_f
		@y3=gets.to_f
		@x4=gets.to_f
		@y4=gets.to_f
	end
#两条线平行
#两线不平行
	def iscross
		if isparall
			
		else
			
		end
	end
	
	def isparall
			(@y2-@y1)*(@x4-@x3) == (@y4-@y3)*(@x2-@x1)
	end
	
end

c = P1264.new()
testcase = gets.to_i
(1..testcase).each do |i|
	c.readcase()
	puts c.iscross
end

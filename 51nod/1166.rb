class P1166
	def sqrt(q)
		@x = q.to_i
		r0 = Math.sqrt(@x).floor
		
		r1 = ((r0 + @x / r0) / 2).floor
		while (@x-r0*r0).abs >1
			r0 = r1
			r1 = ((r0 + @x / r0) / 2)
			puts"#{r0}=#{r0*r0}\n#{r1}=#{r1*r1}\nx=#{@x}"
		end
	
		if  r0 < r1
			r0
		else
			r1
		end
	end
	def isequal(r0,r1)
		puts"#{r0}=#{r0*r0}\n#{r1}=#{r1*r1}\nx=#{@x}"
		(r0*r0 < @x and r1*r1 > @x) or (r0*r0> @x and r1*r1 < @x )
	end
	def isless(r0,r1)
		r0*r0 > @x and r1*r1 > @x
	end
	def ismore(r0,r1)
		 r0*r0< @x and r1*r1 < @x 
	end
	
end


p = P1166.new
q = '4610883590567611257098989898988888888888888888888888877777777777777777777777777777777777777777777777'
x = p.sqrt(q)
puts x
puts q
puts q.to_i-x*x
=begin
puts x*x
puts q
puts 67903487322578736104414314797260129834195195265025 * 67903487322578736104414314797260129834195195265025
'67903487322578736104414314797260129834195195265024'
'67903487322578736104414314797260129834195195265025'
=end
#puts p.sqrt(gets)

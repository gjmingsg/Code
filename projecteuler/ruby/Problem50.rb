class Problem50
	def initialize()
		@size = 1000000
		@parray = Array.new(@size + 1 ){|i|i}
	end
	
	def getprimes()
		@parray[0]=0
		@parray[1]=0
		(2..@size).each do|x|
			if @parray[x]>0
				t = (2*x)
				(t..@size).step(x) do|y| 
					@parray[y]=0 
				end
			end
		end
		t = @parray.select{|x|x>0}
		
		@maxp=2
		 size = t.size - 1
		 @maxlen=1
		 i=0
		 while size - i > @maxlen and  i<size do
			 len = 0
			 p=0
			 (i..size).each do |inx|
			 
					p += t[inx]
					len += 1
					if (p<=@size and @parray[p]>0 and @maxlen < len)
						@maxlen = len
						@maxp=p
					end
			 
			end
			i+=1
		end
		return @maxp
	end
end

p = Problem50.new


puts p.getprimes
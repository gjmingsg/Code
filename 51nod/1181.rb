class P1181
	def initialize()
		@size = 1000000
		@parray = Array.new(@size + 1 ){|i|i}
		#@parray2 = Array.new(@size + 1 ){|i|i}
	end
	def getp(n)
		@parray[0]=0
		@parray[1]=0
		(2..@size).each do|x|
			if @parray[x]>0
				t = (2*x)
				(t..@size).step(x) do|y| 
					@parray[y]=0 
					#@parray2.delete_at(y)
				end
				
			end
		end
		list = @parray.select{|x| x>0}
		i = 0
		#list.each{|x| puts "#{i+=1}, #{x}\n"}
		while @parray[n]==0 or list.index(n).nil? or @parray[list.index(n)+1]==0
			n+=1
		end
		n
		#@parray
	end
	
end

p = P1181.new

puts p.getp(gets().to_i)
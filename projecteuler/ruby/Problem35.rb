class Problem35
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
		#0,2,4,5,6,8
		t = @parray.select{|x|x>0 and (x.to_s().size()==1 or (x.to_s().index(/[024568]/).nil? and iscircluar(x)))} 
		
		 puts t
		 puts t.size
		 
	end
	def iscircluar(x)
		t = x.to_s
		a = []
		t1 = t
		(1..t.size-1).each do|i|
			t2 =(t1[1..t.size-1]<<t1[0])
			a<<t2.to_i
			t1 = t2
		end
		flag = true
		a.each do |item|
			if @parray[item]==0
				flag=false
				return
			end
		end
		return flag
	end
	
end

p = Problem35.new
#p.iscircluar(123456)

p.getprimes
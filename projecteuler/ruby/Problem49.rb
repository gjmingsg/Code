class Problem49
	def initialize()
		@size = 10000
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
		
		t = @parray.select{|x|x>0 and x.to_s().size()==4 and isseq(x)} 
		 
		puts t
		
		
	end
	#ÅĞ¶ÏÊÇ·ñÎªĞòÁĞ
	def isseq(x)
		t = x.to_s
		a = []
		t.each_char{|x| a<<x}
		
		p = a.permutation(a.size).to_a().select{|x|  (x[x.size-1]=~/[024568]/).nil?}
		
		seq = []
		flag = 0
		p.each do |item|
		    digits = item.join().to_i
			if @parray[digits]>0 and digits > 1000
				flag+=1
				seq<<digits
			end
		end
		
			
		if flag>=3
			z = seq.combination(3).to_a().select do|parr|
				parr.sort!
				if (parr[1]-parr[0] == parr[2]-parr[1]) and  (parr[2]-parr[1]>0)
					 true
				else
					 false
				end
			end
		 
			return z.size>=1
		end
		return false
	end
	
end

p = Problem49.new
#p.iscircluar(123456)

p.getprimes
class Problem43
	@@sum=0
	@@count=0
	
	def initialize()
		@Digits=[1,2,3,4,5,6,7,8,9,0]#[1,4,0,6,3,5,7,2,8,9]#
	end
	def GetNum(indexlist)
		indexlist.inject(0) {|sum, i| sum *10 + @Digits[i]}
	end
	
	def GenerateNum(n)
		
		if n >= 9
			if check()
				@@count = @@count +1
				@@sum = @@sum +GetNum([0,1,2,3,4,5,6,7,8,9])
				puts "#{@@sum} #{@@count}:#{GetNum([0,1,2,3,4,5,6,7,8,9])}" 
			end
			
			return
		end
		
		(n...10).each do  |x|
			swap(x,n)
			
			GenerateNum(n+1)
			
			swap(x,n)
		end
		 
	 end
	 def swap(i,j)
		 t = @Digits[i]
		@Digits[i] = @Digits[j] 
		@Digits[j]  = t
	end
	def check()
		Rule1() and Rule2()  and Rule3()  and Rule4()  and Rule5()  and Rule6()  and Rule7() and Rule8()
	end
	
	def Rule1()
		@Digits[3] % 2 == 0
	end
	
	def Rule2()
		GetNum([2,3,4])%3==0
	end
	
	def Rule3()
		@Digits[5]  == 0 or @Digits[5]  == 5
	end
	
	def Rule4()
		GetNum([4,5,6])%7==0
	end
	
	def Rule5()
		GetNum([5,6,7])%11==0
	end
	
	def Rule6()
		GetNum([6,7,8])%13==0
	end
	
	def Rule7()
		GetNum([7,8,9])%17==0
	end
	def Rule8()
		@Digits[0]  !=0
	end
end

p = Problem43.new

#puts p.GetNum([0,1,2,3,4,5,6,7,8,9])
puts p.GenerateNum(0)

 


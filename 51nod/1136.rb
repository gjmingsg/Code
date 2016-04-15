class P1136
	def initialize()
		@dic = {}
	end
	def get_prime_set(n)
		p = Array.new(n + 1 ){|i|i}
		p[0]=0
		p[1]=0
		(2..n).each do|x|
			if p[x]>0
				t = (2*x)
				(t..n).step(x) do|y| 
					p[y]=0 
				end
			end
		end
		t = p.select{|x|x>0} 
	end
	
	def find_prime(n)
		r = Math.sqrt(n).floor
		set = get_prime_set(r)
		#puts set.inspect
		set.each do |x|
			while n % x==0 and n>0 do
					if @dic.has_key?(x)
						@dic[x] +=1
					else
						@dic[x]=1
					end
					n /= x
			end	
		end
		if n>1
			@dic[n]=1
		end
		#puts @dic.inspect
	end
	
	def phi(n)
		find_prime(n)
		
		@dic.each_key do |x|
			n= n* (x-1)
		end
		@dic.each_key do |x|
			n = n / x
		end
		n
	end
	
end

c = P1136.new
#puts c.find_prime(34).inspect
#puts c.phi(34)
#==16
puts c.phi(gets.to_i)
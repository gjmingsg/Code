class P1242
	def f(n)
		if n==0
			0
		else
			1
		end
			
		f0 = 0
		f1 = 1
		i=2
		while i<=n do
			t = f1
			f1 =( f1+f0)%1000000009
			f0 = t
			i+=1
		end
		
		f1 
	end
	
end


p = P1242.new

puts p.f(gets.to_i)

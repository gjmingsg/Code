
class Fibo
	def initialize
		f0 = 0
		f1 = 1
		@fibolist = Array.new
		@fibolist<<f0
		@fibolist<<f1
		while f1< 10000000000 do
			t = f1
			f1 = f1+ f0
			f0=t
			@fibolist<<f1
		end
		#puts @fibolist
	end
	
	def IsFibo(n)
		for t in @fibolist do
			if n==t
				puts "IsFibo"
				break
			elsif n<t
				puts "IsNotFibo"
				break
			end
		end
	end
end


t = gets.to_i
c = Fibo.new
for i in 1..t
	n = gets.to_i
	c.IsFibo(n)
end
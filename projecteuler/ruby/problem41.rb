class Problem41
	def getprime()
		(1..9).each do |n|
			digits=[]
			(1..n).each{|x| digits<<x}
			darray = digits.permutation(n).to_a().select{|x|(x[x.size-1]=~/[24568]/).nil?}
			l = darray.select {|x| isprime(getnum(x))}
			puts "#{l}"
		end

	end
	def getnum(x)
		num = 0
		x.each{|i|  num=num*10 + i}
		num
	end
	
	def isprime(n)
		r = Math.sqrt(n).floor
		(2..r).each do|x|
			if n % x == 0
				return false
			end
		end
		return true
	end
end


p = Problem41.new

#puts p.getnum([1,2,3,4,5])
puts p.getprime
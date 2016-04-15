class P1018
	def readArray()
		@n =gets().to_i
		@array = []
		(1..@n).each do |x|
			@array << gets().to_i
		end
	end
	
	def sort(l,h)
			##¹é²¢ÅÅĞò
			return if l >=h 
			m = (l+h)/2
			sort(l,m)
			sort(m+1,h)
			merge(l,h,m)
	end
	
	def merge(l,h,m)
			i = 0
			j = m + 1
			k = l
			ta = []
			for z in (l..m) do
				ta<<@array[z]
			end
			while i <= m-l do
				if  j <= h && ta[i] > @array[j]
					@array[k] = @array[j]
					j+=1
				else
					@array[k] = ta[i]
					i+=1
				end
				k+=1
			end
	end
	
	def print
			sort(0,@n-1)
			@array.each{|x| puts x}
	end
	
end

c = P1018.new

c.readArray

c.print
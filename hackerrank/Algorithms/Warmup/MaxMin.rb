class MaxMin
	def solve(lst,k)
		lst.sort!
		min = 1000000000
		(k..lst.size).each do |x|  
			t = lst[x-1]-lst[x-k]
			min = t if min>t
		end
		return min
	end
	
end
# Code required to read in the values of k,n and candies.
n = gets.to_i
k = gets.to_i
candy = Array.new(n)
for i in 0..n-1
      candy[i] = gets.to_i
  end
  c = MaxMin.new
ans = c.solve(candy,k)### Compute answer from k, n, candies
puts ans

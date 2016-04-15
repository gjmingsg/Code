class P1305
	def fun(ar)
		sum=0
		for i in (0...ar.size) do
			for j in (i+1...ar.size) do 
				sum+=  (ar[i] +ar[j]) .floor
			end
		end
		sum
	end
end

n = gets.to_i
ar = []
(1..n).each do |x|
	ar << 1/ gets.chomp.to_i;
end

c = P1305.new
puts c.fun(ar)

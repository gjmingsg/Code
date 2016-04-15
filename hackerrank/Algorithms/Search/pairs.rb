class Pairs
	def solve()
		s = gets.split(" ")
		n = s[0].to_i
		k = s[1].to_i
		ar = gets.chomp.split(" ").map {|i| i.to_i};
		hs = {}
		ar.each{|x| hs[x] = 0}
		ar.map! {|i| i+k};
		count=0
		ar.each do |x|
			if hs.has_key?(x)
				count+=1
			end
		end
		count
	end
end

c = Pairs.new
c.solve

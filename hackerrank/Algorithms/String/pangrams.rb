class Pangrams
	def solve
		hs = {}
		('a'..'z').each {|x| hs[x]=0}
		s = gets
		s.downcase!
 
		s.each_char do |x|
			if ('a'..'z').include?(x)
				hs[x] +=1
			end
		end
 
		t = hs.select{|k,v| v==0}
		t.size==0
	end
end

c = Pangrams.new
if c.solve
	puts "pangram"
else
	puts "not pangram"
end

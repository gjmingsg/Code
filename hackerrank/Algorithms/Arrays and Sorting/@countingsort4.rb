def countingsort(ar)
	countlist=Array.new(100){|i| 0}
	ar.each{|x| countlist[x] += 1}
	
	#puts countlist.inspect
	for i in (1..99) do
		 countlist[i] += countlist[i-1]
	end
	 s = []
	 for i in (0..99) do
		s << br[countlist[i]-1]
	 end
	puts s.join(" ")
end

ar = []
br =[]
cnt = gets.to_i
(1..cnt).each do |x| 
	i = gets.strip.split(" ")[0].to_i 
	s = gets.strip.split(" ")[1]
	ar << i
	br << s
end
countingsort(ar)
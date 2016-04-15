def countingsort(ar)
	countlist=Array.new(100){|i| 0}
	ar.each{|x| countlist[x] += 1}
	
	#puts countlist.inspect
	for i in (1..99) do
		 countlist[i] += countlist[i-1]
	end
	 
	puts countlist.join(" ")
end

ar = []
cnt = gets.to_i
(1..cnt).each {|x| ar << gets.strip.split(" ")[0].to_i}
countingsort(ar)
def  insertionSort( ar) 
	v = ar.last
	last = ar.size-2
	while ar[last]>v and last>=0 do
		ar[last+1] = ar[last]
		last -= 1
		puts ar.join(" ")
	end
	ar[last+1] = v
	puts ar.join(" ")
end

count = gets.to_i
ar = gets.strip.split.map {|i| i.to_i}

insertionSort( ar )

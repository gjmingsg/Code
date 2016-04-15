#!/usr/bin/ruby
def  insertionSort(ar) 
	count=0
    if ar.size>1
		i = 1
		while i < ar.size do
			v = ar[i]
			last = i-1
			while ar[last]>v and last>=0 do
				ar[last+1] = ar[last]
				last -= 1
				count +=1
			end
			ar[last+1] = v
			#puts ar.join(" ")
			i+=1
		end
	end
	puts count
end
cnt = gets.to_i
ar = gets.strip.split(" ").map! {|i| i.to_i}
insertionSort(ar)


def quickSort(ar) 
	@quickSortCount=0
	partition(ar,0,ar.size)
	ar
end
def  partition(ar,first,last) 
	
	return if (last-first)<=1
	 small_i = first-1
	 big_i=first
	 p = ar[last-1]
	 (first..last-2).each do|x|
		if ar[x]>p
			big_i=x
		elsif  ar[x]<p
			@quickSortCount+=1
			if small_i+1< x
				ar[small_i+1],ar[x] = ar[x] ,ar[small_i+1]
				small_i += 1
				big_i = x
				
			else
				small_i =x
			end
		end
	end
	ar[small_i+1],ar[last-1] = ar[last-1] ,ar[small_i+1]
	@quickSortCount+=1
	m = small_i+1
	#puts ar.join(" ")
	partition(ar,first,m)
	partition(ar,m+1,last)
end


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
	count
end


cnt = gets.to_i;
ar = STDIN.gets.chomp.split(" ").map {|i| i.to_i};
br = ar.clone
quickSort(ar);

count =  insertionSort(br) 
puts count - @quickSortCount
=begin
ar = %w[1 3 9 8 2 7 5].map {|i| i.to_i};
quickSort(ar)
puts @@quickSortCount
ar = %w[1 3 9 8 2 7 5].map {|i| i.to_i};
count =  insertionSort(ar) 
puts count
puts count - @@quickSortCount
=end
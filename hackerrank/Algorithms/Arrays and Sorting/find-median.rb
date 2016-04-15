def find_median(ar)
	m = ar.size / 2 - 1
	partition(ar,0,ar.size)
	ar[m]
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
 
	m = small_i+1
	#puts ar.join(" ")
	partition(ar,first,m)
	partition(ar,m+1,last)
end

cnt = gets.to_i;
ar = STDIN.gets.chomp.split(" ").map {|i| i.to_i};
find_median(ar)
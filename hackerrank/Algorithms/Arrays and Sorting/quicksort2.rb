def quickSort(ar) 
	partition(ar,0,ar.size)
	ar
end
def  partition(ar,first,last) 
	if (last-first)>1
		  p = ar[first]
		  small = []
		  big = []
		  i=first+1
		  
		  while i<last do 
				x = ar[i]
				if x<p
				  small << x
				else
				  big << x
				end
				i+=1
			end
		
			m = first+small.size
			j= 0
			for i in (first..m-1) do
				ar[i] = small[j]
				j+=1
			end
			ar[m] = p
			j = 0
			for i in (m+1..last-1) do
				ar[i] = big[j]
				j+=1
			end
		    
			partition(ar,first,m)
		
			partition(ar,m+1,last)
	
	end
end
#puts 1
cnt = gets.to_i;
ar = STDIN.gets.chomp.split(" ").map {|i| i.to_i};
quickSort(ar);

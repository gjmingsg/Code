# Enter your code here. Read input from STDIN. Print output to STDOUT
def GameOfThronesI(s)
	ap = Hash.new
	
	s.each_char do|c| 
		if ap.has_key?(c) 
			ap[c]+=1 
		else 
			ap[c]=1
		end
	end
	#puts ap
	c=ap.count{|k,v| v % 2 ==1}
	if c==1 or c==0
		0
	else
		1
	end
end

string = gets.chomp 

found = 0
# Assign found a value of 1 or 0 depending on whether or not you found what you were looking for.

if found == GameOfThronesI(string)
    puts "YES"
else
    puts "NO"
end

t = gets.to_i
for i in 1..t
	s = gets
	a=""
	s.each_char{|c| a<< c if a.size==0 or a[-1]!=c}
	puts s.size - a.size
end

class Closestnumbers
	def reasd_data
			@n = gets.to_i
			@ar = gets.split(" ").map{|x| x.to_i}
			@ar.sort!
			#puts "#{@n} #{@ar}"
	end
	
	def print_data
		b = []
		for i in (0..@n-2) do
			b<< {@ar[i] => @ar[i+1]-@ar[i], }
		end
		t = b.sort{|a,b| a.values[0]<=>b.values[0]}

		v = t[0].values[0]
		#puts "#{v}"
		s=[]
		t = t.select{|x| x.values[0]==v}
		#puts "#{t}"
		t=t.sort{|a,b| a.keys[0]<=>b.keys[0]}
		t.each { |x|s<< (x.keys[0].to_s)+" " + (x.keys[0]+x.values[0]).to_s }
		puts s.join(" ")
	end
end

c = Closestnumbers.new
c.reasd_data
c.print_data
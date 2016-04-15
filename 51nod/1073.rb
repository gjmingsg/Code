=begin
class Node
	attr_accessor:val,:next
	def initialize(x)
		@val = x
		@next=nil
	end
end

class P1073
		def read_data()
			s= gets.split(' ')
			@n = s[0].to_i
			@k = s[1].to_i
		end
		
		def create_range
			@head = Node.new(1)
			t = @head
			(2..@n).each do|x|
				t.next = Node.new(x)
				t = t.next
			end
			t.next = @head
		end
		def show_last
			
			while @head.val != @head.next.val do
				t = @head
				2.upto(@k) do |x|  
					t = @head
					@head = @head.next 
				end
				#puts @head.val
				t.next = @head.next
				t = @head
				@head = @head.next 
				t .next = nil
			end
			puts @head.val
		end
		
		def show_range
				t = @head
				while !t.nil? do
					puts "#{t.val}->"
					t = t.next
				end
		end
end
	

c = P1073.new
c.read_data()
c.create_range()
#c.show_range()
c.show_last
=end

class P1073
		def read_data()
			s= gets.split(' ')
			@n = s[0].to_i
			@k = s[1].to_i
		end
		
		def create_range
			@range = (1..@n).to_a
		end
		def show_last
			last = @k
			while @range.size>1 do
				if last < @range.size 
					@range.delete_at(last-1)
				else
					@range.delete_at((last -1) % @range.size)
				end
				last += @k + 1
				#puts @range.inspect
			end
			puts @range[0]
		end
end
	

c = P1073.new
c.read_data()
c.create_range()
c.show_last
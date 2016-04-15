class P1046
	def  initialize(a,b,c)
		@dic={}
		@a = a
		@b = b
		@c = c
	end
	def pow(a,b)
			t = 0
			if @dic.has_key?(b)
				t = @dic[b]
			else
				if b==2
					@dic[b] =a*a % @c
					t = @dic[b]
				elsif b  == 1
					@dic[b] = a % @c
					t = @dic[b]
				else
					@dic[b/2]=pow(a,b/2) % @c
					@dic[b-b/2]=pow(a,b-b/2) % @c
					t = (@dic[b-b/2] * @dic[b/2])  % @c
				end
			end
			t
	end
	def getmod
		pow(@a,@b)
	end	
end

s = gets().split(' ')
a = s[0].to_i
b = s[1].to_i
c = s[2].to_i
c = P1046.new(a,b,c)
puts c.getmod

=begin
c = P1046.new(52,14,37)
puts c.getmod == 4

c = P1046.new(4648903,9581989,4609038)
puts c.getmod == 1487395
=end

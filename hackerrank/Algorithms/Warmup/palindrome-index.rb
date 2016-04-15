t = gets.to_i
t.times{
    s = gets
    s.chomp!
    len = s.size - 1
    mid = s.size / 2
    index = -1
    for i in (0..mid)
        #puts "#{s[i]} #{s[len-i]}"
        if s[i]==s[len-i]
            next
        elsif s[i] == s[len-i-1] and s[i+1] == s[len-i-2]
            index = len-i
            break
        elsif s[i+1] == s[len-i] and s[i+2] == s[len-i-1]
            index = i
            break
        end
    end
    puts index
}


# Main file
# ruby main.rb

require './edit_distance'

def test_strings(str1, str2, expected)
  output = edit_distance(str1, str2, str1.length, str2.length)

  raise "Error for strings '#{str1}' '#{str2}'. Expected: #{expected}. Returned: #{output}." if output != expected
end

# Verified using http://www.let.rug.nl/kleiweg/lev/

# Empty strings
test_strings("", "", 0)
test_strings("", "fernando", 8)
test_strings("fernando", "", 8)

# Normal strings
test_strings("david", "fernando", 7)
test_strings("abababababa", "bababababab", 2)

# Insertion and deletion
test_strings("aaabaaaa", "aaaaaaa", 1)
test_strings("aaaaaaa", "aaaabaaa", 1)
test_strings("aaaaaaa", "baaaaaaa", 1)
test_strings("aaaaaaab", "aaaaaaaa", 1)

# Substitution
test_strings("aaaaaaa", "aaaaaax", 1)
test_strings("axaaaaa", "aaaaaaa", 1)

puts "All tests OK."
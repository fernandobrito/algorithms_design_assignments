# Print 2d table
def print_table(table)
  table.each do |row|
    p row
  end
end

# Calculates the edit distance between two strings using dynamic programming
def edit_distance(str1, str2, m, n)  
  # Initialize table to store solution of sub problems
  # with length1 + 1 rows and length2 + 1 columns
  table = []

  (m + 1).times do |row|
    table[row] = []

    (n + 1).times do |column|
      table[row][column] = nil
    end
  end

  # Fill the table, column-wise, starting from (0, 0)
  (m + 1).times do |row|
    (n + 1).times do |column|

      # When one string is empty, we consider its cost
      # as inserting all elements from the other string
      if row == 0
        table[row][column] = column
      elsif column == 0
        table[row][column] = row
      
      # If last chars from both strings are equal,
      # nothing is added to the cost, and cost is equal
      # to comparing both substrings with -1 length
      elsif str1.chars[row-1] == str2.chars[column-1]
        table[row][column] = table[row-1][column-1]

      # If last chars are different, add one to the cost of
      # the optimal (minimum) subsolution either adding, removing
      # or replacing char
      else
        table[row][column] = 1 + [table[row][column-1], table[row-1][column], table[row-1][column-1]].min
      end
    end
  end

  # print_table(table)

  return table[m][n]
end
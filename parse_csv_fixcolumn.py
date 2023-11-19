## Purpose:  Parse a csv file.
##           If a row has two columns, output it as is.
##           If a row has one column, add a second column
##           and populate that second column with the most recent 2nd column value + 1
##           The results will be csv file and every row has 2 columns
##           the second column has integer values.

import csvr
        
input_file = "C:/Temp/input.csv"  
output_file = "C:/Temp/output.csv" 

with open(input_file, 'r') as csv_in, open(output_file, 'w', newline='') as csv_out:

    writer = csv.writer(csv_out)
    rownum = 0  
    next_id = 1

    for line in csv_in:

        rownum += 1
        columns = line.strip().split(',')
        num_cols = len(columns)

        if num_cols == 2:

            writer.writerow(columns)
            cur_id = columns[1]
            next_id = int(cur_id) + 1    

        if num_cols == 1: 

            columns.append(next_id)
            writer.writerow(columns)
            num_cols = 2

        print(str(rownum) + str(num_cols))

exit()
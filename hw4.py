
daily_yield_curves = []
with open('daily-treasury-rates-2022.csv', 'rt', encoding='utf-8') as fin:
    for line in fin:
        line = line[:-1]   # eliminate final '\n'
        row = line.split(',')
        daily_yield_curves.append(row)

# now eliminate the '4 mo' column
for row_num in range(len(daily_yield_curves)):
    # up to but not including 4 mo, and after 4 mo
    daily_yield_curves[row_num] = daily_yield_curves[row_num][:4] + daily_yield_curves[row_num][5:]

# convert each interest rate value from a str to a float:
for row in daily_yield_curves[1:]:
    row[1:] = list(map(float, row[1:]))

headers = [word.replace('"', '') for word in daily_yield_curves[0]]
daily_yield_curves[0] = headers

outf = open('daily_yield_curves_2022.txt', 'wt')
for row in daily_yield_curves:
    frmt_row = f"{row[0]: <15} {row[1]: <8} {row[2]: <8} {row[3]: <8} {row[4]: <8} {row[5]: <8} {row[6]: <8} {row[7]: <8} {row[8]: <8} {row[9]: <8} {row[10]: <8} {row[11]: <8} {row[12]: <8}\n"
    outf.write(frmt_row)

outf.close()


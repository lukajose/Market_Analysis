


tickers = open('tickers.csv','r')
Line = []
for i in tickers:
    Line.append(i.partition("\t")[0])

print(Line)

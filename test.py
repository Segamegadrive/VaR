import csv

def get_cell(x,y):
    with open('microsoft-DataAnalysis.csv', 'r') as f:
        reader = csv.reader(f)
        y_count = 0
        for n in reader:
            if y_count == y:
                cell = n[x]
                return cell
            y_count +=1


datapoint = int(input('Please enter datapoint'))
investment = int(input('Please enter investment'))


unsort_returnlist = []
for i in range(1, datapoint+1):
    unsort_returnlist.append(get_cell(7,i))
    unsort_returnfloat = [float(x) for x in unsort_returnlist]


sort_return = sorted(unsort_returnfloat)

Total = len(sort_return)
His_Var95_num = (int(round(0.05 * Total)))
His_Var99_num = (int(round(0.01 * Total)))
print(His_Var95_num, His_Var99_num)

Var95_value = investment * sort_return[His_Var95_num]
Var99_value = investment * sort_return[His_Var99_num]
print(Var95_value, Var99_value)

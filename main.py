file = open("input.txt")

numClass ,numFeature ,datasetLen = 0,0,0

lines = file.readlines()

dataset = []

count = 0
for line in lines:
    if(count==0):
        var = line.split()
        numFeature = int(var[0])
        numClass = int(var[1])
        datasetLen = int(var[2])
    else:
        var = line.split()
        data = []
        for i in var:
            data.append(int(i))
        dataset.append(data)
    count += 1

print(numFeature,numClass,datasetLen)
print(dataset)

distinct_class_list = set()

for i in dataset:
    className = i[len(i)-1]
    distinct_class_list.add(className) # if classNames are strings

distinct_feature_list = []

print('Class Names: ',distinct_class_list)

for i in range(numFeature):
    distinct = set()
    for data in dataset:
        distinct.add(data[i])
    distinct_feature_list.append(distinct)

print('Distinct Feature List: ',distinct_feature_list)    # returns unique features values for each feature






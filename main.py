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

class_count = []

for son in distinct_class_list:
    count = 0
    for i in dataset:
        if son == i[len(i)-1]:
            count += 1
    class_count.append(count)

print(class_count)

prior_probability = [ float(x/datasetLen) for x in class_count ]
print(prior_probability)

feature_likelihood = []


for son in distinct_class_list:
    each_son = []
    index = 0
    for features in distinct_feature_list:
        likelihood = []
        for feature_value in features:
            sum = 0
            for i in dataset:
                if i[index]==feature_value and i[len(i)-1]==son:
                    sum += 1
            sum = float(sum/datasetLen)
            p_x_wi = sum/prior_probability[son]
            likelihood.append(p_x_wi)
        each_son.append(likelihood)
        index += 1
    feature_likelihood.append(each_son)


print(feature_likelihood)

# Test Section
# feature value for feature 1 = 10 , feature value for feature 1 = 18
# task is to find the highest p(wi|x)

feature_value = [10,18]

indexes = []

index = 0
for features in distinct_feature_list:
    features = list(features)
    indexes.append(features.index(feature_value[index]))
    index += 1

posterior = []

for features in feature_likelihood:
    index = 0
    mul = 1
    for feature in features:
        mul *= (feature[indexes[index]])
        index += 1
    posterior.append(mul)


print()
print('Output Class: ')
print(posterior.index(max(posterior)))
        





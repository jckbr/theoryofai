import pandas, numpy
import plotly.express as px

# 1
print('1:')
n_clusters = 3 # either 2 or 3
n_iters = 25

datRaw = pandas.read_csv('cluster_data_1D.dat', names=['Value', 'Closest'])

centers = numpy.linspace(int(datRaw['Value'].min()), int(datRaw['Value'].max()), n_clusters)
centerTemp = numpy.zeros(n_clusters)
print('Initial centers:', centers)

for l in range(0, n_iters):
    for i in range(0, datRaw.shape[0]):
        # print('i:', i, 'x:', datRaw.iloc[i, 0])
        temp = datRaw.iloc[i, 0]
        for j in range(0, len(centers)):
            dist = abs(datRaw.iloc[i, 0] - centers[j])
            if dist < temp:
                datRaw.iloc[i, 1] = j
                temp = dist

    datRawGroup = datRaw.groupby('Closest').mean()
    centerTemp = datRawGroup['Value'].to_numpy()

scatterFig = px.scatter(x=datRaw['Value'], y=[0 for x in datRaw['Value']])
for i in centers:
    scatterFig.add_vline(i)
for i in centerTemp:
    scatterFig.add_vline(i, line_dash='dash', line_color='green')
scatterFig.show()

print('Cluster centers:', centerTemp, '\n')

# 3
print('3:')
k_count = 1 # either 1 or 3

trainRaw = pandas.read_csv('classify_train_1D.dat', delimiter='\s+', names=['Value', 'Class'])
testRaw = pandas.read_csv('classify_test_1D.dat', delimiter='\s+', names=['Value', 'Class'])
testRaw['Pred'] = numpy.zeros(testRaw.shape[0])
testRaw['PredVal'] = numpy.zeros(testRaw.shape[0])

dists = numpy.zeros(trainRaw.shape[0])
for i in range(0, testRaw.shape[0]):
    for j in range(0, trainRaw.shape[0]):
        dists[j] = abs(testRaw.iloc[i, 0] - trainRaw.iloc[j, 0])

    lowestK = numpy.argpartition(dists, k_count)[:k_count]

    vals, counts = numpy.unique(lowestK, return_counts=True)
    modeIndex = numpy.argmax(counts)
    mode = vals[modeIndex]

    testRaw.iloc[i, 2] = trainRaw.iloc[mode, 1]
    testRaw.iloc[i, 3] = trainRaw.iloc[mode, 0]

print(testRaw)
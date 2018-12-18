import frequency_analysis as freq

# inspired by Ikey
def test():
    words = []
    # run 10000 times
    for _ in range(10000):
        words.append(freq.test())
    trueData = freq.histogram("oneFish.txt")
    # normalize to make it comparable
    data = normalize(freq.histogram(words), trueData, 10000)
    print('Result: ', data)
    print('True: ', trueData)

# Makes data and trueData proportional
def normalize(data, trueData, total):
    trueCount = sum([trueData[i] for i in trueData.keys()])
    newData = {}
    for key, value in data.items():
        newData[key] = value * trueCount / total
    return newData


if __name__ == '__main__':
    print('Running Test...')
    test()

result = {}
i=0
with open('measurements.txt', 'r+') as file:
    while True:
        line = file.readline().rstrip()
        location, measurement = line.split(';')
        measurement = int(float(measurement)*100)
        if location not in result:
            result[location] = [1, measurement, measurement, measurement]
        else:
            l = result[location]
            l[0] += 1
            l[1] = min(l[1], measurement)
            l[2] += measurement
            l[3] = max(l[3], measurement)
            result[location] = l
        i+=1
        print(i, location ,result[location])
        if i == 100000000:
            break

resultttxt = ""
for key in sorted(result.keys()):
    resultttxt+=f'{key} {result[key][1]/100:.1f} {result[key][2]/result[key][0]/100:.1f} {result[key][3]/100:.1f}\n' 

with open('result.txt', 'w') as file:
    file.write(resultttxt)
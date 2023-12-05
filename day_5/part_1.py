import pprint

f = open("./day_5/input_text.txt", 'r')
almanac = f.readlines()
while '\n' in almanac:
    almanac.remove('\n')
   
for i in range(len(almanac)):
    almanac[i] = almanac[i].strip()

pprint.pprint(almanac)

seeds = almanac[0][almanac[0].index(":")+2:].strip().split(" ")

seedToSoilMap = almanac[2:almanac.index("soil-to-fertilizer map:")]

soilToFertilizerMap = almanac[almanac.index("soil-to-fertilizer map:")+1:almanac.index("fertilizer-to-water map:")]#

fertilizerToWaterMap = almanac[almanac.index("fertilizer-to-water map:")+1:almanac.index("water-to-light map:")]#

waterToLightMap = almanac[almanac.index("water-to-light map:")+1:almanac.index("light-to-temperature map:")]#

lightToTemperatureMap = almanac[almanac.index("light-to-temperature map:")+1:almanac.index("temperature-to-humidity map:")]#
   
temperatureToHumidityMap = almanac[almanac.index("temperature-to-humidity map:")+1:almanac.index("humidity-to-location map:")]#

humidityToLocationMap = almanac[almanac.index("humidity-to-location map:")+1:]#

def mapper(seed, convertMap):
    for line in convertMap:
        destRangeStart = int(line.split()[0])
        srcRangeStart = int(line.split()[1])
        rangeLen = int(line.split()[2])

        destRange = range(destRangeStart, destRangeStart+rangeLen)
        srcRange  = range(srcRangeStart , srcRangeStart+rangeLen )

        if seed in srcRange:
            return destRange[srcRange.index(seed)]
    return seed
    

pprint.pprint(seedToSoilMap)

def getFinalNum(seed):
    return mapper(mapper(mapper(mapper(mapper(mapper(mapper(seed,seedToSoilMap),soilToFertilizerMap),fertilizerToWaterMap),waterToLightMap),lightToTemperatureMap),temperatureToHumidityMap),humidityToLocationMap)

#print(seeds)
locations = []

for seed in seeds:
    #print(seed)
    locations.append(getFinalNum(int(seed)))


locations.sort()

print(locations[0])
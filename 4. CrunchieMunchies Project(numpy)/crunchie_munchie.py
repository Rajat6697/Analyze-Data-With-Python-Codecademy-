import codecademylib
import numpy as np

calorie_stats= np.genfromtxt('cereal.csv', delimiter= ',')
print(calorie_stats)

average_calories= np.mean(calorie_stats)
print('average_calories')
print(average_calories)

calorie_stats_sorted= np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories= np.median(calorie_stats)
print(median_calories)

tenth_percentile= np.percentile(calorie_stats, 10)
print('tenth_percentile')
print(tenth_percentile)

twentieth_percentile= np.percentile(calorie_stats, 20)
print('twentieth_percentile')
print(twentieth_percentile)

thirtieth_percentile= np.percentile(calorie_stats, 30)
print('thirtieth_percentile')
print(thirtieth_percentile)

fourtieth_percentile= np.percentile(calorie_stats, 40)
print('fourtieth_percentile')
print(fourtieth_percentile)

fiftieth_percentile= np.percentile(calorie_stats, 50)
print('fiftieth_percentile')
print(fiftieth_percentile)

sixtieth_percentile= np.percentile(calorie_stats, 60)
print('sixtieth_percentile')
print(sixtieth_percentile)

seventieth_percentile= np.percentile(calorie_stats, 70)
print('seventieth_percentile')
print(seventieth_percentile)

nth_percentile= tenth_percentile

more_calories= np.mean(calorie_stats > 60)
print(more_calories)

calorie_std= np.std(calorie_stats)
print('Standard Deviation of data is ',calorie_std)

conclusion= """Conclusions:
  1. As you can see the average calorie present in our data is 106 which is much higher than 60 calorie of our crunchiemunchies.
  2. The lowest percentile i.e. tenthpercentile is 90, which also is 30 calorie more than our crunchiemunchie whis has 60 calroie.
  3. The standard deviation of our data is 19, which shows our numbers are in clusters and close to each other and not distributed.  """

print(conclusion)

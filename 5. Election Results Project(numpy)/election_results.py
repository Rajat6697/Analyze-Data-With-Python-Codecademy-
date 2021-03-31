import codecademylib
import numpy as np
import matplotlib.pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']


total_ceballos= sum([1 for response in survey_responses if response== 'Ceballos'])
print(total_ceballos)

percentage_ceballos= 100* total_ceballos/len(survey_responses)
print(percentage_ceballos)
survey_length= len(survey_responses)
possible_surveys= np.random.binomial(survey_length, .54, 10000)/ float(survey_length)
print(possible_surveys)

plt.hist(possible_surveys, range= (0,1), bins= 20)
plt.show()

cabellos_loss_surveys= np.mean(possible_surveys< .5)
print(cabellos_loss_surveys)
len_large_survey= float(7000)
large_survey= np.random.binomial(len_large_survey, .54, 10000)/ len_large_survey
print(large_survey)

ceballos_loss_new= np.mean(large_survey< .5)
print(ceballos_loss_new)


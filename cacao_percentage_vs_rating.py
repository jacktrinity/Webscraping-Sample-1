"""
Parse through a sample content site provided by codecademy.com.
https://content.codecademy.com/courses/beautifulsoup/cacao/index.html

Using Beautifulsoup, scape, and clean data in regards to "rating" and "cacao percentage" of each chocolate bar.
Create a data frame, pairing rating and cacao percentage.
Display data frame and scatterplot with line of best-fit.
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Request
webpage_reponse = requests.get('https://content.codecademy.com/courses/beautifulsoup/cacao/index.html')
webpage = webpage_reponse.content
soup = BeautifulSoup(webpage, "html.parser")

# Empty list for collecting data for our rating.
rating_list = []
cacao_percentage_list = []

# Clean up data, stripping only the rating value and cacao percentage.
# Sample: <td class="Rating">2.75</td>
rating_leading_strip = '<td class="Rating">'
rating_ending_strip = '</td>'

# Sample: <td class="CocoaPercent">70%</td>
cacao_leading_strip = '<td class="CocoaPercent">'
cacao_ending_strip = '%</td>'

for rating_text in soup.find_all('td', class_='Rating'):
  # Data clean up for rating
  rating_str = str(rating_text)
  rating_clean1 = rating_str.replace(rating_leading_strip, '')
  rating_clean2 = rating_clean1.replace(rating_ending_strip, '')
  
  # Convert our data into a float and append it.
  try:
    rating_list.append(float(rating_clean2))
  except(ValueError):
    # If rating value isn't able to convert into a float.
    # Example, We will scape the title "Rating" before its value.
    # If that is the case, we will just ignore.
    pass

for cacao_text in soup.find_all('td', class_='CocoaPercent'):
  # Data clean up for cacao
  cacao_str = str(cacao_text)  
  cacao_clean1 = cacao_str.replace(cacao_leading_strip, '')
  cacao_clean2 = cacao_clean1.replace(cacao_ending_strip, '')

  # Convert our data into an int and append it.
  try:
    cacao_percentage_list.append(float(cacao_clean2))
  except(ValueError):
    # If cacao value isn't able to convert into a float.
    # Example, We will scape the title "Cacao Percentage" before its value.
    # If that is the case, we will just ignore.
    pass
  
# Create data frame: rating and cacao_percentage
d = {'Rating': rating_list, 'Cacao_Percentage': cacao_percentage_list} 
df = pd.DataFrame(data=d)
print(df)

# scatterplot
plt.scatter(df.Cacao_Percentage, df.Rating, edgecolor='black', linewidth=1)
plt.title("Is more cacao better?")
plt.xlabel("Cacao Percentage")
plt.ylabel("Rating 1-5")

# line of best-fit
z = np.polyfit(df.Cacao_Percentage, df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(df.Cacao_Percentage, line_function(df.Cacao_Percentage), "r--")

plt.show()

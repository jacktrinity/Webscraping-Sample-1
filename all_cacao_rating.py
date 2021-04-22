"""
Parse through a sample content site provided by codecademy.com.
https://content.codecademy.com/courses/beautifulsoup/cacao/index.html

Using Beautifulsoup, scape, and clean data in regards to "rating" of each chocolate bar.
Finally, display data in a histogram graph.
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

# Clean up data, stripping out everything and leaving only the rating value.
# Sample: <td class="Rating">2.75</td>
leading_strip = '<td class="Rating">'
ending_strip = '</td>'
for text in soup.find_all('td', class_='Rating'):
  # Data clean up
  text = str(text)
  clean1 = text.replace(leading_strip, '')
  clean2 = clean1.replace(ending_strip, '')
  
  # Convert our data into a float and append it.
  try:
    rating_list.append(float(clean2))
  except(ValueError):
    # If value isn't able to convert into a float.
    # Example, We will scape the title "Rating" before its value.
    # If that is the case, we will just ignore.
    pass
  
# Output a historgram graph of our data
plt.hist(rating_list, edgecolor='black', linewidth=1)
plt.xlabel('Rating from 1-5')
plt.ylabel('Compiled ratings of over 1700 Chocolate bars')
plt.title('Cacao Ratings')
plt.show()

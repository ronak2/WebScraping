#Author: Ronak Trivedi
#Purpose: Take the user on a dereive through the most imminent hackathons
#Critical imports
from flask import Flask, render_template
from bs4 import BeautifulSoup #Parsing agent
import re
import requests


app = Flask(__name__)

#Initializing list of the hottest topics in computer science
appList = ['Artificial Intelligence', 'Blockchain', 'Machine Learning', 'BioMedical', 'Mobile App Development']

#Storing the constant user agent
mozillaConstant = 'Mozilla/5.0'
hackathons = []

#Initializing the web app's home page
@app.route('/')     
def index():
    topic1 = appList[0]
    topic2 = appList[1]
    topic3 = appList[2]
    topic4 = appList[3]
    topic5 = appList[4]
    return render_template('index.html',topic1 = topic1, topic2 = topic2, topic3 = topic3, topic4 = topic4, topic5 = topic5)

#Starting the dereive in Artificial Intelligence
@app.route('/artificialintel')     
def artificialintel():
  result = requests.get("https://devpost.com/hackathons?utf8=✓&search=artificial+intelligence&challenge_type=all&sort_by=Recently+Added")
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  featured_events = soup.find_all('a',attrs={'data-role': 'featured_challenge'})
  
  for featured_challenge in featured_events:
      hackathons.append(featured_challenge.attrs['href'])
  
  output1 = hackathons[0]
  output2 = hackathons[1]
  output3 = hackathons[3]
  hackathons.clear()
  return render_template("artificialintel.html", output1 = output1, output2 = output2, output3 = output3 )



#Setting a route for the second step in the dereive
@app.route('/blockchain')
def blockchain():
  result = requests.get("https://devpost.com/hackathons?utf8=✓&search=blockchain&challenge_type=all&sort_by=Recently+Added")
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  featured_events = soup.find_all('a',attrs={'data-role': 'featured_challenge'})
  
  for featured_challenge in featured_events:
      hackathons.append(featured_challenge.attrs['href'])
  
  output1 = hackathons[0]
  output2 = hackathons[1]
  output3 = hackathons[3]
  hackathons.clear()
  return render_template("blockchain.html", output1 = output1, output2 = output2, output3 = output3)

#Setting a route for the third step in the dereive
@app.route('/machinelearning')
def machinelearning():
  result = requests.get("https://devpost.com/hackathons?utf8=✓&search=machine+learning&challenge_type=all&sort_by=Recently+Added")
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  featured_events = soup.find_all('a',attrs={'data-role': 'featured_challenge'})
  
  for featured_challenge in featured_events:
      hackathons.append(featured_challenge.attrs['href'])
  
  output1 = hackathons[0]
  output2 = hackathons[1]
  output3 = hackathons[3]
  hackathons.clear()
  return render_template("machinelearning.html", output1 = output1, output2 = output2, output3 = output3 )


#Setting a route for the fourth step in the dereive
@app.route('/biomedical')
def biomedical():
  result = requests.get("https://devpost.com/hackathons?utf8=✓&search=biomedical&challenge_type=all&sort_by=Recently+Added")
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  featured_events = soup.find_all('a',attrs={'data-role': 'featured_challenge'})
  
  for featured_challenge in featured_events:
      hackathons.append(featured_challenge.attrs['href'])
  
  output1 = hackathons[0]
  output2 = hackathons[1]
  output3 = hackathons[3]
  hackathons.clear()
  return render_template("biomedical.html", output1 = output1, output2 = output2, output3 = output3 )

#Setting a route for the fifth step in the dereive
@app.route('/mobileapp')
def mobileapp():
  result = requests.get("https://devpost.com/hackathons?utf8=✓&search=mobile+app&challenge_type=all&sort_by=Recently+Added")
  src = result.content
  soup = BeautifulSoup(src, 'lxml')
  featured_events = soup.find_all('a',attrs={'data-role': 'featured_challenge'})
  
  for featured_challenge in featured_events:
      hackathons.append(featured_challenge.attrs['href'])
  
  output1 = hackathons[0]
  output2 = hackathons[1]
  output3 = hackathons[3]
  hackathons.clear()
  return render_template("mobileapp.html", output1 = output1, output2 = output2, output3 = output3 )


if __name__ == '__main__':
  app.run()
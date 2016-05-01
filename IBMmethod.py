import json
from watson_developer_cloud import ToneAnalyzerV3Beta

#module2 define as writing the IBM function


tone_analyzer = ToneAnalyzerV3Beta(
username='0e6e23c5-20c5-4c1e-bed5-f0b81751d3ef',
password='2F5BGfic6OHZ',
version='2016-02-11')
   


def parse_data(analysis_string):

  

  # get result from watson
  analysis_results = tone_analyzer.tone(text = analysis_string)

  #convert analysis result into string
  json_data_string = json.dumps(analysis_results, indent=2)

  # put the string into the parsed_data
  parsed_data = json.loads(json_data_string)
  print ("Data from blue mix is all being parsed in parsed_data")
  #return parsed_data

  #looping through all disgust data and adding to list/printing 

  
#def emotion_parser(parsed_data):
  tone_data = []
  tones = parsed_data['document_tone']['tone_categories'][0]['tones']
  print("Printing your mood")
  emotions = sorted(tones, key = lambda x: x['score'],reverse = True)
  maxEmotions = (emotions[0]['tone_id'])
  return maxEmotions




























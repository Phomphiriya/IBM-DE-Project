import glob
import pandas as pd
import xml.etree.ElementTree as ET 
from datetime import datetime

list_csv = glob.glob('*.csv')
# list_csv:['source1.csv','source3.csv','source3.csv']
list_json = glob.glob('*.json')
# list_json:['source1.json','source3.json','source3.json']

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe
# df = extract_from_csv('source1.csv')

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process,lines=True)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["name", "height", "weight"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for person in root:
        name = person.find("name").text
        height = float(person.find("height").text)
        weight = float(person.find("weight").text)
        dataframe = dataframe.append({"name":name, "height":height, "weight":weight}, ignore_index=True)
    return dataframe

def extract():
    # create an empty data frame to hold extracted data
    extracted_data = pd.DataFrame(columns=['name','height','weight'])

    #process all csv files
    for csvfile in glob.glob('*.csv'):
        # print(csvfile)
        extracted_data = extracted_data.append(extract_from_csv(csvfile),ignore_index=True)
    
        #process all json files
    for jsonfile in glob.glob('*.json'):
        extracted_data = extracted_data.append(extract_from_json(jsonfile),ignore_index=True)
    
    for xmlfile in glob.glob('*.xml'):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile),ignore_index=True)

    return extracted_data

df = extract()
print(df)


def transform(data):
    data['height'] = round(data.height * 0.0254,2)
    data['weight'] = round(data.weight * 0.4535,2)
    return data
print(transform(df))


def load(targetfile,data_to_load):
    data_to_load.to_csv(targetfile)
    # targetfile = 'transformed_data.csv'
    # load(targetfile.transformed_data)

load("transform_data.csv",df)
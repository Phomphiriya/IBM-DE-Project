import requests
import pandas as pd
import json

url = "https://api.apilayer.com/exchangerates_data/latest?base=EUR&apikey=Ng2AcGUI2jADufC3WrsyZAmyZnNHvUBN"
data = json.loads(requests.get(url).text)
# print(data)

dataframe = pd.DataFrame(columns=["Currency", "Rate"])
for k,v in data['rates'].items():
    dataframe = dataframe.append({"Currency": k, "Rate": v}, ignore_index=True)
print(dataframe)

# Drop unnecessary columns
dataframe.set_index("Currency", inplace=True, drop=True)
# Save the Dataframe
dataframe.to_csv("exchange_rates_1.csv")
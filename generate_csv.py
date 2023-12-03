import requests
import json
import pandas as pd


def import_csv():
    endpoint_url = "http://localhost:8080/integra/getresults?sort=date,desc&size=512"
    response = requests.get(endpoint_url)

    json_data = response.json()

    with open('./outfiles/data.json', 'w') as file:
        json.dump(json_data, file)

    df = pd.read_json("./outfiles/data.json")

    df.to_csv('./outfiles/integra_400.csv', mode='w', header=None, index=False)


    df_2 = pd.read_json("./outfiles/integra_400.json")

    df_2.to_csv('./outfiles/integra_400_python_ONLY.csv', mode='w', header=None, index=False)
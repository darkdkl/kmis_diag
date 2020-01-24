import xmltodict
import json

def get_documents(file):
    with open(file, encoding="utf-8") as f:
            xml = xmltodict.parse(f.read())
    json.dumps(xml)
    my_dict=json.loads(json.dumps(xml))
    client_info={}
    diagn_result = {}
    for items in my_dict['document']['item']:
        client_info[items['@name']]=list(items.values())[1]
    for result in my_dict['document']['results']['item']:    
        diagn_result[result['@name'] ]=result['text']
    client_info['results']=diagn_result
    return client_info

if __name__ == "__main__":
    print(get_documents('./Document.xml'))
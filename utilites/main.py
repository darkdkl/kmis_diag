import requests
from parse_xml import get_documents
from load_device import get_device
from decode import decode
import json


def get_norm_data(text):
    lst = text.split('.')
    y = lst[2][:4]
    m = lst[1]
    d = lst[0]
    return f'{y}-{m}-{d}'


def main(doc, file):

    templates = {
        "name": "user",
        "date": "2020-12-07",
        "device": {
            "device_id": 311,
            "name": "УЗД"
        },
        "description": "текст",
        "conclusion": "текст",
        "file": "",
        "file_md5": "",
        "results": [{
                "id": 1,
                "heart_rate": 80,
                "bp_syst": 122,
                "bp_diast": 80,
                "diagnostics": 1
        }, ]
    }

    doc = get_documents(doc)
    raw_data = {}

    for key in templates.keys():
        if key in doc.keys():
            raw_data[key] = doc[key]

    file_md5, file = decode('uzi.png')

    templates["device"]['device_id'] = get_device(
        raw_data['device'], './devices.json')
    templates["device"]["name"] = raw_data['device']
    templates['name'] = raw_data['name']
    templates['date'] = get_norm_data(raw_data['date'])
    templates['description'] = raw_data['description']
    templates['conclusion'] = raw_data['conclusion']
    templates['file'] = file
    templates['file_md5'] = file_md5
    templates['results'] = [raw_data['results'], {
        'bp_syst': '80', 'bp_diast': '130', 'heart_rate': '90'}]

    response = requests.post('http://localhost:8000/api/diag/', json=templates)

    if response.ok:
        with open('out_json.json', 'w') as file:
            json.dump(response.json(), file)
        print('успешно')
        print('в данном каталоге были созданы 3 файла :md5_in image.txt,image_in_base64code.txt и out_json.json',)


if __name__ == "__main__":
    main('./Document.xml', './devices.json')

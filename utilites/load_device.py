import json


def get_device(name,file):
    with open(file) as f:
        devices = json.load(f)

    for device in devices:
        if device['name'] == name and bool(device['available']) == True and bool(device['is_active']) == True:
            return device['id']


if __name__ == "__main__":
    print(get_device('Acusonic 2000','./devices.json'))

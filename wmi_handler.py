import json
import os
import platform
from datetime import datetime

import psutil
import base64
import cv2
import geocoder


class Monitor(object):

    def __init__(self):
        self.uuid_device = 'e85bb04c-3371-40d0-8fb0-83ee138982a2'

    @staticmethod
    def get_user():
        return psutil.users()

    @staticmethod
    def get_gps():
        result = dict()
        g = geocoder.ip('me')
        result['latlng'] = g.latlng
        result['city'] = g.city
        return result

    @staticmethod
    def get_data_network():
        net_connections = psutil.net_connections()
        return net_connections

    @staticmethod
    def get_cpu_usage():
        usage = list()
        for i in range(1):
            usage.append(psutil.cpu_percent(interval=1))
        return usage[0]

    @staticmethod
    def get_os_system():
        return platform.system()

    @staticmethod
    def get_ram_usage():
        return dict(psutil.virtual_memory()._asdict())

    @staticmethod
    def get_battery_level():
        return psutil.sensors_battery()

    @staticmethod
    def get_image_captured():
        data = dict()
        cap = cv2.VideoCapture(0)

        if not cap.isOpened():
            print("Error opening Cam")

        ret, frame = cap.read()
        if ret:
            string = base64.b64encode(cv2.imencode('.jpg', frame)[1]).decode()
            data['img'] = string
            with open('./0.json', 'w') as outfile:
                json.dump(data, outfile, ensure_ascii=False, indent=4)

        return json.dumps(data)

    def get_result_monitor(self):
        result = dict()
        result['cpu'] = self.get_cpu_usage()
        result['ram'] = self.get_ram_usage()
        result['battery'] = self.get_battery_level()
        result['user'] = self.get_user()
        result['so'] = self.get_os_system()
        result['connections'] = self.get_data_network()
        result['image'] = self.get_image_captured()
        result['datetime'] = str(datetime.now())
        result['uuid'] = self.uuid_device
        result['gpsinfo'] = self.get_gps()


        return result


if __name__ == '__main__':
    m = Monitor()
    r = m.get_result_monitor()
    print(r)
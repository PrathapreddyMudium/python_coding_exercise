import csv
import json
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

import pytz
from pytz import timezone
import json


def parsexml(x, y):
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    depart_tag = root.find('.//DEPART')
    return_tag = root.find('.//RETURN')
    initial_depart_date = depart_tag.text
    initial_return_date = return_tag.text
    modified_depart_date = datetime.strptime(initial_depart_date, '%Y%m%d')
    modified_return_date = datetime.strptime(initial_return_date, '%Y%m%d')
    modified_depart_date = modified_depart_date + timedelta(x)
    modified_return_date = modified_return_date + timedelta(y)
    print(modified_depart_date.strftime("%Y%m%d"))
    modified_depart_date = modified_depart_date.strftime("%Y%m%d")
    modified_return_date = modified_return_date.strftime("%Y%m%d")
    depart_tag.text = modified_depart_date
    return_tag.text = modified_return_date
    tree.write('test_payload1_modified.xml')


# parsexml(20, 25)


def parsejson(element):
    data = json.load(open("test_payload2.json"))
    parse_json_recursively(data, element)
    # Output the updated file with pretty JSON
    open("test_payload_modified.json", "w").write(json.dumps(data, indent=4, separators=(',', ': ')))


def parse_json_recursively(json_object, target_key):
    if type(json_object) is dict and json_object:
        for key in json_object:
            if key == target_key:
                del json_object[key]
                break
            parse_json_recursively(json_object[key], target_key)

    elif type(json_object) is list and json_object:
        for item in json_object:
            parse_json_recursively(item, target_key)

parsejson("text")
# parsejson("outParams")


def parselogfiles(filename):
    output_file = open("log_analysis.txt", "w")
    result_writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open(filename, "r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        write_flag = 0
        for line in csv_reader:
            if line_count == 0:
                line_count += 1
                print("label," + "responseCode," + "responseMessage," + "failureMessage," + "timeStamp")
                str1 = ""
                result_writer.writerow(["timeStamp", "label", "responseCode", "responseMessage", "failureMessage"])
            if line["responseCode"] != '200':
                time_stamp = int(line["timeStamp"])
                # print(time_stamp)
                date_obj = datetime.fromtimestamp(time_stamp/1e3)
                date_obj = date_obj.astimezone(pytz.timezone("US/Pacific"))
                date_format = '%Y-%m-%d %H:%M:%S %Z'
                date_obj = datetime.strftime(date_obj, date_format)
                # print(line["timeStamp"]+","+line["label"]+","+line["responseCode"]+","+line["responseMessage"]+","+line["failureMessage"])
                result_writer.writerow([date_obj, line["label"], line["responseCode"], line["responseMessage"], line["failureMessage"]])


# parselogfiles("Jmeter_log1.jtl")







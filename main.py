import json
import os

# Open, read  and write into json file


def solution(file):

    try:
        os.path.exists(file)

        with open(file, 'r') as f:

            try:
                data = json.load(f)

                for i in data:

                    # adding key and description keys
                    data1 = data[i]
                    data1['tag'] = 'dict'
                    data1['description'] = 'Dictionary'
                    # print(data)

                data = data['message']
                # print(json.dumps(data, indent=4, sort_keys=True))

                json_list = []
                output = {}
                count = 0
                for i, k in data.items():
                    count += 1

                    output['key_'+ str(count)] = {'type': str(type(k).__name__),
                                                  'tag': 'This is an ' + str(type(k).__name__),
                                                  'description': type(k),
                                                  "required": 'false'}

                print(output)
                return output
            except:
                message = "Not A JSON File"
                print(message)
                return message
    except:
        message = "File Does Not exists"
        print(message)
        return message


file = 'data/data_1'
solution(file)

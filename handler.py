import requests
import json

def post_endpoint(event, context):
    r = requests.get("https://reqres.in/api/users")
    r_dict = r.json()
    count = 0
    inp = event['body']
    num = int(inp)
    tim = 0
    s_name = {}
    list_of_names = []
while (count < num ):
        for i in num:
            try:
                fname = r_dict['data'][tim]['first_name']
                lname = r_dict['data'][tim]['last_name']
                fullname = fname+" "+lname
                s_name = {'fullname' : fullname}
                list_of_names.append(s_name)
                print(fullname)
                tim = tim +1
                count = count +1
    #print("**************")
    #print("completed")
            except:
                response = {
                    'statusCode' : 401,
                    'response' : 'Cant reach endpoint'
                }
        response = {
            'statusCode' : 200,
            'response': list_of_names
        }

        r_json = {
            'body' : json.dumps(response)
        }

        return r_json
import requests


r = requests.get("https://reqres.in/api/users")
r_dict = r.json()


#print(r_dict['data'][1]['first_name'])
#print(r.text)
count = 0
inp = input('type a number:  ')
num = int(inp)
tim = 0
while (count < num ):
    fname = r_dict['data'][tim]['first_name']
    lname = r_dict['data'][tim]['last_name']
    fullname = fname+" "+lname
    print(fullname)
    tim = tim +1
    count = count +1
print("**************")
print("completed")


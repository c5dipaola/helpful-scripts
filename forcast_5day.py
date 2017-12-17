import time
import json
import requests


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def apiResponse(apicall):
    """
    Used to create a JSON formatted object using "json.loads"

    Example:
    apicall_object = "'http://some.api.url/apicall'"
    apiResponse(apicall_object)

    :param apicall: Enter in the variable you used as for the API call
    :return: returns the JSON formatted object as "decoded"
    """
    response = apicall.text
    decoded = json.loads(response)
    return decoded


zip_input = raw_input("Please enter the 5 digit zip code:  ")

base_url = "http://api.openweathermap.org/data/2.5/"
type_5day_zip = "forecast?zip="
units_imp = "&units=imperial"
# NOTE - You need to sign up at https://openweathermaps.org and get your own API Key
api_key = "&appid=<YOUR OPENWEATHERMAPS API KEY GOES HERE>"

api_call = requests.get(base_url + type_5day_zip + zip_input + units_imp + api_key)

city = apiResponse(api_call)['city']['name']

print("#" * 75)
print("")
print("You've entered the zip code {}.".format(zip_input))
print("Here is your 5 day forecast for the city of {}.".format(city))
print("")
print("#" * 75)

dint = 0
x = 0
counts = len(apiResponse(api_call)['list']) - 1
while dint <= counts:
    day = time.strftime('%w', (time.localtime(apiResponse(api_call)['list'][dint]['dt'])))
    date = time.strftime('%A, %B %d, %Y', (time.localtime(apiResponse(api_call)['list'][dint]['dt'])))
    now_temp = apiResponse(api_call)['list'][dint]['main']['temp']
    conditions = apiResponse(api_call)['list'][dint]['weather'][0]['description']
    time_now = time.strftime('%H:%M', (time.localtime(apiResponse(api_call)['list'][dint]['dt'])))
    if day == "0":
        if x != 0:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 0
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "1":
        if x != 1:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 1
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "2":
        if x != 2:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 2
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "3":
        if x != 3:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 3
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "4":
        if x != 4:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 4
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "5":
        if x != 5:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 5
        else:
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
    if day == "6":
        if x != 6:
            print("")
            raw_input("Press enter to continue...")
            print("")
            print("=" * 75)
            print("")
            print("======  The weather for {} will be  ======".format(date))
            print("")
            print(" " * 4 + "The weather at {} will be:".format(time_now))
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1
            x = 6
        else:
            print("")
            print(" " * 8 + "Expected Temperature is {}".format(now_temp))
            print(" " * 8 + "Expect {}".format(conditions))
            print("")
            dint += 1

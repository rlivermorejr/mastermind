# for api calls
import requests


def getNumbers(param):
    # gets the numbers from the api
    # param 1 is for initializing numbers variable
    # 2, 3, and 4 are easy, medium, and hard respectively
    if param == 1:
        pass
    if param == 2:
        params = requests.get(
            "https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num
    if param == 3:
        params = requests.get(
            "https://www.random.org/integers/?num=6&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num
    if param == 4:
        params = requests.get(
            "https://www.random.org/integers/?num=8&min=0&max=7&col=1&base=10&format=plain&rnd=new")
        num = params.text.split()
        return num

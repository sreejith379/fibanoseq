import timeit
from rest_framework.decorators import api_view
import json
from rest_framework.response import Response

def calculation(num):
    if num <= 0:
        return Response(content)
    elif num == 1:
        return 1
    else:
        num1 = 1
        num2 = 1
        for i in range(2, num):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2


@api_view(["POST"])
def fibanocci(num):
    start_time = timeit.timeit()
    content = "Enter an integer value greater than zero"
    try:
        val = json.loads(num.body)
        result = calculation(val)
    except:

        return Response(content)
    else:
        end_time = timeit.timeit()
        time_taken = start_time - end_time
        return Response({'Fibanocci sequence number': result, 'Time taken': time_taken})

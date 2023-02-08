from django.http import JsonResponse
import json

def api_home(request , *args , **kwargs):
    
    #request -> HttpRequest -> Django
    
    #request.body
    print(request.GET) #url query param
    print (request.POST) 
    body = request.body  #byte string JSON data
    data = {}
    try:
        data = json.loads(body) #string of JSON data -> python dict
    except:
        pass
    
    print (data)
    # data['headers'] = request.headers  #request.META -> 
    # print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)


    
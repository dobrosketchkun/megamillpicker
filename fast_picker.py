from http.client import HTTPSConnection                                        
from json import dumps, loads                                                  

#Оригинал - https://teletype.in/@snakeblog/rJnA9jwEX , модификации - мои
#Больше о формате запроса                                                        
#https://api.random.org/json-rpc/1/introduction                                  

API_TOKEN = ''  # Ваш токен                                                  
LINES = 1 # Number of lottery lines
LOTTERY = 'PowerBall'


def random_int(min, max, n=2):
    request_data = {  # Тело запроса                                                
      'jsonrpc': '2.0',                                                            
      'method': 'generateIntegers',                                                
      'params': {                                                                  
        'apiKey': API_TOKEN,                                                        
        'min': min,  # Нижняя граница рандома                                        
        'max': max,  # Верхняя граница                                              
        'n': n,  # Количество запрашиваемых чисел                                  
      },                                                                            
      'id': 1,                                                                      
    }                                                                              
    encoded_data = dumps(request_data)                                              
                                                                                   
    headers = {                                                                    
      'Content-Type': 'application/json-rpc',  # Тип запроса                        
    }                                                                              
    encoded_headers = dumps(headers)                                                
                                                                                   
    connection = HTTPSConnection('api.random.org')                                  
    connection.request('GET', '/json-rpc/1/invoke', encoded_data, headers)          
    response = connection.getresponse()                                            
    response_data = loads(response.read().decode())                                
    return response_data['result']['random']['data']

def line_maker(lottery):
    if lottery == 'PowerBall':
        big = 69
        small = 26
    elif lottery == 'Mega':
        big = 70
        small = 25
    elif lottery == 'test':
        big = 10
        small = 10
    else:
        print('Only PowerBall or Mega are supported!')
    rand_list = random_int(1, big, n=50)
    seted_rand_list = []
    for _ in rand_list:
        if _ not in seted_rand_list:
            seted_rand_list.append(_)
    a, b, c, d, e = seted_rand_list[0:5]
    f = random_int(1, small, n=1)[0]
    print(f" Your numbers are {a}, {b}, {c}, {d}, {e} and {f}")


for _ in range(LINES):
    print('#' + str(_), end='')
    line_maker(LOTTERY)

#middleware 1

class Middleware1:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware1 pre-procesamiento")
        response = self.get_response(request) #llama al siguiente midleware o a la vista
        print("Middleware1 post-procesamiento")
        return response 
    
#middleware 2

class Middleware2:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Middleware2 pre-procesamiento")
        response = self.get_response(request) #llama al siguiente midleware o a la vista
        print("Middleware2 post-procesamiento")
        return response 
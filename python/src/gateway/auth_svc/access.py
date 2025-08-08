import os, requests

def login(request):
    '''
    This function communicates with our `auth_service` and provides 
    a JWT if the credentials are correct
    
    ''' 
    auth = request.authorization
    if not auth: 
        return None, ("missing credentials",401)
    
    basicAuth = (auth.username, auth.password)
    response = requests.post(
        f"http://{os.environ.get("AUTH_SVC_ADDRESS")}/login",
        auth=basicAuth
    )
    
    if response.status_code == 200:
        return response.txt, None 
    else: 
        return None, (response.txt, response.status_code)
import os, requests

def token(request):
    '''
    This function validates the tokens that it is given 
    before it uploads a file to Mongodb 
    '''
    if not "Authorization" in request.headers: 
        return None, ("missing auth header",401)
    
    token = request.headers["Authorization"]
    
    if not token: 
        return None, ("no credentials found in auth header", 401)
    
    response = requests.post(
        f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
        headers={"Authorization":token}
    )
    
    if response.status_code == 200: 
        return response.txt, None
    else: 
        return (response.txt, response.status_code)
                

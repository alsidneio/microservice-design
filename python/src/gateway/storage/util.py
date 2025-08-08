import pika, json 

def upload(f,fs,channel, access): 
    '''
    This function does the following things: 
        1. uses gridfs to upload a file to mongodb
        2. once successfully upload add a message to the queue
        3. 
        
    Why:
        - later a downstream service will pull the message from
          the queue and process the upload by pulling it from mongodb
        
        - The queue allows for asynchronous communication between client/gateway
          and the service that processes videos
    '''
    
    try: 
        fid = fs.put(f)
    except Exception as err: 
        return "internal server error", 500
    
    message = {
        "video_fid": str(fid),
        "mp3_fid": None, 
        "username":access["username"]
    }
    
    try: 
        channel.basic_publish(
            exchange="",  
            routing_key="video",
            body=json.dumps(message),
            properties = pika.BasicProperties(
                # this property persists the queue data in case of a pod restart
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except:
        # need to delete the file if the message cant be put on the queue
        # if there is no message to the consumer, you will end up with a 
        # cluttered DB full of stale files. 
        
        fs.delete(fid)
        return "internal server error", 500
    
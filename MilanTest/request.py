import hub,utime, ujson



class request:
    def __init__(self):
        self.ser = hub.USB_VCP()
        self.mbegin=b'msg_start\n'
        self.mend=b'\nmsg_end\n'
        self.rbegin = b'reply_start '
        self.rend = b' reply_end'
    
    def comm(self,payload):
        s =  b' '
        self.ser.write(self.mbegin + payload + self.mend)
        utime.sleep(0.01)
        while not(rend in s):
            try:
                s = s + self.ser.readline()
                # print(s)   
            except:
                utime.sleep(0.1)
        start = len(self.rbegin)+s.find(self.rbegin)
        end = s.find(self.rend)
        reply = s[start:end]
        
        return reply.decode()
    def put(self, headers, url, data):
        request= {"method": "put","headers": ujson.dumps(headers) ,"url": url,"data": ujson.dumps(data) }
        reply=comm(ujson.dumps(request))
        utime.sleep(01)
        return(reply)        
    def post(self, headers, url, data):
        request= {"method": "post","headers": ujson.dumps(headers) ,"url": url,"data": ujson.dumps(data) }
        reply=comm(ujson.dumps(request))
        utime.sleep(01)
        return(reply)  
        
    def get(self, headers , url):
        request= {"method": "get","headers": ujson.dumps(headers) ,"url": url}
        reply=comm(ujson.dumps(request))
        utime.sleep(01)
        return(reply)
        

test=request()
SL_Appkey= "bvd8X9LweQY9o2eP1NYL-p8mLL9wMAk6YYOnYSiIo0" 
Headers={"Accept":"application/json","x-ni-api-key": SL_Appkey }
Url="https://api.systemlinkcloud.com/nitag/v2/tags/test1/values/current"
    
Data={"value":{"type":"STRING","value":"lol"}}
# reply= test.put(headers= Headers , url = Url, data= Data )


reply1=test.get(headers=Headers, url=Url) 
    
    
print(reply1)




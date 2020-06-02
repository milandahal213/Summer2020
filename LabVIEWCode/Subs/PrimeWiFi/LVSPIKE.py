import hub,utime
f = hub.USB_VCP()
import ujson
reol = b'return'
def get(headers,b_string):
    s =  b''
    print(type(s))
    f.write("method"+":get" + "headers:"+headers  + "url:"+str(b_string) + ":" +"end" )
    while not(reol in s):
        try:
            s = s+ f.readline()
        except:
            utime.sleep(0.1)    

def put(headers,b_string,payload):
    s =  b''
    print(type(s))
    f.write("method"+":put" + "headers:"+headers  + "url:"+str(b_string) + "payload:" + payload + ":" +"end" )
    while not(reol in s):
        try:
            s = s+ f.readline()
        except:
            utime.sleep(0.1)    


Key ="h9xKSrP8EwsCncyq8NvjAo-0Ft1yIlsrokF7ecytSH" 
def SL_setup():
    urlBase = "https://api.systemlinkcloud.com/nitag/v2/tags/"
    headers = "Accept:application/json;x-ni-api-key:"+Key +";"
    return urlBase, headers

def Put_SL(Tag, Type, Value):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current" 
    propValue = {"value":{"type": Type ,"value": Value }}
    try:
        put(headers,urlValue,ujson.dumps(propValue))
        result="success"
    except Exception as e:
        print(e)
        result = 'failed'
    return result

def Get_SL(Tag):
    urlBase, headers = SL_setup()
    urlValue = urlBase + Tag + "/values/current"
    try:
        value =get(headers,urlValue)
        result="a"
    except Exception as e:
        print(e)
        result = 'failed'
    return result

Put_SL("test", "STRING" ,"strange that it worked")



print("how is this running" )

print("this should be running too")

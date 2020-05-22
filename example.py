# DRC this is a small application that will consume the SecureData RESTful web services
# -------------------------------------------------------------------------------- 
# -------------------------------------------------------------------------------- 
# curl -v -k -X POST https://voltage-pp-0000.dataprotection.voltage.com/vibesimple/rest/v1/protect 
#-H'Content-Type:application/json' 
#-H'Authorization:VSAuth vsauth_method="sharedSecret",vsauth_data="dm9sdGFnZTEyMw==",vsauth_identity_ascii="securityops@makemytrip.com",vsauth_version="200"' -d '{"format":"CC", "data":["1111-2222-3333-4444","4444-3333-2222-1111", "38520000023237"]}'

#VSAuth vsauth_method="sharedSecret",vsauth_data="dm9sdGFnZTEyMw==",vsauth_identity_ascii="test@test.com",vsauth_version="200"


import requests
from zipfile import ZipFile

print("Goodbye, World!")

url = "https://voltage-pp-0000.dataprotection.voltage.com/vibesimple/rest/v1/protect"
value = ""

#payload = ['format':'AUTO', 'data':{1111-2222-3333-4444}]
#payload = {'format':'AUTO', 'data':'[1111-2222-3333-4444]'}
payload = '{ "format" : "AUTO", "data" : ["Daniel","Clift","some text goes here"]}'
#payload = {}

headers = {'Content-Type':'application/json','Authorization':'VSAuth vsauth_method="sharedSecret",vsauth_data="dm9sdGFnZTEyMw==",vsauth_identity_ascii="test@test.com",vsauth_version="200"'}
r = requests.post(url, headers=headers, data=payload)

print (r.content)
print (r.status_code)

# deploy PAPI components
# call PAPI

# zips test
# with ZipFile("trustStore.zip", "r") as zipObj:
with ZipFile("/home/dan/python_rest_papi_local/trustStore.zip", "r") as zipObj:
# Extract all the contents of zip file in different directory
    # printing all the contents of the zip file 
    #zip.printdir() 
    zipObj.extractall("/tmp")
    print('done')

# %%
import requests 
progress1 = requests.get('https://api.worldquantbrain.com/simulations/9NN21z3')
progress2 = requests.get('https://api.worldquantbrain.com/alphas/7QawWMO/recordsets')
cookies1 = {'t': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJSWlp2WEFtMktyNUZaMzBvek11UFBPOFVieTJzRlB0cyIsImV4cCI6MTY2MTg3MzQ2N30.BWctEtkJycq6U6PD-V2EEWctSLXyiHdikWVmYahK2EE'}
r = requests.get('https://api.worldquantbrain.com/alphas/Okbp2kp', cookies = cookies1)
print(r.status_code)
cookies2 = {'t', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJSWlp2WEFtMktyNUZaMzBvek11UFBPOFVieTJzRlB0cyIsImV4cCI6MTY2MTg3MzQ2N30.BWctEtkJycq6U6PD-V2EEWctSLXyiHdikWVmYahK2EE'}
e = requests.get('https://api.worldquantbrain.com/simulations/yDD5PQq', cookies = cookies2)
print(e.status_code)
#print(progress1)
#print(progress1.status_code)
#print(progress2.status_code)
# %%

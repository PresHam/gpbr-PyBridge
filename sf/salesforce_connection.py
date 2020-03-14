from salesforce_api import Salesforce

'''
    Estabelece conexão de acordo com as informações de:
    login, senha e token fornecidas pelo usuário na interface.     
'''


def login_salesforce(username, password, security_token, sandbox):
    client = Salesforce(username=username,
                        password=password,
                        security_token=security_token,
                        is_sandbox=sandbox)
    print('Login Attempt')
    return client

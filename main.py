import pandas as pd
import dns
import ipaddress
# import scrapp

# scrapp.lista_universidades

####################### HARDCODED LIST OF UNIS ###############################
dic = {'Universidades': ['IFAC', 'UFAC', 'UFAL', 'UNIFAP'],
        'Sites': ["https://portal.ifac.edu.br/", "http://www.ufac.br/", "http://www.ufal.br/", "http://www.unifap.br/"]
    }

df = pd.DataFrame.from_dict(dic, 'columns')
df.to_csv("./uni_sites.csv")
###########################################################################

def check_public_cloud(ip):
    # IP ranges for public cloud providers
    cloud_ranges = [
        {'provider': 'AWS', 'cidr': '3.0.0.0/8'},
        {'provider': 'Azure', 'cidr': '13.64.0.0/11'},
        {'provider': 'GCP', 'cidr': '35.184.0.0/13'},
        {'provider': 'IBM Cloud', 'cidr': '162.247.0.0/16'},
        {'provider': 'OCI', 'cidr': '132.145.0.0/16'}
    ]

    for cloud_range in cloud_ranges:
        network = ipaddress.ip_network(cloud_range['cidr'])
        if ipaddress.ip_address(ip) in network:
            return cloud_range['provider']
        
    return 'Private Cloud'

def perform_dns_scan(domain):
    try:
        ips = dns.resolver.resolve(domain)
        for ip in ips:
            provider = check_public_cloud(ip)
        if provider:
            print(f"The domain {domain} is hosted on {provider}.")
        else:
            print(f"The domain {domain} is not hosted on a public cloud.")
        return provider
    except:
        print(f"DNS resolution failed for domain {domain}.")
        return "FAILED"

df_retorno = pd.DataFrame([], columns=["Universidade", "Provedor"])

df = pd.read_csv("./uni_sites.csv")
lista_universidades = df.values.tolist()

for id, uni, site in lista_universidades:
    prov = perform_dns_scan(site)
    new_row = {"Universidade":uni, "Provedor":prov}
    df_retorno.loc[len(df_retorno)] = new_row

print(df_retorno.head())
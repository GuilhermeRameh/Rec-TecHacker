import pandas as pd
import whois
# import scrapp

# scrapp.lista_universidades

####################### HARDCODED LIST OF UNIS ###############################
dic = {'Universidades': 
       ['IFAC',
        'UFAC',
        'UNEAL',
        'IFAL',
        'UFAL',
        'UEAP',
        'IFAP',
        'UNIFAP',
        'UEA',
        'IFAM', 
        'UFAM'
        'INPA',
        'UECE',
        'URCA',
        'UVA',
        'IFCE',
        'UFC',
        'UNILAB',
        'UFCA',
        'ESCS',
        'IFB',
        'UnB',
        'ENAP',
        'FACELI',
        'IFES',
        'UniRV',
        'UEG',
        'IFG',
        'UFG',
        'IF Goiano',
        'UEMA',
        'UEMASUL',
        'IEMA',
        'IFMA',
        'UFMA',
        'UNEMAT',
        'IFMT',
        'UFMT',
        'UFR',
        'UEMS',
        'UFGD',
        'IFMS',
        'UFMS',
        'UEMG',
        'USP',
        'UNICAMP',
        'UNESP',
        'UNIVESP'
        ],

        'Sites': 
        ["https://portal.ifac.edu.br/",
         'http://www.ufac.br/',
         'http://www.uneal.edu.br/',
         'http://www.ifal.edu.br/',
         'https://ufal.br/',
         'https://www.ueap.edu.br/',
         'http://www.ifap.edu.br/',
         'http://www.unifap.br/',
         'https://www2.uea.edu.br/',
         'http://www2.ifam.edu.br/',
         'https://ufam.edu.br/',
         'https://www.gov.br/inpa/pt-br/',
         'http://www.uece.br/',
         'http://www.urca.br/', 
         'http://ifce.edu.br/',
         'http://www.ufc.br/',
         'http://www.unilab.edu.br/',
         'http://www.ufca.edu.br/',
         'https://www.escs.edu.br/',
         'http://www.ifb.edu.br/', 
         'https://unb.br/', 
         'https://www.enap.gov.br/', 
         'https://faceli.edu.br',
         'https://www.ifes.edu.br/',
         'http://www.unirv.edu.br/',
         'http://www.ueg.br/',
         'http://www.ifg.edu.br/',
         'http://www.ufg.br/',
         'http://www.ifgoiano.edu.br/',
         'http://www.uema.br/',
         'http://www.uemasul.edu.br/',
         'http://www.iema.ma.gov.br/',
         'http://www.ifma.edu.br/',
         'http://www.ufma.br/',
         'http://portal.unemat.br/',
         'http://www.ifmt.edu.br/',
         'http://www.ufmt.br/',
         'http://ufr.edu.br/',
         'http://www.uems.br/',
         'http://www.ufgd.edu.br/',
         'http://ifms.edu.br/',
         'http://www.ufms.br/',
         'http://www.uemg.br/',
         'https://www5.usp.br/',
         'http://www.unicamp.br/',
         'http://www.unesp.br/',
         'https://univesp.br/'
        ]
    }

df = pd.DataFrame.from_dict(dic, 'columns')
df.to_csv("./uni_sites.csv")
###########################################################################

def check_cloud_provider(server_name):
    if 'amazonaws' in server_name:
        return 'AWS'
    elif 'azure' in server_name:
        return 'Azure'
    elif 'google' in server_name:
        return 'Google Cloud'
    else:
        return 'Private Cloud'

def check_public_cloud(site):
    w = whois.whois(site)
    result = []
    if w:
        for server in w.name_server:
            prov = check_cloud_provider(server)
            if prov not in result:
                result.append(prov)  
        return result
    return 'FAILED'



df_retorno = pd.DataFrame([], columns=["Universidade", "Provedor"])

df = pd.read_csv("./uni_sites.csv")
lista_universidades = df.values.tolist()

for id, uni, site in lista_universidades:
    if site is not None:
        prov = check_public_cloud(site)
        new_row = {"Universidade":uni, "Provedor":prov}
        df_retorno.loc[len(df_retorno)] = new_row

print(df_retorno)
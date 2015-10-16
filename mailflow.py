#!/usr/bin/python
#-=- encoding: utf-8 -=-


# variaveis
from enviamail import enviamail 
from checkmail import checkmail
from limpamail import limpamail
from acesso import acesso
import time
import sys

def mailflow():
    limpamail(sys.argv[2],sys.argv[3])

    # executa o mailflow.
    envia=enviamail("mailflow@%s" %sys.argv[1])
    time.sleep(10)
    valida=checkmail(sys.argv[2],sys.argv[3])
	
while (str(valida) == "Erro-3"):
    	time.sleep(5)
	valida=checkmail(sys.argv[2],sys.argv[3])

    # compara o tempo de entrega.
    if (str(valida) < '0:01:30'):
    	arq = open('%s.log' %sys.argv[1] , 'w')
       	arq.write("%s - OK" %valida)
        return valida
    elif (str(valida) < '0:04:00'):
       	arq = open('%s.log' %sys.argv[1] , 'w')
        arq.write("%s - MEDIA" %valida)
        return valida
    else:
        arq = open('%s.log' %sys.argv[1] , 'w')
        arq.write("%s - ALTA" %valida)
        return valida

    
print mailflow()




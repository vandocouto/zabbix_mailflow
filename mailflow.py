#!/usr/bin/python
#-=- encoding: utf-8 -=-

from enviamail import enviamail 
from checkmail import checkmail
import time
import sys

def mailflow():
    
    # executando o mailflow
    try:
	envia=enviamail("mailflow@%s" %sys.argv[1])
        time.sleep(10)
        valida=checkmail()

	while (str(valida) == "Erro-3"):
           time.sleep(5)
	   valida=checkmail()

	# acima de 2 minutos
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
    except:
	arq = open('%s.log' %sys.argv[1] , 'w')
        arq.write("%s - DESASTRE" %valida)
        return valida
    
print mailflow()




#!/usr/bin/python
#-=- encoding: utf-8 -=-

from enviamail import enviamail 
from checkmail import checkmail
import time
import sys

def mailflow():
    
    # executando o mailflow
    try:
        # até 2 minutos
        envia=enviamail("mailflow@%s" %sys.argv[1])
        time.sleep(115)
        valida=checkmail()
        # até 12 minnutos
        if (str(valida) == "Erro-3"):
            time.sleep(475)
            valida=checkmail()
	    if (str(valida) < '0:04:00'):
            	arq = open('%s.log' %sys.argv[1] , 'w')
            	arq.write("%s - ATENCAO" %valida)
            	return valida
	    else: 
            	arq = open('%s.log' %sys.argv[1] , 'w')
            	arq.write("%s - MEDIA" %valida)
            	return valida
        else:
	    arq = open('%s.log' %sys.argv[1] , 'w')
            arq.write("%s - OK" %valida)
            return valida
    except:
	arq = open('%s.log' %sys.argv[1] , 'w')
        arq.write("%s - DESASTRE" %valida)
        return valida
    
        

print mailflow()




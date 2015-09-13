#!/usr/bin/python
#-=- encoding: utf-8 -=-


def limpamail():
    
    # bibliotecas
    import imaplib
    from datetime import datetime
    from acesso import acesso
    
    # formato do horario 
    FMT = '%H:%M:%S'
    try:
       # imap
        mail = imaplib.IMAP4_SSL(acesso()[0])
        mail.login(acesso()[1],acesso()[2])
        mail.list()
        mail.select("inbox")
    except:
        return "Erro-2"

    # recebendo os dados do  último email
    resultado, dado = mail.search(None, "ALL")
    try:
    	ids = dado[0].split()
    	latest_email_id = ids[-1]
    	# apagando o útlimo email
    	mail.store(latest_email_id,'+FLAGS','\\Deleted')
    	mail.expunge()
    except:
	return 1

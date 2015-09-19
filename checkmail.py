#!/usr/bin/python
#-=- encoding: utf-8 -=-


def checkmail(imap,login):
    
    # bibliotecas.
    import imaplib
    from datetime import datetime
    from acesso import acesso
    
    # formato do horario. 
    FMT = '%H:%M:%S'
    try:
        # conexão imap.
        mail = imaplib.IMAP4_SSL(imap)
        mail.login(login,acesso()[2])
        mail.list()
        mail.select("inbox") 
    except:
        return "Erro-2"

    try:
        # recebendo os dados do  último email.
        resultado, dado = mail.search(None, "ALL")
        ids = dado[0].split()
        latest_email_id = ids[-1]

        # recebendo o Hearder.
        resultado, dado = mail.fetch(latest_email_id, '(BODY.PEEK[HEADER.FIELDS (SUBJECT)] UID)')
        hheader=str(dado[0][1])[9:-4]
    
        # horario atual.
        hatual=str(datetime.now())[11:19]

        # subtraindo os horarios.
        tdelta = datetime.strptime(hatual, FMT) - datetime.strptime(hheader, FMT)
        
        # apagando o e-mail.
        mail.store(latest_email_id,'+FLAGS','\\Deleted')
        mail.expunge()
        
        # retornando resultado.
        return tdelta
    except:
	# erro-3.
        return "Erro-3"



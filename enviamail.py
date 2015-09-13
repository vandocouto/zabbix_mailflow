#!/usr/bin/python
#-=- encoding: utf-8 -=-

# 
def enviamail(mailflow):
    
    # bibliotecas
    import os
    import commands
    import time
    from datetime import datetime
    import smtplib
    from email.MIMEText import MIMEText
    from acesso import acesso
    
    # variaveis
    SMTP    =   acesso()[3]
    PORTA   =   acesso()[4]
    LOGIN   =   acesso()[5]
    EMAIL   =   acesso()[6]
    PASS    =   acesso()[7]
    FMT     =   '%H:%M:%S'

    # checando a porta de conexão
    if (int(PORTA) == 465):
        SMTPSERVER = smtplib.SMTP_SSL
    else:
        SMTPSERVER = smtplib.SMTP

    # enviando o email mailflow
    try:
        SMTPSERVER
        PORTA = str(PORTA)

	# aqui no assunto e mensagem irá o horário
        ASSUNTO="%s" %(str(datetime.now())[11:19])
        MENSAGEM=(str(datetime.now())[11:19])
        FROM=EMAIL

        # destinatário
        TO=mailflow

        serv=SMTPSERVER()
        serv.connect(SMTP,PORTA)
        serv.login(LOGIN,PASS)
        msg1 = MIMEText("%s"% MENSAGEM,"html")
        msg1['Subject']=(ASSUNTO)
        msg1['From']=FROM
        msg1['To']=TO
        msg1['Content-type']="text/html"
        serv.sendmail(FROM,TO, msg1.as_string())
        serv.quit()
        return ASSUNTO
    except:
        return "Erro-1"



                                                  

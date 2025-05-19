import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

def enviar_email(url, email):
     try:
          conteudo_email = "<div style='text-align:center;'><h3>Blog</h3><p>Clique no link para validar seu email: "+str(url)+"</p></div>"

          msg = EmailMessage()
          msg.set_content(conteudo_email, subtype='html')
          msg['Subject'] = 'Verificação de email'
          msg['From'] = os.environ.get('MY_EMAIL')
          msg['To'] = email
          password = os.environ.get('MY_EMAIL_PASS')

          with smtplib.SMTP(os.environ.get('MY_SMTP_GMAIL_SOCKET')) as smtp:
               smtp.starttls()
               smtp.login(msg['From'], password)
               smtp.send_message(msg)

     except:
          print("Tentativa de envio de email falhou!")
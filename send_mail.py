# Lê uma lista de emails e envia uma mensagem de notificação. 
# Simula o envio de e-mails imprimindo uma mensagem para cada email.
# A mensagem é a mesma pra todos, só o destinatario muda.

emails = [
    'e1@gmail.com',
    'e2@gmail.com',
    'e3@gmail.com',
    'e4@gmail.com',
    'e5@gmail.com'
]

msg = "Este é um e-mail de notificação."

def send_notification(emails, msg):
    for email in emails:
        print(f'Enviando e-mail para {email}: {msg}')

send_notification(emails, msg)

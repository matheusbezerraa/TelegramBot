import telebot

CHAVE_API = "6098583627:AAEcgMBeahLeBhTZojFIKTBbxnAMawYbqN8"

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    bot.send_message(mensagem.chat.id,"link do meu Linkedin: http://www.linkedin.com/profile/edit?trk=hb_tab_pro_top")
    

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    bot.send_message(mensagem.chat.id,"link do meu GitHub: https://github.com/matheusbezerraa")

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.send_message(mensagem.chat.id,"link do meu Currículo: https://drive.google.com/file/d/191s24R-aVWfkCnG8tn5GmO3JLZPiaAS0/view?usp=sharing")

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """Escolha uma opção para continuar(clique no item):
    /opcao1 Ver o Linkedin
    /opcao2 Ver o GitHub
    /opcao3 Ver o Currículo
Responder qualquer outra coisa não vai funcionar, clique em uma das opções."""
    bot.reply_to(mensagem, texto)

bot.polling()
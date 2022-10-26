

import sys
import irc.bot
import requests
import json

print("Teste")

file = open("variavelrip.json", "r")
rip = json.loads(file.read())

file = open("variavelpuff.json", "r")
puff = json.loads(file.read())

file = open("variavelpinou.json", "r") 
pinou = json.loads(file.read())

file = open("variaveldripou.json", "r") 
dripou = json.loads(file.read())

file = open("variavelagua.json", "r") 
agua = json.loads(file.read())

file = open("variavelju.json", "r")
ju = json.loads(file.read())

file = open("variavelmurillo.json", "r") 
murillo = json.loads(file.read())

file = open("variavelcolucci.json", "r")
colucci = json.loads(file.read())

file = open("variavelserge.json", "r")
serge = json.loads(file.read())

file = open("variaveltsu.json", "r") 
tsu = json.loads(file.read())

file = open("variavelarroto.json", "r") 
arroto = json.loads(file.read())

file = open("variaveljulio.json", "r")
julio = json.loads(file.read())

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel

        # CHANNEL ID para chamar as API'S

        url = 'https://api.twitch.tv/kraken/users?login=' + channel
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

# Conexao com o chat

        server = 'irc.chat.twitch.tv'
        port = 6667
        print ('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:'+token)], username, username)
        
    def on_welcome(self, c, e):
        print ('Joining ' + self.channel)

    # Requisicao de capacidades

        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):

# Se a mensagem comecar com "!", tentar rodar como um comando

        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            print ('Received command: ' + cmd)
            comando = cmd.upper()
            self.do_command(e, comando)
        return

# Criar comandos

    def do_command(self, e, cmd):
        c = self.connection

        # Achar a API do jogo atual
        if cmd == "JOGO":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, r['display_name'] + ' esta jogando ' + r['game'])

        # Achar a API do titulo atual

        elif cmd == "TITULO":
            url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
            headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
            r = requests.get(url, headers=headers).json()
            c.privmsg(self.channel, r['display_name'] + ' esta transmitindo: ' + r['status'])

    # Comandos somente frase

        elif cmd == "DISNEY":
            message = "Alguem avisa pro Matt que ele ta na disney!!!"
            c.privmsg(self.channel, message)

    # Comandos de contador

        elif cmd == "RIP":
            global rip
            rip += 1
            message = 'Matt caiu fedendo pela ' + str(rip) + ' vez!!!'
           
            c.privmsg(self.channel, message)
            file = open("variavelrip.json", "w")
            file.write(str(rip))

        elif cmd == "ARROTO":
            global arroto
            arroto += 1
            message = 'O Murillo arrotou pela ' + str(arroto) + ' vez e o Math precisou pedir pra ele parar de novo!'

            c.privmsg(self.channel, message)
            file = open("variavelarroto.json", "w") 
            file.write(str(rip))
       
        elif cmd == "PUFF":
            global puff
            puff += 1
            message = 'Matt vaporou pela ' + str(puff) + ' vez!!!'
            
            c.privmsg(self.channel, message)
            file = open("variavelpuff.json", "w")
            file.write(str(puff))
            
        elif cmd == "PINOU":
            pinou += 1
            message = 'Matt acertou tudo menos o inimigo pela ' + str(pinou) + ' vez!'

            c.privmsg(self.channel, message)
            file = open("variavelpinou.json", "w") 
            file.write(str(pinou))

        elif cmd == "DRIPOU":
            dripou += 1
            message = 'Matt reabasteceu o monstro pela ' + str(dripou) + ' vez!'

            c.privmsg(self.channel, message) 
            file = open("variaveldripou.json", "w") 
            file.write(str(dripou))
            
        elif cmd == "AGUA":
            agua += 1
            message = 'Matt bebeu agua pela ' + str(agua) + ' vez!'

            c.privmsg(self.channel, message)
            file = open("variavelagua.json", "w") 
            file.write(str(agua))
            
        elif cmd == "MURILLO":
            murillo += 1
            message = 'Murillo quase causou meu ban pela ' + str(murillo) + ' vez!'

            c.privmsg(self.channel, message)
            file = open("variavelmurillo.json", "w")
            file.write(str(murillo))
            
        elif cmd == "COLUCCI":
            colucci += 1
            message = 'O Colucci foi pra outra dimensao pela ' + str(colucci) + ' vez!'

            c.privmsg(self.channel, message)
            file = open("variavelcolucci.json", "w") 
            file.write(str(colucci))

        elif cmd == "SERGE":
            serge += 1
            message = 'Serge roubou o loot pela ' + str(serge) + ' vez!'

            c.privmsg(self.channel, message)
            file = open("variavelserge.json", "w")
            file.write(str(serge))

        elif cmd == "TSU":
            tsu += 1
            message = 'O Tsu nao entendeu nada que a gente falou pela ' + str(tsu) + ' vez!!!'

            c.privmsg(self.channel, message)
            file = open("variaveltsu.json", "w") 
            file.write(str(tsu))
 
        elif cmd == "JULIO":
            julio += 1
            message = 'O Julio falou na hora errada pela ' + str(julio) + ' vez!!!'

            c.privmsg(self.channel, message)
            file = open("variaveljulio.json", "w")
            file.write(str(julio))
        
    # Comandos extras

        elif cmd == "SALVE":
            message = "HeyGuys"
            c.privmsg(self.channel, message)

    # Fim TansinhoBot

    def main():
        if len(sys.argv) != 5:
            print("Usage: twitchbot <username> <client id> <token> <channel>")
            sys.exit(1)

            username  = sys.argv[1]
            client_id = sys.argv[2]
            token     = sys.argv[3]
            channel   = sys.argv[4]

            bot = TwitchBot(username, client_id, token, channel)
            bot.start()

    if __name__ == "__main__":
        main()
#a extensao deixa tudo mais facil

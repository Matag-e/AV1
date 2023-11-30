from datetime import datetime
from faker import Faker

fake = Faker()

class Mensagem:
    def __init__(self, conteudo, formato=None, arquivo=None):
        self._conteudo = conteudo
        self._formato = formato
        self._arquivo = arquivo
        self._data_envio = datetime.now()

    def __str__(self):
        return f"{self._conteudo} ({self._formato})"

    @property
    def conteudo(self):
        return self._conteudo

    @property
    def formato(self):
        return self._formato

    @property
    def arquivo(self):
        return self._arquivo

    @property
    def data_envio(self):
        return self._data_envio

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, arquivo, duracao):
        super().__init__(conteudo, formato="Vídeo", arquivo=arquivo)
        self._duracao = duracao

    def __str__(self):
        return f"{super().__str__()}, Duração: {self._duracao}"

    @property
    def duracao(self):
        return self._duracao

class Canal:
    def __init__(self, destinatario):
        self._destinatario = destinatario

    @property
    def destinatario(self):
        return self._destinatario

    def obter_info_rede_social(self):
        raise NotImplementedError("Método 'obter_info_rede_social' deve ser implementado nas subclasses")

    def enviar_mensagem(self, mensagem):
        raise NotImplementedError("Método 'enviar_mensagem' deve ser implementado nas subclasses")

class CanalWhatsApp(Canal):
    def __init__(self, numero):
        super().__init__("@" + fake.user_name())  # Nome aleatório precedido por "@" para simular um usuário no WhatsApp
        self._numero = numero

    @property
    def numero(self):
        return self._numero

    def obter_info_rede_social(self):
        return "WhatsApp", self.numero

    def enviar_mensagem(self, mensagem):
        rede_social, info_contato = self.obter_info_rede_social()
        print(f"Enviando mensagem para {self.destinatario} ({info_contato}) via {rede_social}:")
        print(f"Conteúdo: {mensagem}")
        print(f"Data de envio: {mensagem.data_envio}")
        print("")
        ArmazenamentoMensagens().armazenar_mensagem(self, mensagem)

class CanalTelegram(Canal):
    def __init__(self):
        super().__init__("@" + fake.user_name())

    def obter_info_rede_social(self):
        return "Telegram", self.destinatario

    def enviar_mensagem(self, mensagem):
        rede_social, info_contato = self.obter_info_rede_social()
        print(f"Enviando mensagem para {self.destinatario} ({info_contato}) via {rede_social}:")
        print(f"Conteúdo: {mensagem}")
        print(f"Data de envio: {mensagem.data_envio}")
        print("")
        ArmazenamentoMensagens().armazenar_mensagem(self, mensagem)

class CanalFacebook(Canal):
    def __init__(self):
        super().__init__("@" + fake.user_name())

    def obter_info_rede_social(self):
        return "Facebook", self.destinatario

    def enviar_mensagem(self, mensagem):
        rede_social, info_contato = self.obter_info_rede_social()
        print(f"Enviando mensagem para {self.destinatario} ({info_contato}) via {rede_social}:")
        print(f"Conteúdo: {mensagem}")
        print(f"Data de envio: {mensagem.data_envio}")
        print("")
        ArmazenamentoMensagens().armazenar_mensagem(self, mensagem)

class CanalInstagram(Canal):
    def __init__(self):
        super().__init__("@" + fake.user_name())

    def obter_info_rede_social(self):
        return "Instagram", self.destinatario

    def enviar_mensagem(self, mensagem):
        rede_social, info_contato = self.obter_info_rede_social()
        print(f"Enviando mensagem para {self.destinatario} ({info_contato}) via {rede_social}:")
        print(f"Conteúdo: {mensagem}")
        print(f"Data de envio: {mensagem.data_envio}")
        print("")
        ArmazenamentoMensagens().armazenar_mensagem(self, mensagem)

class ArmazenamentoMensagens:
    def __init__(self, nome_arquivo="mensagens.txt"):
        self._nome_arquivo = nome_arquivo

    def armazenar_mensagem(self, canal, mensagem):
        rede_social, info_contato = canal.obter_info_rede_social()
        with open(self._nome_arquivo, "a") as arquivo:
            arquivo.write(f"{mensagem.conteudo} ({mensagem.formato}) - Enviada para {canal.destinatario} ({info_contato}) via {rede_social} em {mensagem.data_envio}\n")

class GerenciadorMensagens:
    def __init__(self):
        self._mensagens_enviadas = []

    def enviar_mensagem(self, canal, mensagem):
        try:
            canal.enviar_mensagem(mensagem)
            self._mensagens_enviadas.append((canal.destinatario, mensagem))
        except Exception as e:
            print(f"Erro ao enviar mensagem: {str(e)}")

    @property
    def mensagens_enviadas(self):
        return self._mensagens_enviadas


if __name__ == "__main__":
    gerenciador = GerenciadorMensagens()

    mensagem_texto = Mensagem("Olá, como vai?")
    mensagem_video = MensagemVideo("Vídeo legal!", "video.mp4", "2 minutos")

    canal_whatsapp = CanalWhatsApp("+55123456789")
    canal_telegram = CanalTelegram()
    canal_facebook = CanalFacebook()
    canal_instagram = CanalInstagram()

    gerenciador.enviar_mensagem(canal_whatsapp, mensagem_texto)
    gerenciador.enviar_mensagem(canal_telegram, mensagem_texto)
    gerenciador.enviar_mensagem(canal_facebook, mensagem_texto)
    gerenciador.enviar_mensagem(canal_instagram, mensagem_texto)

    gerenciador.enviar_mensagem(canal_whatsapp, mensagem_video)
    gerenciador.enviar_mensagem(canal_telegram, mensagem_video)
    gerenciador.enviar_mensagem(canal_facebook, mensagem_video)
    gerenciador.enviar_mensagem(canal_instagram, mensagem_video)

  #Exibe mensagens
    print("\nMensagens enviadas:")
    for destinatario, mensagem in gerenciador.mensagens_enviadas:
        print(f"Para: {destinatario}, Mensagem: {mensagem}")

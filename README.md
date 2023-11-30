# AV1

TRABALHO FACULDADE - UNINOVE

EXPLICAÇÃO:

O CODIGO CRIA AS CLASSES DE MENSAGEM e CANAL:

conteudo: Texto da mensagem.
formato: Formato da mensagem (por exemplo, "Texto", "Vídeo", etc.).
arquivo: Nome do arquivo associado à mensagem.
data_envio: Data e hora de envio.

CRIA AS INSTANCIAS DAS CLASSES DE MENSAGEM: MensagemTexto, MensagemVideo, etc..

CRIA AS INSTANCIAS DAS CLASSES DE CANAL: CanalWhatsApp, CanalTelegram, etc..

CRIA A CLASSE PARA ENVIO DE MENSAGEM: GerenciadorDeMensagens

E POR FIM EXIBE AS MENSAGENS ENVIADAS: print("\nMensagens enviadas:")
    for destinatario, mensagem in gerenciador.mensagens_enviadas:
        print(f"Para: {destinatario}, Mensagem: {mensagem}")

A LIB FAKER GERA NOMES RANDOMICOS QUE SÃO ARMAZENADOS JUNTO DAS MENSAGENS.

TODO O CONTEUDO É ARMAZENADO NO ARQUIVO mensagens.txt

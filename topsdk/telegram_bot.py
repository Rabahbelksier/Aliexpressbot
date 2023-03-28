import telebot
import requests
from requests_html import HTMLSession

apiKey = "6055626308:AAGzUX-NVvmrzDNRzF6g8Z-dumwf6S-iiXg"
bot = telebot.TeleBot(apiKey)


from topsdk.client import TopApiClient,TopException
# create Client
client = TopApiClient(appkey='34173206', app_sercet='a0d5286213b1b65b06c3c2ec2f30681c', top_gateway_url='http://api.taobao.com/router/rest',verify_ssl=True)

@bot.message_handler(content_types=['text'])
def handle_links(message):
    if message.text.startswith("http") and "aliexpress" in message.text.lower():
        print(message)

       # bot.reply_to(message, "Ajude nosso Grupo Comprando pelo nosso link.")
        link = message.text
        print(link)
        request_dict = {
            "promotion_link_type": 0,
            "source_values": link,
            "tracking_id": "dmsimports"
        }
        #  填充入参
        #  如果为复杂类型，填数据结构json字符串

        file_param_dict = {

        }
        #  填充文件类型入参（如有）

        try:
            response = client.execute("aliexpress.affiliate.link.generate", request_dict, file_param_dict)
            print(response)
            print(response['resp_result']['result']['promotion_links'][0])

            # RESPONSAVEL POR LOCALIZAR O RESULTADO DO PROMOTION_LINK NO DICIONARIO
            res = response['resp_result']['result']['promotion_links'][0]

            linkAff = res.get('promotion_link')
            if message.text and message.text.strip():
                if linkAff:
                    bot.reply_to(message, f"Ajude o Grupo Comprando pelo nosso link.  \n{linkAff}")
                    #bot.send_message(chat_id=message.chat.id, text=linkAff)
                    print(linkAff)
                else:
                 print(linkAff)

        except TopException as e:
            print(e)


bot.polling()

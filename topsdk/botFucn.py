import sys
import telebot
import requests
from requests_html import HTMLSession

apiKey = "6055626308:AAGzUX-NVvmrzDNRzF6g8Z-dumwf6S-iiXg"
bot = telebot.TeleBot(apiKey)

from topsdk.client import TopApiClient, TopException

def initialize_top_client():
    return TopApiClient(appkey='34173206', app_sercet='a0d5286213b1b65b06c3c2ec2f30681c', top_gateway_url='http://api.taobao.com/router/rest', verify_ssl=True)

def handle_promotion_links(client, link):
    request_dict = {
        "promotion_link_type": 0,
        "source_values": link,
        "tracking_id": "dmsimports"
    }
    file_param_dict = {}
    try:
        response = client.execute("aliexpress.affiliate.link.generate", request_dict, file_param_dict)
        res = response['resp_result']['result']['promotion_links'][0]
        return res.get('promotion_link')
    except TopException as e:
        print(e)
        return None
def get_product_details(url):
        session = HTMLSession()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
        }
        response = session.get(url, headers=headers)
        response.html.render(timeout=12)
        title = response.html.find('h1', first=True).text
        rating = response.html.find('.overview-rating-average', first=True)
        if rating:
            print("Avaliação média:", rating.text)
        else:
            print("Avaliação média não encontrada")

        rating_count = response.html.find('.product-reviewer-reviews', first=True).text.replace('Reviews', '').strip()
        if rating_count:
            print("Avaliação média:", rating.text)
        else:
            print("Avaliação média não encontrada")
        price = response.html.find('.product-price-value', first=True).text.replace('US', '').strip()
        links = response.html.absolute_links
        image_src = response.html.xpath('//*[@id="root"]/div/div[2]/div/div[1]/div/div/div[1]/img',
                                        first=True).attrs.get('src')
        print("Título:", title)
        print("Contagem de avaliações:", rating_count)
        print("Preço:", price)
        print("Links absolutos:", links)
        print("Imagem:", image_src)
@bot.message_handler(content_types=['text'])
def handle_links(message):
    if message.text.startswith("http") and "aliexpress" in message.text.lower():
        get_product_details(message.text)
        link = message.text
        client = initialize_top_client()
        linkAff = handle_promotion_links(client, link)
        if linkAff:
            bot.reply_to(message, f"Ajude nosso Grupo Comprando pelo nosso link.  \n{linkAff}")
            print(linkAff)
        else:
            print("Link not found")

bot.polling()

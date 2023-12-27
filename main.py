from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
import telebot
from topsdk.client import TopApiClient, TopException
import urllib.parse
import re

client = TopApiClient(appkey='502304', app_sercet='qq6EcmVKOIzv7iBJUcJGPEboMzO8y9vG', top_gateway_url='http://api.taobao.com/router/rest', verify_ssl=True)
apiKey = "6586708255:AAHO23LR49vLrhLF2B7lCHO4hZFBG2lxhds"
bot = telebot.TeleBot(apiKey)
class HomePage(Screen):

    def enviar_msg(self):
        print("BOTAO OK")
        desc_prod = self.ids.desc_prod.text
        title_prod = self.ids.title_prod.text
        imagem_prod = self.ids.url_imagem.text
        preco_prod = self.ids.valor_prod.text
        cupom_desc = self.ids.cupom_conta_nova.text
        preco_prod_antigo = self.ids.valor_conta_antiga.text
        cupom_usada = self.ids.cupom_conta_antiga.text
        link_aff = self.ids.link_afiliado.text
        if not imagem_prod:
            self.ids.url_imagem.text = "Campo obrigatório"
            return

        send_message_f(-1001887279681, photo=f"{imagem_prod}", caption_entities=[
            f"{desc_prod}\n\n\u26A1 {title_prod[0:75]}\n\n\u27A1 {link_aff}\n\n\U0001F525 Conta Nova\n\u2705 Valor: R${preco_prod}\U0001f631\U0001f631\U0001f631\n\U0001F3F7 Use o cupom: {cupom_desc}\n\n\U0001F525 Conta Antiga\n\u2705 Valor: R${preco_prod_antigo}\U0001f631\U0001f631\U0001f631\n\U0001F3F7 Use o cupom: {cupom_usada}\n\n\u27A1 {link_aff}"
        ])

        self.ids.link_produto.text = ""
        self.ids.desc_prod.text = ""
        self.ids.title_prod.text = ""
        self.ids.valor_prod.text = ""
        self.ids.cupom_conta_nova.text = ""
        self.ids.valor_conta_antiga.text = ""
        self.ids.cupom_conta_antiga.text = ""
        self.ids.url_imagem.text = ""
        self.ids.link_afiliado.text = ""
        pass



    def buscar_prod(self):
        link_p = self.ids.link_produto.text
        if not link_p:
            self.ids.link_produto.hint_text = "Campo obrigatório"
            return
        link_p = self.ids.link_produto.text
        #desc_prod = self.ids.desc_prod.text
        print(link_p)
        parsed_url = urllib.parse.urlparse(link_p)
        item_id = re.search(r'/(\d+)\.html', parsed_url.path).group(1)
        id_prod = item_id
        print(id_prod)
        # create Client


        request_dict = {
            "product_ids": id_prod,
            "target_language": "PT",
            "target_currency": "BRL",
            "tracking_id": "dmsimports",
            "pais": "BR"
        }

        #  填充入参
        #  如果为复杂类型，填数据结构json字符串

        file_param_dict = {}
        #  填充文件类型入参（如有）

        try:
            response = client.execute("aliexpress.affiliate.productdetail.get", request_dict, file_param_dict)
            if len(response['resp_result']['result']['products']) > 0:

                print(response)
                response = response['resp_result']['result']['products'][0]
                title_prod = response['product_title']
                preco_prod = response['target_app_sale_price']
                imagem_prod = response['product_main_image_url']
                link_prod = response['promotion_link']
                print(title_prod)
                print(imagem_prod)
                print(preco_prod)
                print(link_prod)
                self.ids.valor_prod.text = str(preco_prod)
                #self.ids.desc_prod.text = str(desc_prod)
                self.ids.title_prod.text = str(title_prod)
                self.ids.url_imagem.text = str(imagem_prod)
                self.ids.link_afiliado.text = str(link_prod)
                self.ids.msg_err.text = ""

                gerar_link(self, link_prod)
            else:
                print("Produto não encontrado")
                self.ids.msg_err.text = "Produto não encontrado"
                self.ids.link_produto.text = ""
                self.ids.desc_prod.text = ""
                self.ids.title_prod.text = ""
                self.ids.valor_prod.text = ""
                self.ids.cupom_conta_nova.text = ""
                self.ids.valor_conta_antiga.text = ""
                self.ids.cupom_conta_antiga.text = ""
                self.ids.url_imagem.text = ""
                self.ids.link_afiliado.text = ""

        except TopException as e:
            print(e)
        pass
class PostPage(Screen):
    def enviar_msg(self):

        print("BOTAO OK")
        desc_prod = self.ids.desc_prod.text
        title_prod = self.ids.title_prod.text
        imagem_prod = self.ids.url_imagem.text
        v1_prod = self.ids.v_prod.text
        valor_1 = self.ids.valor_prod.text
        v2_prod = self.ids.v_2.text
        valor_2 = self.ids.valor_v2.text
        v3_prod = self.ids.v_3.text
        valor_3 = self.ids.valor_v3.text
        if not imagem_prod:
            self.ids.url_imagem.text = "Campo obrigatório"
            return

        #cupom_desc = self.ids.cupom_conta_nova.text
        #preco_prod_antigo = self.ids.valor_conta_antiga.text
        #cupom_usada = self.ids.cupom_conta_antiga.text
        link_aff = self.ids.link_afiliado.text
        cupom_usada = self.ids.cupom_conta_nova.text



        # ENVIA A MENSAGEM PARA O CANAL NO TELEGRAM CASO O LINK TENHA SIDO GERADO
        send_message_f(-1001887279681, photo=f"{imagem_prod}", caption_entities=[
            f"\u26A1{title_prod[0:75]}\n\n"
            f"{desc_prod}\n\n"
            f"\u27A1 {link_aff}\n\n"
            f"\U0001F525 Contas Novas\n\n "
            f"{v1_prod}\n"
            f"\u2705 Valor: R${valor_1} \U0001f631\U0001f631\U0001f631\n\n"
            f"{v2_prod}\n"
            f"\u2705 Valor: R${valor_2} \U0001f631\U0001f631\U0001f631\n\n"
            f"{v3_prod}\n"
            f"\u2705 Valor: R${valor_3} \U0001f631\U0001f631\U0001f631\n\n"
            f"\U0001F3F7 Use o cupom: {cupom_usada}\n\n"
            f"\u27A1 {link_aff}"
        ])
        self.ids.link_produto.text = ""
        self.ids.desc_prod.text = ""
        self.ids.title_prod.text = ""
        self.ids.valor_prod.text = ""
        self.ids.cupom_conta_nova.text = ""
        self.ids.url_imagem.text = ""
        self.ids.link_afiliado.text = ""
        self.ids.v_prod.text = ""
        self.ids.valor_prod.text = ""
        self.ids.v_2.text = ""
        self.ids.valor_v2.text = ""
        self.ids.v_3.text = ""
        self.ids.valor_v3.text = ""

        pass

    def buscar_prod(self):
        link_p = self.ids.link_produto.text
        if not link_p:
            self.ids.link_produto.hint_text = "Campo obrigatório"
            return
        link_p = self.ids.link_produto.text
        #desc_prod = self.ids.desc_prod.text
        print(link_p)
        parsed_url = urllib.parse.urlparse(link_p)
        item_id = re.search(r'/(\d+)\.html', parsed_url.path).group(1)
        id_prod = item_id
        print(id_prod)
        # create Client


        request_dict = {
            "product_ids": id_prod,
            "target_language": "PT",
            "target_currency": "BRL",
            "tracking_id": "dmsimports",
            "pais": "BR"
        }

        #  填充入参
        #  如果为复杂类型，填数据结构json字符串

        file_param_dict = {}
        #  填充文件类型入参（如有）

        try:
            response = client.execute("aliexpress.affiliate.productdetail.get", request_dict, file_param_dict)
            if len(response['resp_result']['result']['products']) > 0:

                print(response)
                response = response['resp_result']['result']['products'][0]
                title_prod = response['product_title']
                preco_prod = response['target_app_sale_price']
                imagem_prod = response['product_main_image_url']
                link_prod = response['promotion_link']
                print(title_prod)
                print(imagem_prod)
                print(preco_prod)
                print(link_prod)
                self.ids.valor_prod.text = str(preco_prod)
                #self.ids.desc_prod.text = str(desc_prod)
                self.ids.title_prod.text = str(title_prod)
                self.ids.url_imagem.text = str(imagem_prod)
                self.ids.link_afiliado.text = str(link_prod)
                self.ids.msg_err.text = ""

                gerar_link(self, link_prod)
            else:
                print("Produto não encontrado")
                self.ids.msg_err.text = "Produto não encontrado"
                self.ids.link_produto.text = ""
                self.ids.desc_prod.text = ""
                self.ids.title_prod.text = ""
                self.ids.valor_prod.text = ""
                self.ids.cupom_conta_nova.text = ""
                self.ids.url_imagem.text = ""
                self.ids.link_afiliado.text = ""
                self.ids.v_prod.text = ""
                self.ids.valor_prod.text = ""
                self.ids.v_2.text = ""
                self.ids.valor_v2.text = ""
                self.ids.v_3.text = ""
                self.ids.valor_v3.text = ""

        except TopException as e:
            print(e)
        pass

GUI = Builder.load_file("main.kv")
class MainApp(App):
    def build(self):
        return GUI
    def mudar_tela(self, id_tela):
        print(id_tela)
        print(self.root.ids)
        gerenciador_telas = self.root.ids["screen_manager"]
        gerenciador_telas.current = id_tela

def send_message_f(group_id, photo, caption_entities):
    bot.send_photo(group_id, photo, caption_entities)
def gerar_link(self, link_prod):
        request_dict = {
                "promotion_link_type": 0,
                "source_values": link_prod,
                "tracking_id": "dmsimports"
        }
        #  填充入参
        #  如果为复杂类型，填数据结构json字符串
        file_param_dict = {}
        #  填充文件类型入参（如有）

        try:
            response = client.execute("aliexpress.affiliate.link.generate", request_dict, file_param_dict)
                # print(response)
                # print(response['resp_result']['result']['promotion_links'][0])

                # RESPONSAVEL POR LOCALIZAR O RESULTADO DO PROMOTION_LINK NO DICIONARIO
            res = response['resp_result']['result']['promotion_links'][0]
            link_aff = res.get('promotion_link')
            print(link_aff)
            self.ids.link_afiliado.text = str(link_aff)

        except TopException as e:
                print(e)

MainApp().run()

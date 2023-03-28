from topsdk.client import TopApiClient,TopException


if __name__ == '__main__':
    # create Client
    client = TopApiClient(appkey='34173206', app_sercet='a0d5286213b1b65b06c3c2ec2f30681c', top_gateway_url='http://api.taobao.com/router/rest',verify_ssl=False)


    link = "https://pt.aliexpress.com/item/1005004109269957.html"
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
        response = client.execute("aliexpress.affiliate.link.generate",request_dict,file_param_dict)
        #print(response)
        #print(response['resp_result']['result']['promotion_links'][0])

        #RESPONSAVEL POR LOCALIZAR O RESULTADO DO PROMOTION_LINK NO DICIONARIO
        res = response['resp_result']['result']['promotion_links'][0]
        linkAff = res.get('promotion_link')
        print(linkAff)



    except TopException as e:
        print(e)
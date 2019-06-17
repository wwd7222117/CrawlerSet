import scrapy
import json
import jsonpath
from chengfeng.items import ChengfengItem

class chengfeng_spider(scrapy.Spider):
    name = 'chengfeng_driver'

    start_urls = ['http://cy.chengfengkuaiyun.com/member/order/not_login/pending_receive?pageNumber=1&pageSize=1000']

    def parse(self,response):
        #base_url = "http://cy.chengfengkuaiyun.com/member/order/not_login/pending_receive?pageNumber=1&pageSize=10"
        unicodestr = json.loads(response.body)
        objects = jsonpath.jsonpath(unicodestr,'$.orders[*]')

        for i in objects:
            item = ChengfengItem()
            print(i['consignerName'])
            item['deliveryLongitude'] = i['deliveryLongitude']
            item['leftTon'] = i['leftTon']
            item['consignerName'] = i['consignerName']
            item['isOrderChatGroupMember'] = i['isOrderChatGroupMember']
            item['businessName'] = i['businessName']
            if 'tonString' in i:
                item['tonString'] = i['tonString']
            else:
                item['tonString'] = ''
            if 'arrearsDepositString' in i:
                item['arrearsDepositString'] = i['arrearsDepositString']
            else:
                item['arrearsDepositString'] = ''
            item['deliveryLatitude'] = i['deliveryLatitude']
            item['memo'] = i['memo']
            item['type'] = i['type']
            item['freightString'] = i['freightString']
            item['shippingTons'] = i['shippingTons']
            item['singlePrice'] = i['singlePrice']
            item['amountString'] = i['amountString']
            item['createdVersion'] = i['createdVersion']
            item['receivedTonsString'] = i['receivedTonsString']
            item['pendingShippingTons'] = i['pendingShippingTons']
            item['id'] = i['id']
            item['consignerPhone'] = i['consignerPhone']
            item['deliveryAreaCode'] = i['deliveryAreaCode']
            item['emptyFreightString'] = i['emptyFreightString']
            item['unloadFeeString'] = i['unloadFeeString']
            item['deliveryPlace'] = i['deliveryPlace']
            item['loadFeeString'] = i['loadFeeString']
            item['expectedPaymentDateString'] = i['expectedPaymentDateString']
            item['singlePriceString'] = i['singlePriceString']
            item['totalTon'] = i['totalTon']
            item['receivedTons'] = i['receivedTons']
            item['isFreightDistinct'] = i['isFreightDistinct']
            item['isExposure'] = i['isExposure']
            item['loadDateEndString'] = i['loadDateEndString']
            item['memberMobile'] = i['memberMobile']
            item['memberRole'] = i['memberRole']
            if 'unShared' in i:
                item['unShared'] = i['unShared']
            else:
                item['unShared'] = ''
            item['status'] = i['status']
            item['receiveAreaCode'] = i['receiveAreaCode']
            item['cargoType'] = i['cargoType']
            item['freightTonType'] = i['freightTonType']
            item['freight'] = i['freight']
            item['distanceString'] = i['distanceString']
            item['memberName'] = i['memberName']
            item['receiveLatitude'] = i['receiveLatitude']
            item['consumeRatio'] = i['consumeRatio']
            item['receivePlace'] = i['receivePlace']
            item['paymentType'] = i['paymentType']
            item['totalTonString']= i['totalTonString']
            item['consigneeName'] = i['consigneeName']
            item['orderDuration'] = i['orderDuration']
            if 'ton' in i:
                item['ton'] = i['ton']
            else:
                item['ton'] = ''
            item['receiveLongitude'] = i['receiveLongitude']
            item['shippingTonsString'] = i['shippingTonsString']
            item['consigneePhone'] = i['consigneePhone']
            item['sn'] = i['sn']
            if 'deficit' in i:
                item['deficit'] = i['deficit']
            else:
                item['deficit'] = ''
            item['amount'] = i['amount']
            item['cancelMessage'] = i['cancelMessage']
            if 'paymentMode' in i:
                item['paymentMode'] = i['paymentMode']
            else:
                item['paymentMode'] = ''
            item['consumeRatioString'] = i['consumeRatioString']
            item['createdDate'] = i['createdDate']
            item['createdDateString'] = i['createdDateString']
            item['pendingPaymentAmountString'] = i['pendingPaymentAmountString']
            item['loadDateBeginString'] = i['loadDateBeginString']
            item['pendingShippingTonsString'] = i['pendingShippingTonsString']
            item['leftTonString'] = i['leftTonString']
            yield item







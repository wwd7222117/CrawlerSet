# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class ChengfengItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    deliveryLongitude = Field()
    leftTon = Field()
    consignerName = Field()
    isOrderChatGroupMember = Field()
    businessName = Field()
    tonString = Field()
    arrearsDepositString = Field()
    deliveryLatitude = Field()
    memo = Field()
    type = Field()
    freightString = Field()
    shippingTons = Field()
    singlePrice = Field()
    amountString = Field()
    createdVersion = Field()
    receivedTonsString = Field()
    pendingShippingTons = Field()
    id = Field()
    consignerPhone = Field()
    deliveryAreaCode = Field()
    emptyFreightString = Field()
    unloadFeeString = Field()
    deliveryPlace = Field()
    loadFeeString = Field()
    expectedPaymentDateString = Field()
    singlePriceString = Field()
    totalTon = Field()
    receivedTons = Field()
    isFreightDistinct = Field()
    isExposure = Field()
    loadDateEndString = Field()
    memberMobile = Field()
    memberRole = Field()
    unShared = Field()
    status = Field()
    receiveAreaCode = Field()
    cargoType = Field()
    freightTonType = Field()
    freight = Field()
    distanceString = Field()
    memberName = Field()
    receiveLatitude = Field()
    consumeRatio = Field()
    receivePlace = Field()
    paymentType = Field()
    totalTonString = Field()
    consigneeName = Field()
    orderDuration = Field()
    ton = Field()
    receiveLongitude = Field()
    shippingTonsString = Field()
    consigneePhone = Field()
    sn = Field()
    deficit = Field()
    amount = Field()
    cancelMessage = Field()
    paymentMode = Field()
    consumeRatioString = Field()
    createdDate = Field()
    createdDateString = Field()
    pendingPaymentAmountString = Field()
    loadDateBeginString = Field()
    pendingShippingTonsString = Field()
    leftTonString = Field()
    pass
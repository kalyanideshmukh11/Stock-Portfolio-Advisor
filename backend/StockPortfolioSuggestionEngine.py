from flask import Flask
from flask import request
import json
import yfinance as yf
import requests
import datetime
import pytz
from pandas import DataFrame
import pandas as pd
import math
import datetime
from flask_cors import CORS
from flask_cors import *
app = Flask(__name__)


# Ethical Investing:
ethical_investing = ["AAPL", "TSLA", "ADBE"]
# Growth Investing :
growth_investing = ["AMZN", "VEEV", "NOW"]
# index Investing:
index_investing = ["FXAIX", "IVV", "SWPPX"]
# Quality Investing:
quality_investing = ["NVDA", "GOOGL", "CSCO"]
# Value Investing :
value_investing = ["INTC", "T", "CVS"]


@app.route("/calculateprofit", methods=['POST'])
@cross_origin(origins="*")
def stockStrategy():
    print('In Calculate Profit')
    # parameters = request.get_data("amount")
    Amount = request.json['amount']

    Strategies = request.json['strategies'].split(",")

    return return_data(Strategies, Amount)


def return_data(Strategies, Amount):
    result = []
    print('In return data')
    if(len(Strategies) > 1):
        print('Inside if statement')
        amount_for_strategy1 = int(Amount) / 2
        amount_for_strategy2 = int(Amount) / 2
        response_for_strategy1 = []
        response_for_strategy2 = []
        stock_list = []
        price = []
        

        if(Strategies[0] == "Index Investing" or Strategies[0] == "Ethical Investing" or Strategies[0] == "Growth Investing" or Strategies[0] == "Quality Investing" or Strategies[0] == "Value Investing"):
            if Strategies[0] == "Ethical Investing":
                    stock_list.append((ethical_investing[0]))
                    stock_list.append((ethical_investing[1]))
                    stock_list.append((ethical_investing[2]))
            elif Strategies[0] == "Growth Investing":
                    stock_list.append((growth_investing[0]))
                    stock_list.append((growth_investing[1]))
                    stock_list.append((growth_investing[2]))
            elif Strategies[0] == "Index Investing":
                    stock_list.append((index_investing[0]))
                    stock_list.append((index_investing[1]))
                    stock_list.append((index_investing[2]))
            elif Strategies[0] == "Quality Investing":
                    stock_list.append((quality_investing[0]))
                    stock_list.append((quality_investing[1]))
                    stock_list.append((quality_investing[2]))
            elif Strategies[0] == "Value Investing":
                    stock_list.append((value_investing[0]))
                    stock_list.append((value_investing[1]))
                    stock_list.append((value_investing[2]))

            response_for_strategy1 = (get_stock_quote(stock_list))
            stock_dict = {}
            stock_unit = {}
            
            print('----------------------------Response_From_Strategy1------------------------------------------------')
            print(response_for_strategy1)
            for i in response_for_strategy1:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0
            print('----------------------------Strategy1------------------------------------------------')
            print('----------------------------stock_dict------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit------------------------------------------------')
            print(stock_unit)    
            flag = 'true'
            while amount_for_strategy1 >= 0 and flag == 'true':
                
                flag = 'false'
                for i in stock_dict:
                    
                    if amount_for_strategy1 >= stock_dict.get(i):
                       amount_for_strategy1 = amount_for_strategy1 - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if amount_for_strategy1 > stock_dict.get(i)  :
                                flag = 'true'

            print('----------------------------Strategy1------------------------------------------------')
            print('----------------------------stock_dict------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit------------------------------------------------')
            print(stock_unit)
            for i in response_for_strategy1:
                if stock_unit[i['companyName']] > 0:
                    data_for_company = {}
                    data_for_company['CompantName'] = i['companyName']
                    data_for_company['CurrentPrice'] =(i['currentPrice'])
                    data_for_company['PercentageChange']=(i['percentage_change'])
                    data_for_company['ValueChange']=(i['value_change'])
                    data_for_company['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    data_for_company['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    data_for_company['Strategy'] = Strategies[0]
                    ticker = yf.Ticker(i['ticker'])
                    # print(ticker.history(interval = '5d'))
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    print('--------------DATE-------------------------------------------')
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    print(dataList)
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0,len(data['Open'])):
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])


                    data_for_company['HistoricalData'] = historical_data   
                    data_for_company['HistoricalDates'] = historical_dates
                    result.append(data_for_company) 
                     
        
            print('----------------------------Response From Strategy1------------------------------------------------')
            print(result)            
                
        if(Strategies[1] == "Index Investing" or Strategies[1]  == "Ethical Investing" or Strategies[1]  == "Growth Investing" or Strategies[1]  == "Quality Investing" or Strategies[1]  == "Value Investing"):
            stock_list = []
            if Strategies[1]  == "Ethical Investing":
                    stock_list.append((ethical_investing[0]))
                    stock_list.append((ethical_investing[1]))
                    stock_list.append((ethical_investing[2]))
            elif Strategies[1] == "Growth Investing":
                    stock_list.append((growth_investing[0]))
                    stock_list.append((growth_investing[1]))
                    stock_list.append((growth_investing[2]))
            elif Strategies[1]  == "Index Investing":
                    stock_list.append((index_investing[0]))
                    stock_list.append((index_investing[1]))
                    stock_list.append((index_investing[2]))
            elif Strategies[1]  == "Quality Investing":
                    stock_list.append((quality_investing[0]))
                    stock_list.append((quality_investing[1]))
                    stock_list.append((quality_investing[2]))
            elif Strategies[1]  == "Value Investing":
                    stock_list.append((value_investing[0]))
                    stock_list.append((value_investing[1]))
                    stock_list.append((value_investing[2]))
            stock_dict = {}
            stock_unit = {}
            response_for_strategy2 = (get_stock_quote(stock_list))
            print('----------------------------Response_From_Strategy2------------------------------------------------')
            print(response_for_strategy2)
           
            for i in response_for_strategy2:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0
            print('----------------------------Strategy1------------------------------------------------')
            print('----------------------------stock_dict------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit------------------------------------------------')
            print(stock_unit)    
            flag = 'true'
            while amount_for_strategy2 >= 0 and flag == 'true':
                flag = 'false'
                for i in stock_dict:
                    if amount_for_strategy2>= stock_dict.get(i):
                       amount_for_strategy2 = (amount_for_strategy2) - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if amount_for_strategy2 > stock_dict.get(i)  :
                                flag = 'true'
              
            print('----------------------------Strategy2------------------------------------------------')
            print('----------------------------stock_dict2------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit2------------------------------------------------')
            print(stock_unit)

            for i in response_for_strategy2:
                if stock_unit[i['companyName']] > 0:
                    data_for_company = {} 
                    data_for_company['CompantName'] = i['companyName']
                    data_for_company['CurrentPrice'] =(i['currentPrice'])
                    data_for_company['PercentageChange']=(i['percentage_change'])
                    data_for_company['ValueChange']=(i['value_change'])
                    data_for_company['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    data_for_company['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    ticker = yf.Ticker(i['ticker'])
                    data_for_company['Strategy'] = Strategies[1]
                    # print(ticker.history(interval = '5d'))
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    print('--------------DATE-------------------------------------------')
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    print(dataList)
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0, len(data['Open'])):
                        #historical_dates.append(data[0][i])
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])
                    data_for_company['HistoricalData'] = historical_data
                    data_for_company['HistoricalDates'] = historical_dates    
                    result.append(data_for_company)  
            print('----------------------------Response From Strategy2------------------------------------------------')
            print(result)
    else:
        print('--------------------Inside SINGLE STRATEGY statement-------------')
        amount_for_strategy1 = int(Amount)        
        response_for_strategy1 = []
        stock_list = []
        price = []
        

        if(Strategies[0] == "Index Investing" or Strategies[0] == "Ethical Investing" or Strategies[0] == "Growth Investing" or Strategies[0] == "Quality Investing" or Strategies[0] == "Value Investing"):
            if Strategies[0] == "Ethical Investing":
                    stock_list.append((ethical_investing[0]))
                    stock_list.append((ethical_investing[1]))
                    stock_list.append((ethical_investing[2]))
            elif Strategies[0] == "Growth Investing":
                    stock_list.append((growth_investing[0]))
                    stock_list.append((growth_investing[1]))
                    stock_list.append((growth_investing[2]))
            elif Strategies[0] == "Index Investing":
                    stock_list.append((index_investing[0]))
                    stock_list.append((index_investing[1]))
                    stock_list.append((index_investing[2]))
            elif Strategies[0] == "Quality Investing":
                    stock_list.append((quality_investing[0]))
                    stock_list.append((quality_investing[1]))
                    stock_list.append((quality_investing[2]))
            elif Strategies[0] == "Value Investing":
                    stock_list.append((value_investing[0]))
                    stock_list.append((value_investing[1]))
                    stock_list.append((value_investing[2]))

            response_for_strategy1 = (get_stock_quote(stock_list))
            stock_dict = {}
            stock_unit = {}
            
            print('----------------------------Response_From_Strategy1------------------------------------------------')
            print(response_for_strategy1)
            for i in response_for_strategy1:
                stock_dict[i['companyName']] = i['currentPrice']
                stock_unit[i['companyName']] = 0
            print('----------------------------Strategy1------------------------------------------------')
            print('----------------------------stock_dict------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit------------------------------------------------')
            print(stock_unit)    
            flag = 'true'
            while amount_for_strategy1 >= 0 and flag == 'true':
                
                flag = 'false'
                for i in stock_dict:
                    
                    if amount_for_strategy1 >= stock_dict.get(i):
                       amount_for_strategy1 = amount_for_strategy1 - stock_dict.get(i)
                       stock_unit[i] = stock_unit.get(i)+1
                       flag = 'true'
                    else :
                        for i in stock_dict:
                            if amount_for_strategy1 > stock_dict.get(i)  :
                                flag = 'true'

            print('----------------------------Strategy1------------------------------------------------')
            print('----------------------------stock_dict------------------------------------------------')
            print(stock_dict)
            print('----------------------------stock_unit------------------------------------------------')
            print(stock_unit)
            for i in response_for_strategy1:
                if stock_unit[i['companyName']] > 0:
                    data_for_company = {}
                    data_for_company['CompantName'] = i['companyName']
                    data_for_company['CurrentPrice'] =(i['currentPrice'])
                    data_for_company['PercentageChange']=(i['percentage_change'])
                    data_for_company['ValueChange']=(i['value_change'])
                    data_for_company['UnitsYouCanBuy'] = stock_unit[i['companyName']]
                    data_for_company['AmountYouInvest'] = stock_unit[i['companyName']]*i['currentPrice']
                    ticker = yf.Ticker(i['ticker'])
                    data_for_company['Strategy'] = Strategies[0]
                    # print(ticker.history(interval = '5d'))
                    data = DataFrame(ticker.history(period = '5d'))
                    temp_data = data.T
                    print('--------------DATE-------------------------------------------')
                    dataList = [datetime.datetime.date(cols) for cols in temp_data.columns]
                    print(dataList)
                    historical_data = []
                    historical_dates = dataList
                    for i in range(0, len(data['Open'])):
                        if(math.isnan(data['Open'][i])):
                            historical_data.append(0)
                        else:    
                            historical_data.append(data['Open'][i])
                    data_for_company['HistoricalData'] = historical_data   
                    data_for_company['HistoricalDates'] = historical_dates
                    result.append(data_for_company) 
                     
        
            print('----------------------------Response From Strategy1------------------------------------------------')
            print(result)                 

   
    resultdict={}
    resultdict['result']=result
    return resultdict


def get_stock_quote(stock_list):
    """Function that calls stock API for each stock to fetch stock details"""

    # Filter defining the data requirement
    param_filter = ['longName', 'bid', 'previousClose']
    stock_quote = []
    # Loopping through given stock and appending data to result
    for ticker in stock_list:
        stock = yf.Ticker(ticker)
        print('------------------LONG NAME---------')
        print(stock.info['longName'])
        print('------------------------------------------------------------Values from YF----------------------------')
        data = DataFrame(stock.history(period='1mo'))
       # print(DataFrame(stock.history(period='1mo')))
        currentData = data.iloc[-1, :]
        previousData = data.iloc[-2, :]
        previousClose = float(previousData[3])
        currentValue = float(currentData[3])
        print('-----------------------------------------previousclose----------------------')
        print(previousClose)
        print('-----------------------------------------currentvalue----------------------')
        print(currentValue)
        
        print("------------------------------API Rsponse-----------------------------")
        json_response={}
        print(json_response)
           
        
        value_change = round((currentValue-previousClose), 2)
        percentage_change = round(float((value_change/previousClose)*100), 2)
        value_change = ('+ ' + str(value_change)
                        ) if value_change >= 0 else str(value_change)
        percentage_change = ('+ ' + str(percentage_change) +
                             '%') if percentage_change >= 0 else str(percentage_change) + '%'
        
        json_response['companyName'] = stock.info['longName']
        json_response['currentPrice'] = currentValue
        json_response['ticker']=ticker
        json_response.update([('value_change', value_change), ('percentage_change', percentage_change)] )
        stock_quote.append(json_response)

    return stock_quote


if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(host="0.0.0.0", debug=True)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 02:21:40 2019

@author: kenneth
"""

import time
import os
import pandas as pd
from oandapyV20 import API
from oandapyV20.endpoints.pricing import PricingStream


path = {'mainPath': '/home/kenneth/Documents/GIT_PROJECTS/AI-Signal-Generator',
        'acountPath': 'DOCS/account_id.txt',
        'tokenPath': 'DOCS/token.txt',
        'environment': 'practice',
        'instruments': 'EUR_USD,GBP_USD,AUD_CAD,AUD_USD,BTC_USD,EUR_CAD,EUR_GBP,EUR_NZD,NZD_USD,XAU_USD,USD_JPY'}



class Quote(object):
    def __init__(self, path):
        '''Docstring
        params: path: dictionary of mainpath, account path and 
                        token path
        return type: None
        '''
        self.path = path
        return self.quoteStreamer()
    
    def accountDetails(self):
        #account -ID
        with open(os.path.join(self.path['mainPath'], self.path['acountPath'])) as acc:
            accountID = acc.readline().strip()
        #token   
        with open(os.path.join(self.path['mainPath'], self.path['tokenPath'])) as tok:
            token = tok.readline().strip()
        #account API
        api = API(access_token=token, environment=self.path['environment'])
        return accountID, api
        
       
    def arrowHead(self, prev, new):
        '''Docstring
        function compares previous bid price with
        new bid and return direction.
        
        :params: prev: previous bid price
        :params: new: new bid price
        :Return type: ^ Up 
                      v Down 
        '''
        if new > prev:
            return '^'
        else:
            return 'v'
        
    def quoteStreamer(self):
        AccID, api = self.accountDetails()
        
        if not os.path.exists(os.path.join(self.path['mainPath'], 'TICKERS')):
            os.makedirs(os.path.join(self.path['mainPath'], 'TICKERS'))
        try:
            while True:
                n = 0
                s = PricingStream(accountID=AccID, params={"instruments": self.path['instruments']})
                tickers = []
                try:
                    for R in api.request(s):
                        if R['type'] == 'PRICE':
                            rec = {'tickers': R['instrument'], 'bids': R['bids'][0]['price'], 'asks': R['asks'][0]['price'], 'direction': 'v'}
                            if len(tickers)+1 <= len(self.path['instruments'].split(',')):
                                tickers.append(rec)
                            else:
                                for enum, ii in enumerate(tickers):
                                    previous_bid = tickers[enum]['bids']
                                    if tickers[enum]['tickers'] == R['instrument']:
                                        tickers[enum]['bids'] = R['bids'][0]['price']
                                        tickers[enum]['asks'] = R['asks'][0]['price']
                                        tickers[enum]['direction'] = self.arrowHead(previous_bid, tickers[enum]['bids'])
                            df = pd.DataFrame([x for x in tickers], columns=['tickers', 'bids', 'asks', 'direction'])
                            df.to_csv(os.path.join(self.path['mainPath'], 'TICKERS/streams.csv'))
                            print(tickers)
                        else:
                            rec = {'tickers': R['instrument'], 'bids': R['bids'][0]['price'], 'asks': R['asks'][0]['price'], 'direction': 'v'}
                            if len(tickers)+1 <= len(self.path['instruments'].split(',')):
                                tickers.append(rec)
                            else:
                                for enum, ii in enumerate(tickers):
                                    previous_bid = tickers[enum]['bids']
                                    if tickers[enum]['tickers'] == R['instrument']:
                                        tickers[enum]['bids'] = R['bids'][0]['price']
                                        tickers[enum]['asks'] = R['asks'][0]['price']
                                        tickers[enum]['direction'] = self.arrowHead(previous_bid, tickers[enum]['bids'])
                            df = pd.DataFrame([x for x in tickers], columns=['tickers', 'bids', 'asks', 'direction'])
                            df.to_csv(os.path.join(self.path['mainPath'], 'TICKERS/streams.csv'))
                            print(tickers)
                except:
                    pass
                n += 1
                try:
                    if n > 10:
                        time.sleep(10)
                except:
                    pass
                continue
        except:
            pass
        
if __name__ == '__main__' :
    Quote(path)     


    
    
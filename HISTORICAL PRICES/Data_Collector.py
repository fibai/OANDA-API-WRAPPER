# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:30:21 2019

@author: kennedy
"""

class Path(object):
    def __init__(self, path):
        self.path = path
        self.loadPath()
        
    def loadPath(self):
      import os
      try:
        if os.path.exists(self.path):
          try:
            FOLDERS = ['/DATASETS', 
                       '/PREDICTED', 
                       '/IMAGES',
                       '/TICKERS',
                       '/MODEL']
            FOLDER_COUNT = 0
            for folders in FOLDERS:
              '''If folder is not created or created but deleted..Recreate/Create the folder.
              Check for all folders in the FOLDERS list'''
              if not os.path.exists(self.path + FOLDERS[FOLDER_COUNT]):
                os.makedirs(self.path + FOLDERS[FOLDER_COUNT])
                print('====== 100% Completed ==== : {}'.format(self.path + FOLDERS[FOLDER_COUNT]))
                FOLDER_COUNT += 1
              elif os.path.exists(self.path + FOLDERS[FOLDER_COUNT]):
                '''OR check if the file is already existing using a boolean..if true return'''
                print('File Already Existing : {}'.format(self.path + FOLDERS[FOLDER_COUNT]))
                FOLDER_COUNT += 1
          except OSError as e:
              '''raise OSError('File Already Existing {}'.format(e))'''
              print('File Already existing: {}'.format(e))
        elif not os.path.exists(self.path):
            raise OSError('File self.path: {} does not exist\n\t\tPlease check the self.path again'.format(self.path))
        else:
            print('File Already Existing')
      except Exception as e:
          raise(e)
      finally:
          print('Process completed...Exiting')


class stockDownload(Path):
    def __init__(self, instrument, start, end, client, granular):
        self.instrument = instrument
        self.start = start
        self.end = end
        self.client = client
        self.granular = granular
        
    def downloadStockData(self):
        '''
          :Arguments:
            :instruments:
              Name of the instrument we are trading
            :start: specify the start date of stcok to download
            :end: specify end date of the stock to download
            
          :Returntype:
            return the csv file of the downloaded stock in the
            specific folder.
        '''
        def covert_json(reqst, frame):
            for candle in reqst.get('candles'):
                ctime = candle.get('time')[0:19]
                try:
                    rec = '{time},{complete},{o},{h},{l},{c},{v}'.format(time = ctime,
                           complete = candle['complete'],
                           o = candle['mid']['o'],
                           h = candle['mid']['h'],
                           l = candle['mid']['l'],
                           c = candle['mid']['c'],
                           v = candle['volume'])
                except Exception as e:
                    raise(e)
                else:
                    frame.write(rec+'\n')
                
                
        #try except to both create folder and enter ticker
        try:
            if not os.path.exists(path + '/DATASETS/{}'.format(self.instrument)):
                os.makedirs(path + '/DATASETS/{}'.format(self.instrument))
            #import the required timeframe
            for timeframe, descrp in self.granular.items():
                with open(path + '/DATASETS/{}/{}_{}.csv'.format(self.instrument, self.instrument, timeframe), 'w') as OUTPUT:
                    params = {'from': self.start,
                              'to': self.end,
                              'granularity': timeframe,
                              'counts': 2500
                              }
                    try:
                      for ii in InstrumentsCandlesFactory(instrument=self.instrument, params=params):
                          print("REQUEST: {} {} {}".format(ii, ii.__class__.__name__, ii.params))
                          self.client.request(ii)
                          covert_json(ii.response, OUTPUT)
                    except:
                        print('{} not available using this API'.format(instrument))
                    print('********************Done downloading******************\n{}_{}'.format(self.instrument, timeframe))
        except Exception as e:
            raise(e)
        finally:
            print('*'*40)
            print('Stock download completed')
            print('*'*40)

class Run():
    def __init__(self, instrument, start, end, api, granular, timer):
        self.timer = timer
        self.instrument = instrument
        self.start = start
        self.end = end
        self.api = api
        self.granular = granular
        
        try:
            if self.timer is None:
                raise ValueError('set timer')
            else:
                thread = threading.Thread(target = self.runMain)
                thread.daemon = True
                thread.start()
                thread.join()
        except Exception:
            raise ValueError('Thread unable to start')
            
    def runMain(self):
        while True:
            if not self.instrument:
                break
            elif not self.start:
                break
            elif not self.end:
                break
            elif not self.api:
                raise ValueError('client api not found')
            elif not self.granular:
                break
            else:
                for ij in self.instrument:
                    stockDownload(ij, self.start, self.end, self.api, self.granular).downloadStockData()
            time.sleep(self.timer)


if __name__ == '__main__':
  #import required libraries
  import os
  import datetime
  import threading
  import time
  path = '/home/kenneth/Documents/GIT_PROJECTS/AI-Signal-Generator'
  os.chdir(path)
  #load path
  ldfolder = Path(path)
  from oandapyV20 import API
  from oandapyV20.contrib.factories import InstrumentsCandlesFactory
  with open(path +'/DOCS/token.txt') as tk:
    token = tk.readline().strip()
    client = API(access_token = token)
  
  #  instrument should be a dropdown option
  instrument = ['EUR_USD', 'GBP_USD', 'AUD_CAD', 'AUD_USD',
                'BTC_USD', 'EUR_CAD', 'EUR_GBP', 'EUR_NZD',
                'NZD_USD']
  
  #'Note however that this may be time consuming as the dataset is huge
  CandlestickGranularity_ = {
          "M15": "15 minute candlesticks, hour alignment",
          "M30": "30 minute candlesticks, hour alignment",
          "H1": "1 hour candlesticks, hour alignment",
          "H2": "1 hour candlesticks, day alignment",
          "H3": "3 hour candlesticks, day alignment",
          "H4": "4 hour candlesticks, day alignment",
          "H6": "6 hour candlesticks, day alignment",
          "H8": "8 hour candlesticks, day alignment",
          "H12": "12 hour candlesticks, day alignment",
      }
  CandlestickGranularity_WD = {
          "D": "1 day candlesticks, day alignment",
          "W": "1 week candlesticks, aligned to start of week",
          }
  #download stock data
  _from_gr = '2019-03-01T00:00:00Z'
  _end_gr = datetime.datetime.utcnow().isoformat('T')+'Z'
  _end_gr = str(_end_gr[:-8] + 'Z')
  _from = '2017-01-01T00:00:00Z'
  _end = datetime.datetime.utcnow().isoformat('T')+'Z'
  _end = str(_end[:-8] + 'Z')
  Run(instrument, _from, _end, client, CandlestickGranularity_WD, 86400)
  Run(instrument, _from_gr, _end_gr, client, CandlestickGranularity_, 1800)






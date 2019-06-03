## About

```python
The Data Collector class is an automated multi-threaded class designed
to donwload stock prices at defined time intervals. 

Here we set it to:
timer = [1800, 86400]

The first(timer[0]) updates every 30mins (30*60) for timeframes

{
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
      
the second(timer[1]) process updates every 24hours (24*60*60) for timeframes

{
          "D": "1 day candlesticks, day alignment",
          "W": "1 week candlesticks, aligned to start of week",
          }
          
```
## Requirements

```python
oandapyV20

pip install oandapyV20
```

## How to use

Ensure you have your token from Oanda stored in the token folder

```python
with open(path +'/DOCS/token.txt') as tk:
    token = tk.readline().strip()
    client = API(access_token = token)
```

Change line 243 and 246 according to the desired start date for CandlestickGranularity_.

```python
Note that the line 243 is for period 
{
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
      
Line 246 is for periods
        {
          "D": "1 day candlesticks, day alignment",
          "W": "1 week candlesticks, aligned to start of week",
          }

```
```python
$ python Data_Collector.py
```

OUTPUT is stores in DATASET FOLDER

```python
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-04-22T02:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-22T02:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-05-12T22:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-12T22:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-02T18:00:00Z'}
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-06-02T18:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_M30
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-03-21T20:00:00Z'}
********************Done downloading******************
EUR_NZD_H2
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-21T20:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
EUR_NZD_H3
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
EUR_NZD_H4
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H6', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H1
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-04-11T16:00:00Z'}
********************Done downloading******************
EUR_NZD_H6
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H8', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
EUR_NZD_H8
REQUEST: v3/instruments/EUR_NZD/candles InstrumentsCandles {'granularity': 'H12', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
EUR_NZD_H12
****************************************
Stock download completed
****************************************
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-03-06T05:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-06T05:00:00Z', 'to': '2019-03-11T10:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-11T10:00:00Z', 'to': '2019-03-16T15:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-16T15:00:00Z', 'to': '2019-03-21T20:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-21T20:00:00Z', 'to': '2019-03-27T01:00:00Z'}
********************Done downloading******************
NZD_USD_H2
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-27T01:00:00Z', 'to': '2019-04-01T06:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-01T06:00:00Z', 'to': '2019-04-06T11:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H3
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-06T11:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-04-16T21:00:00Z'}
********************Done downloading******************
NZD_USD_H4
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H6', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-16T21:00:00Z', 'to': '2019-04-22T02:00:00Z'}
********************Done downloading******************
NZD_USD_H6
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H8', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-22T02:00:00Z', 'to': '2019-04-27T07:00:00Z'}
********************Done downloading******************
NZD_USD_H8
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H12', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-27T07:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-05-07T17:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-07T17:00:00Z', 'to': '2019-05-12T22:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-12T22:00:00Z', 'to': '2019-05-18T03:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-18T03:00:00Z', 'to': '2019-05-23T08:00:00Z'}
********************Done downloading******************
NZD_USD_H12
****************************************
Stock download completed
****************************************
program running in background
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-05-28T13:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-28T13:00:00Z', 'to': '2019-06-02T18:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M15', 'counts': 2500, 'includeFirst': True, 'from': '2019-06-02T18:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_M15
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-03-11T10:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-11T10:00:00Z', 'to': '2019-03-21T20:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-21T20:00:00Z', 'to': '2019-04-01T06:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-01T06:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-04-22T02:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-22T02:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-05-12T22:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-12T22:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-02T18:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'M30', 'counts': 2500, 'includeFirst': True, 'from': '2019-06-02T18:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_M30
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-03-21T20:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-21T20:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H1', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H1
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-04-11T16:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-04-11T16:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H2', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H2
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-02T12:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H3', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-02T12:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H3
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-05-23T08:00:00Z'}
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H4', 'counts': 2500, 'includeFirst': True, 'from': '2019-05-23T08:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H4
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H6', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H6
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H8', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H8
REQUEST: v3/instruments/NZD_USD/candles InstrumentsCandles {'granularity': 'H12', 'counts': 2500, 'includeFirst': True, 'from': '2019-03-01T00:00:00Z', 'to': '2019-06-03T22:43:21Z'}
********************Done downloading******************
NZD_USD_H12
****************************************
Stock download completed
****************************************
program running in background
```

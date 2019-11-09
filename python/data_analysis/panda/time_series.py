import pandas as pd
import numpy as np

time_df = pd.DataFrame(np.array(['2017-12-30 12:00:00', '2017-12-31 12:00:00',
               '2018-01-01 12:00:00', '2018-01-02 12:00:00',
               '2018-01-03 12:00:00', '2018-01-04 12:00:00',
               '2018-01-05 12:00:00', '2018-01-06 12:00:00',
               '2018-01-07 12:00:00', '2018-01-08 12:00:00',
               '2018-01-09 12:00:00', '2018-01-10 12:00:00',
               '2018-01-11 12:00:00', '2018-01-12 12:00:00',
               '2018-01-13 12:00:00', '2018-01-14 12:00:00',
               '2018-01-15 12:00:00', '2018-01-16 12:00:00',
               '2018-01-17 12:00:00', '2018-01-18 12:00:00',
               '2018-01-19 12:00:00', '2018-01-20 12:00:00',
               '2018-01-21 12:00:00', '2018-01-22 12:00:00',
               '2018-01-23 12:00:00', '2018-01-24 12:00:00',
               '2018-01-25 12:00:00', '2018-01-26 12:00:00',
               '2018-01-27 12:00:00', '2018-01-28 12:00:00',
               '2018-01-29 12:00:00']).reshape(31, 1), columns=['timeStamp'])
# print(time_df)
# time_series = pd.date_range(start='2017-12-30 12:00:00', end='20180130', freq='D')
# print(time_series)

# time_df['timeStamp'] = pd.to_datetime(time_df['timeStamp'])
# time_df['random_data'] = np.zeros((31, 1))
# time_df.set_index('timeStamp', inplace=True)
# print(time_df)
# print(time_df.resample('M').count())

periods = pd.PeriodIndex(year=[1910], month=[5], day=[10], hour=[10], freq='H')
print(periods)

# -*- coding: utf-8 -*-
# 原程序是python3.x的，为了使得可以在python2.x下使用，考虑将数据集导出为pickle格式

from smallnorb.dataset import SmallNORBDataset

data = SmallNORBDataset(dataset_root='smallnorb_data')

train = [{'image_lt':i.image_lt,
          'image_rt':i.image_rt,
          'category':i.category,
          'instance':i.instance,
          'elevation':i.elevation,
          'azimuth':i.azimuth,
          'lighting':i.lighting} for i in data.data['train']]

test = [{'image_lt':i.image_lt,
         'image_rt':i.image_rt,
         'category':i.category,
         'instance':i.instance,
         'elevation':i.elevation,
         'azimuth':i.azimuth,
         'lighting':i.lighting} for i in data.data['test']]

data = {'train': train, 'test':test}


import pickle
# protocol=2 是为了兼容python2
pickle.dump(data, open('smallnorb.pickle', 'wb'), protocol=2)

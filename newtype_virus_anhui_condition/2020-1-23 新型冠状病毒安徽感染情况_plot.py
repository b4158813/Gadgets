#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import json
import plotly.graph_objects as go


# In[82]:


places = pd.DataFrame([ ['合肥',117.22,31.82,352],
                      ['安庆',117.05,30.52,230],
                      ['池州',117.49,30.66,228],
                      ['芜湖',118.43,31.82,350],
                      ['蚌埠',117.39,32.92,265],
                      ['淮南',116.99,32.63,264],
                      ['马鞍山',118.5,31.71,347],
                      ['淮北',116.8,33.95,266],
                      ['铜陵',117.81,30.94,229],
                      ['黄山',118.33,29.71,227],
                      ['滁州',118.32,32.3,354],
                      ['阜阳',115.81,32.89,263],
                      ['宿州',116.98,33.64,267],
                      ['巢湖',117.86,31.59,351],
                      ['六安',116.51,31.75,353],
                      ['亳州',115.78,33.84,268],
                      ['宣城',118.76,30.94,339]],
                      columns = ['name','lon','lat','id'])


# In[83]:


places.head()


# In[84]:


token = 'pk.eyJ1IjoiYjQxNTg4MTMiLCJhIjoiY2s1cWN3YnJuMDE0dDNlbXFzdWhnbXZoMSJ9.opAX-vO03md-Odmubn_nKA'


# In[85]:


virus_cnt = pd.DataFrame([['合肥',5],
                        ['六安',1,],
                        ['滁州',1],
                        ['阜阳',1],
                        ['亳州',1],
                        ['安庆',1]],
                        columns = ['name','cnt'])
virus_cnt


# In[86]:


result = pd.merge(virus_cnt,places,how='outer').fillna(0)
result


# In[87]:


with open(r"map-master\map-master\geo\Anhui.geojson",encoding='utf-8-sig')as f:
    anhui_geo = json.load(f)


# In[88]:


fig = go.Figure(go.Choroplethmapbox(geojson=anhui_geo,
                                    locations = result['id'],
                                  z = result['cnt'],
                                  hovertext = result['name'],
                                  hoverinfo = 'text + z',
                                  colorscale = 'amp',
                                  marker_line_color = 'rgb(169,164,159)',
                                  marker_line_width = 0.5
                                  ))
fig.update_layout(mapbox = {'accesstoken':token,
                           'center':{'lon':117.22,'lat':31.82},
                            'zoom':9.4},
                  title = {'text':"新型冠状病毒 安徽省感染情况",
                          'xref':'paper',
                          'x':0.5},
                  margin = {'l':0,'r':0,'t':30,'b':0}
                )
fig.show()


# In[ ]:





from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, Select
from bokeh.layouts import column

from pre_process import data_dict, zips

num_months = 12
default = [0]*num_months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

all_avg = [sum(monthly[i] for monthly in data_dict.values() if i < len(monthly)) /
           len([monthly for monthly in data_dict.values() if i < len(monthly)])
              for i in range(num_months)]

source = ColumnDataSource(data={'month': months, 'avg': all_avg, 'zip1':[0]*num_months, 'zip2':[0]*num_months})

p = figure(x_range=months, height=400, width=700, title="Average Duration of Complaints Over Time - 2024", x_axis_label='Month', y_axis_label='Average Duration (hours)')
p.line(x='month', y='avg', source=source, line_width=2, color='blue', legend_label='All Zip Codes')
p.line(x='month', y='zip1', source=source, line_width=2, color='green', legend_label='Zip Code 1')
p.line(x='month', y='zip2', source=source, line_width=2, color='red', legend_label='Zip Code 2')
p.legend.location = "top_left"

zip_codes = sorted(zips)
zip_str = [str(z) for z in zips]

if len(zip_str) > 1: 
    select_zip1 = Select(title="Select Zip Code 1:", value=zip_str[0], options=zip_str)
    select_zip2 = Select(title="Select Zip Code 2:", value=zip_str[1], options=zip_str) 
else: 
    select_zip1 = Select(title="Select Zip Code 1:", value=zip_str[0], options=zip_str)
    select_zip2 = Select(title="Select Zip Code 2:", value=zip_str[0], options=zip_str)


def update_plot(attr, old, new):
    zip1 = select_zip1.value
    zip2 = select_zip2.value
    zip1_data = data_dict.get(zip1, default)
    zip2_data = data_dict.get(zip2, default)
    zip1_data = (zip1_data + default)[:num_months]
    zip2_data = (zip2_data + default)[:num_months]
    
    source.data = {'month': months, 'avg': all_avg, 'zip1': zip1_data, 'zip2': zip2_data}

select_zip1.on_change('value', update_plot)
select_zip2.on_change('value', update_plot) 

layout = column(select_zip1, select_zip2, p)
curdoc().add_root(layout)
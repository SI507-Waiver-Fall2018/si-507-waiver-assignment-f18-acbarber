# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets
plotly.tools.set_credentials_file(username='acbarber', api_key='8iPI9o16Ci8trx0G1EsF')

noun_data=open('noun_data.csv', 'r')
readlines=noun_data.readlines()
noun_data.close()
data_list_n=[]
for line in readlines:
    data_list_n.append(line.split(','))

numbers=[]
for pair in data_list_n[1:]:
    if '\n' in pair[1]:
        numbers.append(pair[1][:-1])
    else:
        numbers.append(pair[1])



labels=[]
for pair in data_list_n[1:]:
    labels.append(pair[0])

layout= go.Layout(title='Top 5 Nouns', xaxis=dict(title='Noun'), yaxis=dict(title='Number of Occurences'))

bar_chart=[go.Bar(x=labels, y=numbers)]

fig= go.Figure(data=bar_chart, layout=layout)

part4_chart=py.plot(fig, filename='part4_viz_image')

py.image.save_as(fig, filename='part4_viz_image.png')

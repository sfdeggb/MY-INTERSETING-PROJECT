# import plotly.express as px

# tips = px.data.tips()
# fig = px.parallel_categories(tips,
#                              color='size',
#                              color_continuous_scale=px.colors.sequential.Inferno)
# fig.show()

import plotly.express as px
import pandas as pd

gapminder = px.data.gapminder()
#设置pandas库要打印多少行
pd.set_option("display.max_rows", 30)
#进行二次对象转化
data = pd.DataFrame(gapminder)

print("data sytly is belowing--------")
print(data)
print("data is ending -------------")

fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
           hover_name="country", log_x=True, size_max=60)#指定如何显示多个数据的
fig.show()
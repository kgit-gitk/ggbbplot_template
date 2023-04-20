import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point, theme, element_text, element_rect, element_blank, element_line, scale_y_continuous, scale_x_date, labs
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from plotnine import (ggplot, aes, geom_line, geom_point, theme, element_text, element_rect, element_blank,
                      element_line, scale_y_continuous, scale_x_date, labs, scale_color_manual)

# Sample data
data = {
    'Date': pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'),
    'Category1': [25, 45, 15, 30, 35, 42, 28, 22, 39, 51, 29, 36],
    'Category2': [30, 40, 20, 35, 30, 37, 33, 27, 44, 46, 34, 31],
    'Category3': [35, 55, 25, 40, 45, 52, 38, 32, 49, 61, 39, 46],
    'Category4': [40, 60, 30, 45, 50, 57, 43, 37, 54, 66, 44, 51]
}

df = pd.DataFrame(data)
df = df.melt(id_vars=['Date'], var_name='Category', value_name='Value')

# Color palette based on the base blue color
color_palette = {
    'Category1': '#6B96C3',
    'Category2': '#3D6680',
    'Category3': '#274C63',
    'Category4': '#1A3346'
}

# Very dark gray, almost black
very_dark_gray = '#1a1a1a'

# BBC style theme for plotnine
bbc_style_theme = theme(
    plot_title=element_blank(),
    legend_position='top',
    legend_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    legend_background=element_blank(),
    legend_title=element_blank(),
    legend_key=element_blank(),
    axis_title=element_blank(),
    axis_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    axis_text_x=element_text(margin={'b': 10}, angle=45, ha='right'),
    axis_ticks=element_blank(),
    axis_line=element_blank(),
    axis_line_x=element_line(color=very_dark_gray, size=1.2),
    axis_line_y=element_blank(),
    panel_grid_minor=element_blank(),
    panel_grid_major_y=element_line(color='#cbcbcb'),
    panel_grid_major_x=element_blank(),
    panel_background=element_blank(),
    strip_background=element_rect(fill='white'),
    strip_text=element_text(size=22, hjust=0),
    plot_caption=element_text(ha='right', color=very_dark_gray, margin={'t': 10})
)

# Create the line chart with the BBC style theme and the color palette
chart_bbc_style = (
    ggplot(df, aes(x='Date', y='Value', color='Category'))
    + geom_line(size=1.5)
    + geom_point(size=4)
    + scale_y_continuous(expand=(0, 0), limits=(0, 70))
    + scale_x_date(date_labels="%b '%y", breaks=pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'))
    + labs(y="Y Axis Title", caption="Footnote")
    + scale_color_manual(values=color_palette)
    + bbc_style_theme
)

# Set figure size
fig, _ = chart_bbc_style.draw(return_ggplot=True)
fig.set_size_inches(12, 6)

# Add title and subtitle
ax = fig.get_axes()[0]
ax.set_title("Title", fontweight="bold", fontsize=20, fontname="Helvetica", ha="left", x=0, y=1.1)
# ax.set_title("Subtitle", fontsize=16, fontname="Helvetica", ha="left", x=0, y=1.0)

# Move caption to the left
caption = ax.get_children()[-1]

# Show the chart
plt.show()

######################
import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point, theme, element_text, element_rect, element_blank, element_line, scale_y_continuous, scale_x_date, labs
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'),
    'Value': [25, 45, 15, 30, 35, 42, 28, 22, 39, 51, 29, 36]
}

df = pd.DataFrame(data)

# Main blue color
main_blue = '#6B96C3'

# Very dark gray, almost black
very_dark_gray = '#1a1a1a'

# BBC style theme for plotnine
bbc_style_theme = theme(
    plot_title=element_blank(),
    legend_position='top',
    legend_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    legend_background=element_blank(),
    legend_title=element_blank(),
    legend_key=element_blank(),
    axis_title=element_blank(),
    axis_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    axis_text_x=element_text(margin={'b': 10}, angle=45, ha='right'),
    axis_ticks=element_blank(),
    axis_line=element_blank(),
    axis_line_x=element_line(color=very_dark_gray, size=1.2),
    axis_line_y=element_blank(),
    panel_grid_minor=element_blank(),
    panel_grid_major_y=element_line(color='#cbcbcb'),
    panel_grid_major_x=element_blank(),
    panel_background=element_blank(),
    strip_background=element_rect(fill='white'),
    strip_text=element_text(size=22, hjust=0),
    plot_caption=element_text(ha='right', color=very_dark_gray, margin={'t': 10})
)

# Create the line chart with the BBC style theme and main blue color
chart_bbc_style = (
    ggplot(df, aes(x='Date', y='Value'))
    + geom_line(color=main_blue, size=1.5)
    + geom_point(color=main_blue, size=4)
    + scale_y_continuous(expand=(0, 0), limits=(0, 60))
    + scale_x_date(date_labels="%b '%y", breaks=pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'))
    + labs(y="Y Axis Title", caption="Footnote")
    + bbc_style_theme
)

# Set figure size
fig, _ = chart_bbc_style.draw(return_ggplot=True)
fig.set_size_inches(12, 6)

# Add title and subtitle
ax = fig.get_axes()[0]
ax.set_title("Title", fontweight="bold", fontsize=20, fontname="Helvetica", ha="left", x=0, y=1.1)
#ax.set_title("Subtitle", fontsize=16, fontname="Helvetica", ha="left", x=0, y=1.0)

# Move caption to the left
caption = ax.get_children()[-1]


# Show the chart
plt.show()

##############
import pandas as pd
from plotnine import ggplot, aes, geom_line, geom_point, theme, element_text, element_rect, element_blank, element_line, scale_y_continuous, scale_x_date, labs
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from plotnine import (ggplot, aes, geom_line, geom_point, theme, element_text, element_rect, element_blank,
                      element_line, scale_y_continuous, scale_x_date, labs, scale_color_manual)

# Sample data
data = {
    'Date': pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'),
    'Category1': [25, 45, 15, 30, 35, 42, 28, 22, 39, 51, 29, 36],
    'Category2': [30, 40, 20, 35, 30, 37, 33, 27, 44, 46, 34, 31],
    'Category3': [35, 55, 25, 40, 45, 52, 38, 32, 49, 61, 39, 46],
    'Category4': [40, 60, 30, 45, 50, 57, 43, 37, 54, 66, 44, 51]
}

df = pd.DataFrame(data)
df = df.melt(id_vars=['Date'], var_name='Category', value_name='Value')

# Color palette based on the base blue color
color_palette = {
    'Category1': '#6B96C3',
    'Category2': '#3D6680',
    'Category3': '#274C63',
    'Category4': '#1A3346'
}

# Very dark gray, almost black
very_dark_gray = '#1a1a1a'

# BBC style theme for plotnine
bbc_style_theme = theme(
    plot_title=element_blank(),
    legend_position='top',
    legend_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    legend_background=element_blank(),
    legend_title=element_blank(),
    legend_key=element_blank(),
    axis_title=element_blank(),
    axis_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    axis_text_x=element_text(margin={'b': 10}, angle=45, ha='right'),
    axis_ticks=element_blank(),
    axis_line=element_blank(),
    axis_line_x=element_line(color=very_dark_gray, size=1.2),
    axis_line_y=element_blank(),
    panel_grid_minor=element_blank(),
    panel_grid_major_y=element_line(color='#cbcbcb'),
    panel_grid_major_x=element_blank(),
    panel_background=element_blank(),
    strip_background=element_rect(fill='white'),
    strip_text=element_text(size=22, hjust=0),
    plot_caption=element_text(ha='right', color=very_dark_gray, margin={'t': 10})
)

# Create the line chart with the BBC style theme and the color palette
chart_bbc_style = (
    ggplot(df, aes(x='Date', y='Value', color='Category'))
    + geom_line(size=1.5)
    + geom_point(size=4)
    + scale_y_continuous(expand=(0, 0), limits=(0, 70))
    + scale_x_date(date_labels="%b '%y", breaks=pd.date_range(start='2020-01-01', end='2020-12-31', freq='M'))
    + labs(y="Y Axis Title", caption="Footnote")
    + scale_color_manual(values=color_palette)
    + bbc_style_theme
)

# Set figure size
fig, _ = chart_bbc_style.draw(return_ggplot=True)
fig.set_size_inches(12, 6)

# Add title and subtitle
ax = fig.get_axes()[0]
ax.set_title("Title", fontweight="bold", fontsize=20, fontname="Helvetica", ha="left", x=0, y=1.1)
# ax.set_title("Subtitle", fontsize=16, fontname="Helvetica", ha="left", x=0, y=1.0)

# Move caption to the left
caption = ax.get_children()[-1]

# Show the chart
plt.show()





####################################
import pandas as pd
import numpy as np
from plotnine import ggplot, aes, geom_tile, theme, element_text, element_rect, element_blank, element_line, scale_fill_gradient, labs, geom_text

# Sample data
data = {
    'x': np.repeat(np.arange(1, 6), 5),
    'y': np.tile(np.arange(1, 6), 5),
    'value': np.random.randint(1, 100, size=(25,))
}

df = pd.DataFrame(data)

# Define category names
x_categories = ['A', 'B', 'C', 'D', 'E']
y_categories = ['One', 'Two', 'Three', 'Four', 'Five']

# Assign category names
df['x'] = df['x'].apply(lambda x: x_categories[x - 1])
df['y'] = df['y'].apply(lambda y: y_categories[y - 1])

# Main blue color
main_blue = '#6B96C3'

# Very dark gray, almost black
very_dark_gray = '#1a1a1a'

# Lighter gray for the border
lighter_gray = '#b3b3b3'

# BBC style theme for plotnine
bbc_style_theme = theme(
    plot_title=element_text(family='Helvetica', size=20, face='bold', color=very_dark_gray, margin={'b': 10}, ha='left'),
    legend_position='none',
    axis_title=element_blank(),
    axis_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    axis_ticks=element_blank(),
    axis_line=element_blank(),
    panel_grid_minor=element_blank(),
    panel_grid_major_y=element_blank(),
    panel_grid_major_x=element_blank(),
    panel_background=element_rect(fill='white', color=lighter_gray, size=0.6),
    strip_background=element_rect(fill='white'),
    strip_text=element_text(size=22, hjust=0),
    plot_caption=element_text(ha='left', color=very_dark_gray, margin={'t': 10})
)

# Create the heatmap with the BBC style theme and main blue color
chart_bbc_style = (
    ggplot(df, aes(x='x', y='y', fill='value'))
    + geom_tile(color=lighter_gray, size=0.2)
    + geom_text(aes(label='value'), size=10, color=very_dark_gray)
    + scale_fill_gradient(low='white', high=main_blue)
    + labs(title="Title", caption="Footnote")
    + bbc_style_theme
)

# Show the chart
chart_bbc_style.draw()


#########################

import pandas as pd
from plotnine import ggplot, aes, geom_bar, theme, element_text, element_rect, element_blank, element_line, scale_y_continuous, coord_flip, labs
import matplotlib.pyplot as plt

# Sample data
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [25, 45, 15, 30, 35]
}

df = pd.DataFrame(data)

# Main blue color
main_blue = '#6B96C3'

# Very dark gray, almost black
very_dark_gray = '#1a1a1a'

# BBC style theme for plotnine
bbc_style_theme = theme(
    plot_title=element_text(family='Helvetica', size=20, face='bold', color=very_dark_gray, margin={'b': 10}, ha='left'),
    legend_position='top',
    legend_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    legend_background=element_blank(),
    legend_title=element_blank(),
    legend_key=element_blank(),
    axis_title=element_blank(),
    axis_text=element_text(family='Helvetica', size=16, color=very_dark_gray),
    axis_text_x=element_text(margin={'b': 10}),
    axis_ticks=element_blank(),
    axis_line=element_blank(),
    axis_line_x=element_line(color=very_dark_gray, size=1.2),
    axis_line_y=element_blank(),
    panel_grid_minor=element_blank(),
    panel_grid_major_y=element_line(color='#cbcbcb'),
    panel_grid_major_x=element_blank(),
    panel_background=element_blank(),
    strip_background=element_rect(fill='white'),
    strip_text=element_text(size=22, hjust=0),
    plot_caption=element_text(ha='left', color=very_dark_gray, margin={'t': 10})
)

# Create the bar chart with the BBC style theme and main blue color
chart_bbc_style = (
    ggplot(df, aes(x='Category', y='Value'))
    + geom_bar(stat='identity', fill=main_blue, width=0.7)
    + scale_y_continuous(expand=(0, 0), limits=(0, 50))
    + coord_flip()
    + labs(title="Title", y="Y Axis Title", caption="Footnote")
    + bbc_style_theme
)

# Move caption to the left
fig = chart_bbc_style.draw()
ax = fig.get_axes()[0]
caption = ax.get_children()[-1]
#caption.set_horizontalalignment('left')

# Show the chart
plt.show()

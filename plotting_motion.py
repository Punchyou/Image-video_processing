# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:39:04 2019

@author: Maria
"""

from difference_in_motion_detector import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type="datetime", height=100,
           width=500, responsive=True, title="Motion Graph")
#get rid of unnecessary values on the axis
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks=1

#quadrant graph
p.quad(left=df["Start"], right=["End"], bottom=0, top=1, color="green")

output_file("Graph.html")
show(p)
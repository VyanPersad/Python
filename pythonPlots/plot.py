from matplotlib import pyplot as plt
import numpy as np

def plotPie(data, label, title='Title', sub_title='Sub-title', sub_text='Sub-Text', print = 0, destFolder='', base_name=''):
    f, plot = plt.subplots(figsize=(9, 6)) 
    plot.pie(data, labels=label)
    plot.set_position([0.15,0.07,0.7,0.6])
    plt.suptitle(title, x=0.5, y=0.8)
    plt.title(sub_title,x=0.5, y=1.0)
    plt.figtext(0.1, 0.05, sub_text, ha='left', va='bottom')
    plt.tight_layout
    if (print==0):
        plt.show()
    elif(print==1):
        if (destFolder == ''):
            plt.savefig(f'{base_name}_pie_chart.png')
        else:
            plt.savefig(f'{destFolder}/{base_name}_pie_chart.png')
        plt.close(f)


cars = ['AUDI', 'BMW', 'FORD', 'TESLA', 'JAGUAR', 'MERCEDES']
data = [23, 17, 35, 29, 12, 41]

plotPie(data, cars,'A Simple Pie Chart', 'Sub-title', 'Sub-Text')
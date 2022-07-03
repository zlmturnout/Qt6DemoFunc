from cmath import e
import sys,time,datetime,math

# QT for python import
import PySide6
from PySide6.QtCore import QTimer, Slot, QThread, Signal, Qt,QTime
from PySide6.QtGui import QDoubleValidator, QIntValidator, QTextCursor,QPainter,QPixmap
from PySide6.QtWidgets import QWidget, QPushButton, QStyle, QFileDialog, QApplication, QMainWindow, QGridLayout, \
    QMessageBox
# Qt charts
from PySide6.QtCharts import QChartView,QLineSeries,QChart,QCategoryAxis,QValueAxis
from UI.Status_Flag_UI import Ui_Form
from resource.qpprcc import *


class StatusUpdater(QWidget,Ui_Form):
    """update status by value

    Args:
        QWidget (_type_): _description_
        Ui_Form (_type_): _description_
    """
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Status Updater')
        # initialize for data plot
        self.Data_dict={'x':[],'y':[]}
        self.DataSeries=QLineSeries()
        self.DataChart=QChart()
        self.DataChart.legend().hide()
        self.Axis_X=QValueAxis()
        self.Axis_Y=QValueAxis()
        self.DataChart.setTitle('Status Updater by Sin func')
        
        self.DataChartView=QChartView()
        # timer for plot event
        self.plot_timer=QTimer()
        self.start_t0=None
        self.plot_timer.timeout.connect(self.update_value)
        # input time step 
        self.Time_step_input.setValidator(QIntValidator(10,10000))
        
    def get_timestep(self):
        t_step=self.Time_step_input.text()
        print(t_step)
        return int(t_step)
    
    @Slot()
    def on_Start_plot_btn_clicked(self):
        self.Data_dict={'x':[],'y':[]}
        self.plot_timer.start(self.get_timestep())
        self.start_t0=time.time()
    
    @Slot()
    def update_value(self):
        """update date dict by Sin func
        y=f(x)=2Sin(PI*x/15)
        """
        t=time.time()-self.start_t0
        y=2*math.sin((math.pi)*t/0.1)+math.cos((math.pi)*t/0.2)
        self.Data_dict['x'].append(t)
        self.Data_dict['y'].append(y)
        # plot the x-y list
        self.plot_datalist(self.Data_dict['x'],self.Data_dict['y'])
        if y<0:
            self.label.setPixmap(QPixmap(u":/icons/icons/Status_red50px.png"))
        else:
            self.label.setPixmap(QPixmap(u":/icons/icons/Status_green50px.png"))
            
    
    def plot_datalist(self,x_list:list,y_list:list,xlabel:str='x',ylabel:str='y'):
        """Plot Sin func and update status by
        
        Args:
            x_list: example=[1,2,3]
            y_list: example=[2,4,8]
        """
        self.DataSeries.clear()
        self.DataChart.removeSeries(self.DataSeries)
        self.DataChart.removeAxis(self.Axis_X)
        self.DataChart.removeAxis(self.Axis_Y)
        min_X=0
        max_X=0
        min_Y=0
        max_Y=0
        # update all lineseries data
        for i,val in enumerate(y_list):
            max_Y=val if val>max_Y else max_Y
            min_Y=val if val<min_Y else min_Y
            max_X=x_list[i] if x_list[i]>max_X else max_X
            min_X=x_list[i] if x_list[i]<min_X else min_X
            self.DataSeries.append(x_list[i],val)
        # add lineseries into chart
        self.DataChart.addSeries(self.DataSeries)
        # for X axis
        self.Axis_X.setTitleText(xlabel)
        self.Axis_X.setRange(min_X-5,max_X+5)
        self.DataChart.addAxis(self.Axis_X,Qt.AlignBottom)
        self.DataSeries.attachAxis(self.Axis_X)
        
        # for Y axis
        self.Axis_Y.setTitleText(ylabel)
        self.Axis_Y.setRange(min_Y-1,max_Y+1)
        self.DataChart.addAxis(self.Axis_Y,Qt.AlignLeft)
        self.DataSeries.attachAxis(self.Axis_Y)
        #chartview to show plot
        self.DataChartView.setRenderHint(QPainter.Antialiasing)
        self.DataChartView.setChart(self.DataChart)
        self.gridLayout.addWidget(self.DataChartView,0,0)
            
    @Slot()
    def on_Stop_plot_btn_clicked(self):
        self.plot_timer.stop()
        #self.start_t0=time.time()
        
        


if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=StatusUpdater()
    win.show()
    sys.exit(app.exec())
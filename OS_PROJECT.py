# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 16:27:45 2020

@author: CKP
"""
import tkinter as tk
from functools import partial
class MainWindow:
    def __init__(self , root):
        self.root = root
        root.geometry("550x400+450+200")
        self.frame = tk.Frame(self.root)
        tk.Label(self.root , text ="SCHEDULING ALGORITHMS" , font ="verdana 14 bold").grid(padx=150)
        tk.Label(self.root,text="").grid()
        tk.Label(self.root,text="").grid()
        tk.Label(self.root,text="").grid()
        self.b1 = tk.Button(self.root , text = "Round Robin" ,font = "verdana 12 bold",bg = "yellow",width= 15,command = partial(self.roundrobin,"ROUND-ROBIN")).grid()
        tk.Label(self.root,text="").grid()
        self.b2 = tk.Button(self.root , text = "FCFS" , font = "verdana 12 bold",bg = "yellow" , width = 15,command = partial(self.roundrobin,"FCFS")).grid()
        tk.Label(self.root,text="").grid()
        self.b2 = tk.Button(self.root , text = "SJF" , font = "verdana 12 bold",bg = "yellow", width = 15,command = partial(self.roundrobin,"SJF")).grid()
        tk.Label(self.root,text="").grid()
        self.b2 = tk.Button(self.root , text = "SRTF" , font = "verdana 12 bold",bg = "yellow", width = 15,command = partial(self.roundrobin,"SRTF")).grid()
        tk.Label(self.root,text="").grid()
        self.b2 = tk.Button(self.root , text = "PS" , font = "verdana 12 bold",bg = "yellow", width = 15,command = partial(self.roundrobin,"PS")).grid()
        self.frame.grid()
    def roundrobin(self,algo):
        self.root.withdraw()
        self.rr = tk.Toplevel(self.root)
        bb = robin(self.root,self.rr,algo)
class robin:
    def __init__(self , root,rr,algo) :
        self.root = root
        self.rr = rr
        self.algo = algo
        rr.geometry("+450+200")
        self.frame = tk.Frame(self.rr)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr,text = "Processes",font = "verdana 10 bold").grid(row=1,column=0)
        tk.Label(self.rr,text= "Arrival Time",font = "verdana 10 bold").grid(row=1,column=1)
        tk.Label(self.rr,text= "  ").grid(row=1,column=2)
        tk.Label(self.rr,text = "Burst Time",font = "verdana 10 bold").grid(row=1,column=3)
        tk.Label(self.rr,text= "  ").grid(row=1,column=4)
        if "ROUND-ROBIN"==algo :
            tk.Label(self.rr,text= "Time Quantum",font = "verdana 10 bold").grid(row=1,column=5)
        if "PS" == algo :
            tk.Label(self.rr,text= "Priority",font = "verdana 10 bold").grid(row=1,column=5)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr , text = "P1",font=" verdana 10 bold").grid(row=3,column=0)
        self.a11 = tk.IntVar()
        self.a22= tk.IntVar()
        self.a33= tk.IntVar()
        self.a44= tk.IntVar()
        self.a55= tk.IntVar()
        self.b11= tk.IntVar()
        self.b22= tk.IntVar()
        self.b33= tk.IntVar()
        self.b44= tk.IntVar()
        self.b55= tk.IntVar()
        self.c11= tk.IntVar()
        self.p11 = tk.IntVar()
        self.p22 = tk.IntVar()
        self.p33 = tk.IntVar()
        self.p44 = tk.IntVar()
        self.p55 = tk.IntVar()
        
        self.a1 = tk.Entry(self.rr,textvariable=self.a11).grid(row=3,column=1)
        self.b1 = tk.Entry(self.rr,textvariable=self.b11).grid(row=3,column=3)
        if("ROUND-ROBIN"==algo):
            self.c1 = tk.Entry(self.rr,textvariable=self.c11).grid(row=3,column=5)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr , text = "P2",font=" verdana 10 bold").grid(row=5,column=0)
        self.a2 = tk.Entry(self.rr,textvariable=self.a22).grid(row=5,column=1)
        self.b2  = tk.Entry(self.rr,textvariable=self.b22).grid(row=5,column=3)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr , text = "P3",font=" verdana 10 bold").grid(row=7,column=0)
        self.a3 = tk.Entry(self.rr,textvariable=self.a33).grid(row=7,column=1)
        self.b3 = tk.Entry(self.rr,textvariable=self.b33).grid(row=7,column=3)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr , text = "P4",font=" verdana 10 bold").grid(row=9,column=0)
        self.a4 = tk.Entry(self.rr,textvariable=self.a44).grid(row=9,column=1)
        self.b4 = tk.Entry(self.rr,textvariable=self.b44).grid(row=9,column=3)
        tk.Label(self.rr,text= "").grid()
        tk.Label(self.rr , text = "P5",font=" verdana 10 bold").grid(row=11,column=0)
        self.a5 = tk.Entry(self.rr,textvariable=self.a55).grid(row= 11,column=1)
        self.b5 = tk.Entry(self.rr,textvariable=self.b55).grid(row=11,column=3)
        tk.Label(self.rr,text= "").grid()
        z=0
        self.choice = "HV"
        if "PS"==algo :
            self.p1 = tk.Entry(self.rr,textvariable=self.p11).grid(row=3,column=5)
            self.p2 = tk.Entry(self.rr,textvariable=self.p22).grid(row=5,column=5)
            self.p3 = tk.Entry(self.rr,textvariable=self.p33).grid(row=7,column=5)
            self.p4 = tk.Entry(self.rr,textvariable=self.p44).grid(row=9,column=5)
            self.p5 = tk.Entry(self.rr,textvariable=self.p55).grid(row=11,column=5)
            tk.Label(self.rr,text = "Priority According to :",font = "verdana 10 bold").grid(row=13,column=1)
            tk.Label(self.rr,text= "").grid()
            self.butt = tk.Button(self.rr,text = "Higher Value",command = partial(self.Choices,"HV")).grid(row=15,column=0)
            self.butt = tk.Button(self.rr,text = "Lower Value",command = partial(self.Choices,"LV")).grid(row=15,column=1)
            tk.Label(self.rr,text= "").grid()
            z = 5
        self.button1 = tk.Button(self.rr,text = "BACK",command = self.Back).grid(row=13+z,column=0)
        self.wt = tk.Button(self.rr,text = "CALCULATE",width=15,command = self.calculaterr).grid(row=13+z,column=1) 
        self.button1 = tk.Button(self.rr,text = "EXIT",command = self.clear).grid(row=13+z,column=2)
        self.frame.grid()
    def Choices(self,choice):
        self.choice = choice
        tk.Label(self.rr,text = "<---Request Approved--->",font = "verdana 10 ").grid(row = 17 ,column=1)
    def Back(self):
        self.rr.destroy()
        self.root.deiconify()
    def clear(self):
        self.rr.destroy()
        self.root.destroy()
    def calculaterr(self):
        self.rr.withdraw()
        self.calrr = tk.Toplevel(self.rr)
        self.calrr.geometry("+450+200")
        if(self.algo =="ROUND-ROBIN"):
            obj = RoundRobin(self.a11.get(),self.a22.get(),self.a33.get(),self.a44.get(),self.a55.get(),self.b11.get(),self.b22.get(),self.b33.get(),self.b44.get(),self.b55.get(),self.c11.get(),self.root,self.rr,self.calrr,self.algo)
            obj.processData()
        elif(self.algo == "FCFS"):
            obj = FCFS(self.a11.get(),self.a22.get(),self.a33.get(),self.a44.get(),self.a55.get(),self.b11.get(),self.b22.get(),self.b33.get(),self.b44.get(),self.b55.get(),self.root,self.rr,self.calrr,self.algo)
            obj.processData()
        elif(self.algo == "SJF"):
            obj = SJF(self.a11.get(),self.a22.get(),self.a33.get(),self.a44.get(),self.a55.get(),self.b11.get(),self.b22.get(),self.b33.get(),self.b44.get(),self.b55.get(),self.root,self.rr,self.calrr,self.algo)
            obj.processData()
        elif(self.algo == "SRTF"):
            obj = SRTF(self.a11.get(),self.a22.get(),self.a33.get(),self.a44.get(),self.a55.get(),self.b11.get(),self.b22.get(),self.b33.get(),self.b44.get(),self.b55.get(),self.root,self.rr,self.calrr,self.algo)
            obj.processData()
        elif(self.algo == "PS"):
            obj = PS(self.a11.get(),self.a22.get(),self.a33.get(),self.a44.get(),self.a55.get(),self.b11.get(),self.b22.get(),self.b33.get(),self.b44.get(),self.b55.get(),self.p11.get(),self.p22.get(),self.p33.get(),self.p44.get(),self.p55.get(),self.root,self.rr,self.calrr,self.algo,self.choice)
            obj.processData()
        return

class PS:
    def __init__(self,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,p1,p2,p3,p4,p5,root,rr,calrr,algo,choice):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.algo=algo
        self.p1=p1
        self.p2=p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.choice = choice
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1,2,3,4,5]
        arrival_time = [self.a1,self.a2,self.a3,self.a4,self.a5]
        burst_time = [self.b1,self.b2,self.b3,self.b4,self.b5]
        priority = [self.p1,self.p2,self.p3,self.p4,self.p5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i],burst_time[i],0,priority[i]])
            process_data.append(temporary)
            temporary=[]
        PS.schedulingProcess(self,process_data)
    def schedulingProcess(self,process_data):
        s_time = 0
        process_data.sort(key = lambda x : x[1])
        for i in range(5):
            ready_queue=[]
            normal_queue = []
            for j in range(5):
                if(process_data[j][1]<=s_time and process_data[j][3]==0):
                    ready_queue.append([process_data[j][0],process_data[j][1],process_data[j][2],process_data[j][4]])
                elif(process_data[j][3]==0):
                    normal_queue.append([process_data[j][0],process_data[j][1],process_data[j][2],process_data[j][4]])
            if len(ready_queue) != 0:
                if self.choice == "HV":
                    ready_queue.sort(key=lambda x: x[3], reverse=True)
                elif self.choice == "LV":
                    ready_queue.sort(key=lambda x: x[3])
                s_time = s_time + ready_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                s_time = s_time + normal_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
        t_time = PS.calculateTurnaroundTime(self, process_data)
        w_time = PS.calculateWaitingTime(self, process_data)
        d = Displaydata(self.root,self.rr,self.calrr,process_data,t_time,w_time,0,self.algo)
        d.Display()

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time


    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time
        
class SRTF:
    def __init__(self,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,root,rr,calrr,algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.algo=algo
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1,2,3,4,5]
        arrival_time = [self.a1,self.a2,self.a3,self.a4,self.a5]
        burst_time = [self.b1,self.b2,self.b3,self.b4,self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i],burst_time[i],0,burst_time[i]])
            process_data.append(temporary)
            temporary=[]
        SRTF.schedulingProcess(self, process_data)
    
    def schedulingProcess(self, process_data):
        start_time = []
        exit_time = []
        s_time = 0
        sequence_of_process = []
        process_data.sort(key=lambda x: x[1])
        while 1:
            ready_queue = []
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                ready_queue.sort(key=lambda x: x[2])
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(ready_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == ready_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:        
                    process_data[k][3] = 1
                    process_data[k].append(e_time)
            if len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                start_time.append(s_time)
                s_time = s_time + 1
                e_time = s_time
                exit_time.append(e_time)
                sequence_of_process.append(normal_queue[0][0])
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][2] = process_data[k][2] - 1
                if process_data[k][2] == 0:
                    process_data[k][3] = 1
                    process_data[k].append(s_time)
        t_time = SRTF.calculateTurnaroundTime(self, process_data)
        w_time = SRTF.calculateWaitingTime(self, process_data)
        d = Displaydata(self.root,self.rr,self.calrr,process_data,t_time,w_time,sequence_of_process,self.algo)
        d.Display()
        
    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / len(process_data)
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / len(process_data)
        return average_waiting_time

class FCFS:
    def __init__(self,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,root,rr,calrr,algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.algo=algo
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1,2,3,4,5]
        arrival_time = [self.a1,self.a2,self.a3,self.a4,self.a5]
        burst_time = [self.b1,self.b2,self.b3,self.b4,self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i],burst_time[i],0,0])
            process_data.append(temporary)
            temporary=[]
        FCFS.schedulingProcess(self, process_data)
    def schedulingProcess(self,process_data):
        start_time = []
        exit_time = []
        s_time=0
        process_data.sort(key=lambda x : x[1])
        for i in range(len(process_data)):
            start_time.append(s_time)
            s_time = s_time + process_data[i][2]
            exit_time.append(s_time)
            process_data[i].append(s_time)
        t_time = FCFS.calculateTurnaroundTime(self,process_data)
        w_time = FCFS.calculateWaitingTime(self,process_data)
        d = Displaydata(self.root,self.rr,self.calrr,process_data,t_time,w_time,0,self.algo)
        d.Display()
        
    def calculateTurnaroundTime(self,process_data):
        total_turnaround_time=0
        for i in range(5):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time
    
    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time
        
class SJF:
    
    def __init__(self,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,root,rr,calrr,algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.algo=algo
        
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1,2,3,4,5]
        arrival_time = [self.a1,self.a2,self.a3,self.a4,self.a5]
        burst_time = [self.b1,self.b2,self.b3,self.b4,self.b5]
        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i],burst_time[i],0,0])
            process_data.append(temporary)
            temporary=[]
        SJF.schedulingProcess(self, process_data)
        
    def schedulingProcess(self,process_data):
        s_time = 0
        process_data.sort(key = lambda x : x[1])
        for i in range(5):
            ready_queue = []
            normal_queue = []
            for j in range(5):
                if (process_data[j][1] <= s_time) and (process_data[j][3] == 0):
                    ready_queue.append([process_data[j][0], process_data[j][1], process_data[j][2]])
                elif process_data[j][3] == 0:
                    normal_queue.append([process_data[j][0], process_data[j][1], process_data[j][2]])
            if len(ready_queue)!=0:
                ready_queue.sort(key = lambda x : x[2])
                s_time = s_time + ready_queue[0][2]
                for k in range(5):
                    if ready_queue[0][0]==process_data[k][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
            elif len(ready_queue)==0:
                if normal_queue[0][1] > s_time :
                    s_time = normal_queue[0][1]
                s_time = s_time + normal_queue[0][2]
                for k in range(len(process_data)):
                    if process_data[k][0] == normal_queue[0][0]:
                        break
                process_data[k][3] = 1
                process_data[k].append(s_time)
        t_time = SJF.calculateTurnaroundTime(self, process_data)
        w_time = SJF.calculateWaitingTime(self, process_data)
        d = Displaydata(self.root,self.rr,self.calrr,process_data,t_time,w_time,0,self.algo)
        d.Display()
        
        
    def calculateTurnaroundTime(self,process_data):
        total_turnaround_time=0
        for i in range(5):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time
    
    
    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][2]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time
                    
    
class RoundRobin:

    def __init__(self,a1,a2,a3,a4,a5,b1,b2,b3,b4,b5,t,root,rr,calrr,algo):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3
        self.b4 = b4
        self.b5 = b5
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.algo=algo
        self.t = t
    def processData(self):
        process_data = []
        temporary = []
        process_id = [1,2,3,4,5]
        arrival_time = [self.a1,self.a2,self.a3,self.a4,self.a5]
        burst_time = [self.b1,self.b2,self.b3,self.b4,self.b5]

        for i in range(5):
            temporary.extend([process_id[i], arrival_time[i], burst_time[i], 0 ,burst_time[i]])
            process_data.append(temporary)
            temporary=[]
        time_slice =self.t
        RoundRobin.schedulingProcess(self, process_data, time_slice)

    def schedulingProcess(self, process_data, time_slice):
        start_time = []
        exit_time = []
        executed_process = []
        ready_queue = []
        s_time = 0
        process_data.sort(key=lambda x: x[1])
        while 1:
            normal_queue = []
            temp = []
            for i in range(len(process_data)):
                if process_data[i][1] <= s_time and process_data[i][3] == 0:
                    present = 0
                    if len(ready_queue) != 0:
                        for k in range(len(ready_queue)):
                            if process_data[i][0] == ready_queue[k][0]:
                                present = 1
                    if present == 0:
                        temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                        ready_queue.append(temp)
                        temp = []
                    if len(ready_queue) != 0 and len(executed_process) != 0:
                        for k in range(len(ready_queue)):
                            if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                                ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))
                elif process_data[i][3] == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    normal_queue.append(temp)
                    temp = []    
            if len(ready_queue) == 0 and len(normal_queue) == 0:
                break
            if len(ready_queue) != 0:
                if ready_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                    ready_queue.pop(0)
                elif ready_queue[0][2] <= time_slice:

                    start_time.append(s_time)
                    s_time = s_time + ready_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(ready_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == ready_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
                    ready_queue.pop(0)
            elif len(ready_queue) == 0:
                if s_time < normal_queue[0][1]:
                    s_time = normal_queue[0][1]
                if normal_queue[0][2] > time_slice:
                    start_time.append(s_time)
                    s_time = s_time + time_slice
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = process_data[j][2] - time_slice
                elif normal_queue[0][2] <= time_slice:
                    start_time.append(s_time)
                    s_time = s_time + normal_queue[0][2]
                    e_time = s_time
                    exit_time.append(e_time)
                    executed_process.append(normal_queue[0][0])
                    for j in range(len(process_data)):
                        if process_data[j][0] == normal_queue[0][0]:
                            break
                    process_data[j][2] = 0
                    process_data[j][3] = 1
                    process_data[j].append(e_time)
        t_time = RoundRobin.calculateTurnaroundTime(self,process_data)
        w_time = RoundRobin.calculateWaitingTime(self,process_data)
        d = Displaydata(self.root,self.rr,self.calrr,process_data, t_time, w_time, executed_process ,self.algo)
        d.Display()
        '''
        RoundRobin.printData(self, process_data, t_time, w_time, executed_process)
        '''

    def calculateTurnaroundTime(self, process_data):
        total_turnaround_time = 0
        for i in range(len(process_data)):
            turnaround_time = process_data[i][5] - process_data[i][1]
            total_turnaround_time = total_turnaround_time + turnaround_time
            process_data[i].append(turnaround_time)
        average_turnaround_time = total_turnaround_time / 5
        return average_turnaround_time

    def calculateWaitingTime(self, process_data):
        total_waiting_time = 0
        for i in range(len(process_data)):
            waiting_time = process_data[i][6] - process_data[i][4]
            total_waiting_time = total_waiting_time + waiting_time
            process_data[i].append(waiting_time)
        average_waiting_time = total_waiting_time / 5
        return average_waiting_time
class Displaydata:
    def __init__(self,root,rr,calrr,p,t,w,e,algo):
        self.root = root
        self.rr = rr
        self.calrr = calrr
        self.process_data = p
        self.t_time = t
        self.w_time = w
        self.executed_process = e
        self.algo = algo
    def Display(self):
        self.process_data.sort(key=lambda x: x[0])
        tk.Label(self.calrr,text = " ").grid(row=0,column=0)
        tk.Label(self.calrr,text = "PROCESSES").grid(row=1,column=0)
        tk.Label(self.calrr,text = "COMPLETION TIME   ").grid(row=1,column=1)
        tk.Label(self.calrr,text = "TURN AROUND TIME  ",font = "verdana 11 ").grid(row=1,column=2)
        tk.Label(self.calrr,text = "WAITING TIME",font = "verdana 11 ").grid(row=1,column=3)
        tk.Label(self.calrr,text = " ").grid(row=2,column=0)
        tk.Label(self.calrr,text="P1 :",font = "verdana 10 ").grid(row=3,column=0)
        tk.Label(self.calrr,text=self.process_data[0][5],font = "verdana 10 bold").grid(row=3,column=1)
        tk.Label(self.calrr,text=self.process_data[0][6],font = "verdana 10 bold").grid(row=3,column=2)
        tk.Label(self.calrr,text=self.process_data[0][7],font = "verdana 10 bold").grid(row=3,column=3)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text="P2 :",font = "verdana 10 ").grid(row=5,column=0)
        tk.Label(self.calrr,text=self.process_data[1][5],font = "verdana 10 bold").grid(row=5,column=1)
        tk.Label(self.calrr,text=self.process_data[1][6],font = "verdana 10 bold").grid(row=5,column=2)
        tk.Label(self.calrr,text=self.process_data[1][7],font = "verdana 10 bold").grid(row=5,column=3)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text="P3 :",font = "verdana 10 ").grid(row=7,column=0)
        tk.Label(self.calrr,text=self.process_data[2][5],font = "verdana 10 bold").grid(row=7,column=1)
        tk.Label(self.calrr,text=self.process_data[2][6],font = "verdana 10 bold").grid(row=7,column=2)
        tk.Label(self.calrr,text=self.process_data[2][7],font = "verdana 10 bold").grid(row=7,column=3)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text="P4 :",font = "verdana 10 ").grid(row=9,column=0)
        tk.Label(self.calrr,text=self.process_data[3][5],font = "verdana 10 bold").grid(row=9,column=1)
        tk.Label(self.calrr,text=self.process_data[3][6],font = "verdana 10 bold").grid(row=9,column=2)
        tk.Label(self.calrr,text=self.process_data[3][7],font = "verdana 10 bold").grid(row=9,column=3)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text="P5 :",font = "verdana 10 ").grid(row=11,column=0)
        tk.Label(self.calrr,text=self.process_data[4][5],font = "verdana 10 bold").grid(row=11,column=1)
        tk.Label(self.calrr,text=self.process_data[4][6],font = "verdana 10 bold").grid(row=11,column=2)
        tk.Label(self.calrr,text=self.process_data[4][7],font = "verdana 10 bold").grid(row=11,column=3)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text = "AVG. TURN-AROUND TIME :",font = "verdana 10").grid(row=13,column=0)
        tk.Label(self.calrr,text = self.t_time,font = "verdana 10 bold").grid(row=13,column = 1)
        tk.Label(self.calrr,text = " ").grid()
        tk.Label(self.calrr,text = "AVG. WAITING TIME     :",font = "verdana 10").grid(row=15,column=0)
        tk.Label(self.calrr,text = self.w_time,font = "verdana 10 bold").grid(row=15,column=1)
        tk.Label(self.calrr,text = " ").grid()
        if(self.algo == "ROUND-ROBIN" or self.algo == "SRTF"):
            tk.Label(self.calrr,text = "PROCESS SEQUENCE      :",font = "verdana 10").grid(row=17,column=0)
            tk.Label(self.calrr,text = str(self.executed_process),font = "verdana 10 bold").grid(row=17,column=1)
            tk.Label(self.calrr,text = " ").grid()
        self.b1 = tk.Button(self.calrr , text = "BACK TO MENU" ,font = "verdana 11 ",width= 15,command = self.BackMenu).grid(row=19,column=0)
        tk.Label(self.root,text="").grid()
        self.b1 = tk.Button(self.calrr , text = "BACK TO {}".format(self.algo),font = "verdana 11 ",width= 18,command = self.Back).grid(row=19,column=1)
        tk.Label(self.root,text="").grid()
        self.b1 = tk.Button(self.calrr , text = "EXIT" ,font = "verdana 11",width= 15,command = self.EXIT).grid(row=19,column=2)
        tk.Label(self.root,text="").grid()
    def Back(self):
        self.calrr.destroy()
        self.rr.deiconify()
        
    def EXIT(self):
        self.calrr.destroy()
        self.rr.destroy()
        self.root.destroy()
        
    def BackMenu(self):
        self.calrr.destroy()
        self.rr.destroy()
        self.root.deiconify()
if __name__ == "__main__":
    root=tk.Tk()
    b = MainWindow(root)
    root.mainloop()
    
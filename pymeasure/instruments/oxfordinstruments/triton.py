import socket
<<<<<<< HEAD

class Triton():
    
    """ Allows user to control Magnet power and temperature controller via the Triton control software"""
    
    def connect(self):
        edsIP = "localhost"
        edsPORT = 33576
        MESSAGE = b'SET:DEV:UID:VRM:MEAS:ENAB:\r\n'
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.settimeout(20) # 3 second timeout on commands
        self.srvsock.connect((edsIP, edsPORT))
        
=======
from time import sleep

class Triton():
    edsPORT = 33576
    edsIP = "localhost"
    srvsock = None
    """ Allows user to control Magnet power and temperature controller via the Triton control software"""
    
    def connect(self, edsIP = "localhost"):
        self.edsIP = edsIP
        MESSAGE = b'SET:DEV:UID:VRM:MEAS:ENAB:\r\n'
        self.srvsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsock.settimeout(20) # 3 second timeout on commands
        self.srvsock.connect((self.edsIP, self.edsPORT))
        
    def disconnect(self):
        if(self.srvsock is not None):
            self.srvsock.close()
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
## Magnet


    def get_Bfield(self): #This will get the magnetic field in xyz coordinates, will output float of z magnetic field#
        self.srvsock.sendall(b'READ:SYS:VRM:VECT\r\n')
        data = self.srvsock.recv(4096)
<<<<<<< HEAD
        data = float(data[35:-3])
        return (data)
    
=======
        print(data)
        data = float(data[35:-3])
        return (data)
    
    def get_setpoint(self):
        self.srvsock.sendall(b'READ:SYS:VRM:VSET\r\n')
        data = self.srvsock.recv(4096)
        return (data)
    
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
    def get_swprate(self): #This will get the sweep rate#
        self.srvsock.sendall(b'READ:SYS:VRM:RFST\r\n')
        data = self.srvsock.recv(4096)
        return (data)
    
    def get_current(self): #This returns the instanteous current in vrm#
        self.srvsock.sendall(b'READ:SYS:VRM:MCUR\r\n')
        data = self.srvsock.recv(4096)
        return (data)
    
<<<<<<< HEAD
=======
    def get_current_control(self):
        self.srvsock.sendall(b'READ:SYS:VRM:CURR\r\n')
        data = self.srvsock.recv(4096)
        data = float(data[35:-3])
        return (data)
    
    def get_status(self):
        self.srvsock.sendall(b'READ:SYS:VRM:ACTN\r\n')
        data = self.srvsock.recv(4096)
        return (data)
    
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
    def set_poc_on(self): #Turns persistent on completion on
        self.srvsock.sendall(b'SET:SYS:VRM:POC:ON\r\n')
        data = self.srvsock.recv(4096)
        
    def set_poc_off(self): #Turns persistent on completion mode off
        self.srvsock.sendall(b'SET:SYS:VRM:POC:OFF\r\n')
        data = self.srvsock.recv(4096)
        
    def set_swpto_asap(self,bf): #sets sweep rate to asap#
<<<<<<< HEAD
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:ASAP:VSET[0 0 %a]\r\n' % bf )
        data = self.srvsock.recv(4096)
        
    def set_swprate_rate(self,rate,bf):
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:RATE:RATE:%a:VSET[0 0 %a]\r\n' % rate, bf )
        data = self.srvsock.recv(4096)
        
    def set_swprate_time(self,time,bf):
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:TIME:TIME:%a:VSET[0 0 %a]\r\n' % time, bf )
        data = self.srvsock.recv(4096)
        
    def set_bfield(self,bf):
        self.srvsock.sendall(b'SET:SYS:VRM:VSET:[0 0 %a]\r\n' % bf)
        data = self.srvsock.recv(4096)
=======
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:ASAP:VSET:[0 0 %a]\r\n' % bf )
        data = self.srvsock.recv(4096)
        
    def set_swprate_rate(self,rate,bf):
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:RATE:RATE:%a:VSET:[0 0 %a]\r\n' % rate, bf )
        data = self.srvsock.recv(4096)
        
    def set_swprate_time(self,time,bf):
        self.srvsock.sendall(b'SET:SYS:VRM:RVST:MODE:TIME:TIME:%a:VSET:[0 0 %a]\r\n' % time, bf )
        data = self.srvsock.recv(4096)
        
    # def set_bfield(self,bf): #non-functional use set_swpto_asap
    #     self.srvsock.sendall(b'SET:SYS:VRM:VSET:[0 0 %a]\r\n' % bf)
    #     data = self.srvsock.recv(4096)
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
        
    def goto_set(self):
        self.srvsock.sendall(b'SET:SYS:VRM:ACTN:RTOS\r\n')
        data = self.srvsock.recv(4096)
<<<<<<< HEAD
        
=======

    def is_idle(self):
        return self.get_status() == b'STAT:SYS:VRM:ACTN:IDLE\n'

    def goto_bfield(self, bfield, sweeprate = None, wait=False, log=None):
        if(not self.is_idle()):
            if(log != None):
                log.info('Waiting for magnet controller to be idle.')
            while(self.get_status() != b'STAT:SYS:VRM:ACTN:IDLE\n'):
                sleep(1)
            if(log != None):
                log.info('Magnet controller is now idle.')

        if(not self.isWithin(self.get_Bfield(), bfield, 0.001)):
            if(log != None):
                log.info("Starting B field sweep.")
            if(sweeprate is None):
                self.set_swpto_asap(bfield)
            else:
                self.set_swprate_rate(sweeprate, bfield)
            self.goto_set() 
            if(wait):
                sleep(1)
                while(not self.is_idle()):
                    sleep(1)
        else:
            if(log != None):
                log.info("B field already stable at correct value, proceeding.")

>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
    def goto_zero(self):
        self.srvsock.sendall(b'SET:SYS:VRM:ACTN:RTOZ\r\n')
        data = self.srvsock.recv(4096)

    def set_persistent_on(self):
        self.srvsock.sendall(b'SET:SYS:ACTN:PERS\r\n')
        data = self.srvsock.recv(4096)
       
    def set_persistent_off(self):
        self.srvsock.sendall(b'SET:SYS:ACTN:NPERS\r\n')
  
<<<<<<< HEAD

=======
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
## Temperature control

    def get_temp_T8(self): #This will get the temperature reading from the RuO thermometer, for use below 1.2K#
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
        data = self.srvsock.recv(4096)
        data = float(data[26:-2])
        return (data)
    
    def get_res_T8(self):
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:RES\r\n')
        data = self.srvsock.recv(4096)
        data = float(data[26:-4])
        return (data)
    
<<<<<<< HEAD
    
=======
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922
    def get_temp_T5(self): #This will get the temmperature reading from the Cernox thermometer, for use above 1.2K#
        self.srvsock.sendall(b'READ:DEV:T5:TEMP:SIG:TEMP\r\n')
        data = self.srvsock.recv(4096)
        data = float(data[26:-2])
        return (data)
    
    def get_tset_T8(self): #This will get the temperature set point#
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:LOOP:TSET\r\n')
        data = self.srvsock.recv(4096)
        data = float(data[26:-2])
        return (data)
        
    def get_sweeprate(self): #Temperature sweep rate, to use must also turn on the rate#
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:RAMP:RATE\r\n')
        data = self.srvsock.recv(4096)
        
        ### Set Functions ###
        
    def set_temp_channel(self,channel): #used to manually change the channel used in the PID feedback loop, this will automatically change at 1.2 to the channel 5#
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:LOOP:CHAN:%a\r\n' % channel )
        data = self.srvsock.recv(4096)

    def set_PID_on(self):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:MODE:ON\r\n')
        data = self.srvsock.recv(4096)
    
    def set_PID_off(self):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:MODE:OFF\r\n')
        data = self.srvsock.recv(4096)
    
    def set_heater_range(self,htrrange):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RANGE:%a\r\n' % htrrange )
        data = self.srvsock.recv(4096)
        
    def set_temp(self,tset):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:TSET:%a\r\n' % tset )
        self.srvsock.recv(4096)
        
    def set_ramprate(self,ramprate):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:RATE:%a\r\n' % ramprate )
        data = self.srvsock.recv(4096)
    
    def set_ramp_on(self):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:ENAB:ON\r\n')
        data = self.srvsock.recv(4096)
        
    def set_ramp_off(self):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:ENAB:OFF\r\n')
        data = self.srvsock.recv(4096)
        
    ### Multi step functions ###
    
    def intialize_tempset_default(self,maxtemp):
        #PID Settings
        if maxtemp < 1.2:
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:P:15\r\n')
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:I:120\r\n')
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:D:0\r\n')
        else:
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:P:3\r\n')
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:I:10\r\n')
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:D:0\r\n')
        #Heater range
        if maxtemp < 1:
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RANGE:10\r\n')
        else:
            self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RANGE:3.16\r\n')
        if maxtemp > 2:
            print('Switch off the turbo, switch off the still heater, close V9, open V4, change channel to T5')
        
    def set_temp_wait_1(self,tset,delta = 0.01):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:TSET:%a\r\n' % tset )
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
        temp = self.srvsock.recv(4096)
        temp = float(data[26:-2])
        if (temp < tset-delta or temp > tset+delta):
            sleep(5)
            self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
            temp = self.srvsock.recv(4096)
            temp = float(temp[26:-2])
        sleep(60)
        
    def set_temp_wait_2(self,tset,delta = 0.01):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:TSET:%a\r\n' % tset )
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
        temp1 = self.srvsock.recv(4096)
        temp1 = float(data[26:-2])
        sleep(30)
        self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
        temp2 = self.srvsock.recv(4096)
        temp2 = float(data[26:-2])
        if (abs(temp1 - temp2) > delta):
            temp2 = temp1
            sleep(30)
            self.srvsock.sendall(b'READ:DEV:T8:TEMP:SIG:TEMP\r\n')
            temp1 = self.srvsock.recv(4096)
            temp1 = float(data[26:-2])
    
    def to_base(self):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:ENAB:OFF\r\n')
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RANGE:0\r\n')
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:MODE:OFF\r\n')
        
    def init_temp_swp(self,tempi,ramprate,htr):
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:MODE:OFF\r\n')
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:TSET:%a\r\n' % tempi )
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:RATE:%a\r\n' % ramprate )
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RAMP:ENAB:ON\r\n')
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:RANGE:%a\r\n' % htr )
        self.srvsock.sendall(b'SET:DEV:T8:TEMP:LOOP:MODE:ON\r\n')
<<<<<<< HEAD
=======

    def isWithin(self, have, want, range):
        return want - range <= have <= want + range
>>>>>>> fac2b4bb9f1e7a2a168a52f89e2db10e4a755922

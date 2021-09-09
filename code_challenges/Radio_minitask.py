# Making a Radio class

class Radio:
    
    color = 'brown'
    brand = 'Philips'
    ACPower = False
    headphone = False
    
    def __init__(self):
        self.power_led = "ON"
        self.mode_led = None
        self.frequency = 0.0
        self.volume = 0
        print("Your Radio is Ready to be Played")
        
        #Instance method
    def power_switch(self,power_status):
        self.power_led = power_status
        print("Your Radio Power is " + str(self.power_led))
            
    def mode_switch(self,mode_status):
        self.mode_led = mode_status
        print("Your Radio mode is set to " + str(self.mode_led))
            
    def band_tuner(self,freq_value):
        self.frequency = freq_value
        print("Your Radio Frequency is set to " + str(self.frequency))
            
    def volume_tuner(self,vol_value):
        self.volume = vol_value
        print("Your Radio volume is set to " + str(self.volume))
            
my_radio = Radio()
print("The color of my Radio = " + str(Radio.color))
print("The brand of my Radio = " + str(Radio.brand))

my_radio.power_switch("ON")
my_radio.mode_switch("FM")
my_radio.band_tuner(102.2)
my_radio.volume_tuner(8)

my_radio.power_switch("OFF")
my_radio = None
            
            
            
            


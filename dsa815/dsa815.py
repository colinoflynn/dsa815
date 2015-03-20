
#Install pyvisa, use easy_install for example:
#easy_install pyvisa
import visa

class DSA815(object):
    def __init__(self):
        pass

    def conn(self, constr="USB0::0x1AB1::0x0960::DSA8Axxxxxxx::INSTR"):
        """Attempt to connect to instrument"""
        self.inst = visa.instrument(constr)

    def identify(self):
        """Return identify string which has serial number"""
        return self.inst.ask("*IDN?")

    def TG_enable(self, state):
        if state:
            tstate = "1"
        else:
            tstate = "0"

        self.inst.write(":OUTput:STATe %s\n"%tstate)

    def TG_amp(self, amp):
        """Set the TG output amplitude power in dBm"""

        if amp > 0 or amp < -20:
            raise ValueError("Amplitude outside of allowed range -20dBm to 0dBm")
        
        self.inst.write(":SOUR:POW:LEV:IMM:AMPL %d\n"%amp)

    def set_span(self, span):
        self.inst.write(":SENS:FREQ:SPAN %d\n"%span)

    def set_centerfreq(self, freq):        
        self.inst.write(":SENS:FREQ:CENT %d\n"%int(freq))

    def dis(self):
        del self.inst

        
if __name__ == '__main__':
    test = DSA815()

    #Insert your serial number here / confirm via Ultra Sigma GUI
    test.conn("USB0::0x1AB1::0x0960::DSA8Axxxxxx::INSTR")

    print "Identity string:\n  %s"%test.identify()

    print "Turning TG on, setting frequency"
    test.TG_enable(True)
    test.set_span(0)
    test.set_centerfreq(10E6)
    

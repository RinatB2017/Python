#!/usr/bin/env python3
import hexdump
import time
from greatfet import GreatFET

def reset(gf, reset_pin):
    reset_pin.low()
    time.sleep(0.001)
    reset_pin.high()
    time.sleep(0.001)


def main():
    gf = GreatFET()
    reset_pin = gf.gpio.get_pin('J1_P4')
    prog_pin = gf.gpio.get_pin('J1_P6')

    # Reset is active low
    reset_pin.high()

    # Enter prog mode
    prog_pin.high()
    time.sleep(0.01)
    reset(gf, reset_pin)

    # ...

if __name__ == '__main__':
    main()
    

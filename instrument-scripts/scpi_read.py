"""
Simple read through SCPI

Requires PyVISA, PyVISA-py
pip install pyvisa
pip install pyvisa-py

Confirm proper PyVISA-py installation with
python -m visa info

If using a USB resource, requires PyUSB which in turn requires USB driver library such as libusb 1.0

pip intall pyusb
brew install libusb
may need to restart terminal/computer after libusb installation
"""

# import package
import pyvisa
#import argparse

# known instruments
# we expect all SCPI-enabled instruments to accept the same basic commands, but we can use this list to assign an instrument type
supported_dmms = ["MODEL DMM6500", "DMM6500"]
supported_oscs = ["MODEL MSO4104", "MSO4104"]

dmms = []
oscs = []

# parser = argparse.ArgumentParser('Read value from an Instrument')
# parser.add_argument("--instrument", type=str, help="select an instrument. options: 'dmm', 'osc'")
# parser.add_argument("--function", type=str, help="function for instrument read. examples: voltage, current, resistance")

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

def initializeInstruments():
    if len(resources) == 0:
        print("No resources found")
        return

    for counter in range(len(resources)):
        print("Connecting to resource "+str(counter)+": " + resources[counter])

        if "USB" in resources[counter]: 
            current_resource = rm.open_resource(resources[counter])
            print("Connected to: " + current_resource.query("*IDN?"))
            if current_resource.query("*IDN?").split(",")[1] in supported_dmms:
                print("Resource "+str(counter)+" is a supported DMM")
                dmms.append(current_resource)

            elif current_resource.query("*IDN?").split(",")[1] in supported_oscs:
                print("Resource "+str(counter)+" is a supported oscilliscope")
                oscs.append(current_resource)

            else:
                print("Resource "+ current_resource+ " isn't a supported DMM or oscilliscope")
        else:
            print(resources[counter]+" isn't a USB device. Can't connect.")
    
    # inst.write("*rst; status:preset; *cls")

def queryValue(instrumentType, function):
    if instrumentType == "dmm":
        if function == "voltage":
            # TODO need to fix later so it doesn't just take the first instrument 
            value = float(dmms[0].query(':MEASure:VOLTage:DC?'))
            print("Measured value = " + str(value) + " VDC")
            return value

    elif instrumentType == "osc":
        if function == "voltage":
            # TODO need to fix later so it doesn't just take the first instrument 
            value = float(oscs[0].query(':MEASure:VOLTage:DC?'))
            print("Measured value = " + str(value) + " VDC")
            return value

    else:
        print("Invalid instrument type provided to queryValue")
        return

def main():
    initializeInstruments()
    queryValue("dmm", "voltage")
    for i in range(200):
        value = float(dmms[0].query(':MEASure:VOLTage:DC?'))
        print(value)
        

if __name__ == "__main__":
    # args = parser.parse_args()
    #main(args)
    main()

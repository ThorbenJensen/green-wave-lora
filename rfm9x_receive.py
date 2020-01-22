import board
import busio
import digitalio

import adafruit_rfm9x

# Define radio parameters.
RADIO_FREQ_MHZ = 868.0  # Frequency of the radio in Mhz. Must match your
                        # module! Can be a value like 915.0, 433.0, etc.

CS = digitalio.DigitalInOut(board.CE1)
RESET = digitalio.DigitalInOut(board.D25)
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
rfm9x = adafruit_rfm9x.RFM9x(spi, CS, RESET, RADIO_FREQ_MHZ)

while True:
    packet = rfm9x.receive()
    # Optionally change the receive timeout from its default of 0.5 seconds:
    #packet = rfm9x.receive(timeout=5.0)
    # If no packet was received during the timeout then None is returned.
    if packet is None:
        # Packet has not been received
        print('Received nothing! Listening again...')
    else:
        # Received a packet!
        # Print out the raw bytes of the packet:
        print('Received (raw bytes): {0}'.format(packet))
        packet_text = str(packet, 'ascii')
        print('Received (ASCII): {0}'.format(packet_text))
        [green, seconds_left, seconds_total] = packet_text.split(";")
        print("green:", green)
        print("seconds left:", seconds_left)
        print("seconds total:", seconds_total)
        # Also read the RSSI (signal strength) of the last received message and
        # print it.
        rssi = rfm9x.rssi
        print('Received signal strength: {0} dB'.format(rssi))

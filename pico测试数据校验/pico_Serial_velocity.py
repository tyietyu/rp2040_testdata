import time
import serial


ser = serial.Serial(
    port='COM7',
    baudrate=921600,
    timeout=1,
)

try:
    ser.flushInput()

    start_time = time.time()
    TOTAL_BYTES_RECEIVED = 0

    while time.time() - start_time < 10:
        data = ser.read(ser.in_waiting or 1)
        TOTAL_BYTES_RECEIVED += len(data)

    end_time = time.time()

    total_time = end_time - start_time
    speed_bps = TOTAL_BYTES_RECEIVED * 8 / total_time
    speed_kBps = speed_bps / 8 / 1_000
    print(f"Data received: {TOTAL_BYTES_RECEIVED} bytes")
    print(f"Time elapsed: {total_time:.2f} seconds")
    print(f"Speed: {speed_kBps:.3f} KB/s")

finally:
    ser.close()
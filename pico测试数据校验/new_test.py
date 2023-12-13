import time
import serial
import re

ser = serial.Serial(
    port='COM7',      # 串口号
    baudrate=921600,  # 波特率
    bytesize=serial.EIGHTBITS,  # 数据位
    parity=serial.PARITY_NONE,  # 校验位
    stopbits=serial.STOPBITS_ONE,  # 停止位
    timeout=None  # 读取超时设置
)

# 定义标准数据帧
standard_frame = (
    "00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F "
    "10 11 12 13 14 15 16 17 18 19 1A 1B 1C 1D 1E 1F "
    "20 21 22 23 24 25 26 27 28 29 2A 2B 2C 2D 2E 2F "
    "30 31 32 33 34 35 36 37 38 39 3A 3B 3C 3D 3E 3F "
    "40 41 42 43 44 45 46 47 48 49 4A 4B 4C 4D 4E 4F "
    "50 51 52 53 54 55 56 57 58 59 5A 5B 5C 5D 5E 5F "
    "60 61 62 63 64 65 66 67 68 69 6A 6B 6C 6D 6E 6F "
    "70 71 72 73 74 75 76 77 78 79 7A 7B 7C 7D 7E 7F "
    "80 81 82 83 84 85 86 87 88 89 8A 8B 8C 8D 8E 8F "
    "90 91 92 93 94 95 96 97 98 99 9A 9B 9C 9D 9E 9F "
    "A0 A1 A2 A3 A4 A5 A6 A7 A8 A9 AA AB AC AD AE AF "
    "B0 B1 B2 B3 B4 B5 B6 B7 B8 B9 BA BB BC BD BE BF "
    "C0 C1 C2 C3 C4 C5 C6 C7 C8 C9 CA CB CC CD CE CF "
    "D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 DA DB DC DD DE DF "
    "E0 E1 E2 E3 E4 E5 E6 E7 E8 E9 EA EB EC ED EE EF "
    "F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 FA FB FC FD FE FF "
).split()
def print_frame_in_blocks(frame_hex, block_size=16):
    for i in range(0, len(frame_hex), block_size):
        print(' '.join(frame_hex[i:i + block_size]))
        
def read_and_process_frames(duration):
    start_time = time.time()
    buffer = ''

    while time.time() - start_time < duration:
        if ser.in_waiting:
            # 读取串口中的所有数据
            data = ser.read(ser.in_waiting)
            # 将字节数据转换为十六进制字符串，并在每个字节之间添加空格
            data_hex = ' '.join('{:02X}'.format(b) for b in data)
            # 累积到缓冲区
            buffer += data_hex

            # 在数据的末尾追加空格以匹配单个字节
            buffer += ' '

            # 使用正则表达式匹配数据帧
            pattern = r'00 (?:[0-9A-F]{2} ){254}FF '
            matches = list(re.finditer(pattern, buffer))

            # 如果找到匹配的帧，移除这些帧并处理剩余的缓冲区
            if matches:
                last_match_end = matches[-1].end()
                for match in matches:
                    frame = match.group(0)
                    # 检查是否与标准帧匹配
                    if frame.strip() != ' '.join(standard_frame):
                        print("Problematic frame found:")
                        print_frame_in_blocks(frame.strip().split(' '))
                # 保留未处理的数据
                buffer = buffer[last_match_end:]

            frame_errors = []  # Declare an empty list to store problematic frames

            if frame_errors:
                print(f"Found {len(frame_errors)} problematic frame(s):")
                for index, frame in enumerate(frame_errors, 1):
                    print(f"Frame {index}:")
                    print_frame_in_blocks(frame)


try:
    read_and_process_frames(duration=20)  # 读取时间设定为10秒
finally:
    ser.close()  # 关闭串口连接

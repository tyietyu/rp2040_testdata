clear serialPort;
clc; clear all; close all;

serialPort = serialport("COM7", 115200);  %921600
tic;
data = read(serialPort,257, "uint8");
count = 1;
if isequal(data(1),data(257))
end
while(1)
    data(1) = data(257);
    data(2:257) = read(serialPort,256, "uint8");
    if ~isequal(data(1),data(257))
        error("data lost");
    end
    t = toc;
    count = count+1;
    speed = (count * 256 + 1)/t/1000;
    disp(speed);
end


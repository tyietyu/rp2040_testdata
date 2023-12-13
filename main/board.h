#include "hardware/uart.h"
#include "hardware/gpio.h"
#include "hardware/spi.h"

#define TIMER_INDEX 0
#define TIMER_INTERVAL_MS 20000  //10s
#define IRQ_PIN 5

#define LED0_PIN 25
#define LED1_PIN 24

#define UART_ID uart0
#define BAUD_RATE 921600
#define UART_RX_PIN 17
#define UART_TX_PIN 16

#define SPI_FACE spi_default


void radar_gpio_init();
void radar_uart_init();

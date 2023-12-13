#ifndef __RP2040_CLOCK_H
#define __RP2040_CLOCK_H

#include <stdio.h>
// #include "pico/stdlib.h"
#include "hardware/pll.h"
#include "hardware/clocks.h"
#include "hardware/structs/pll.h"
#include "hardware/structs/clocks.h"

/**
 * @brief config system clock to 133Mhz, usb clock to 48Mhz
 *
 * @param[void] null
 * @return null
 */
void rp2040_clock_133Mhz(void);

/**
 * @brief get current system clock.
 *
 * @param[void] null
 * @return current system clock num like 133000 kHz
 */
uint rp2040_get_sys_clock(void);

#endif // __RP2040_CLOCK_H
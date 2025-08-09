/*
 * led.c
 *
 *  Created on: Aug 9, 2025
 *      Author: Laptop
 */
#include "led.h"
#include "stm32g0xx_hal.h"

#define PIN_LED      GPIOB, GPIO_PIN_9

void led_on()
{
	HAL_GPIO_WritePin(PIN_LED, GPIO_PIN_SET);
}

void led_off()
{
	HAL_GPIO_WritePin(PIN_LED, GPIO_PIN_RESET);
}

/*
 * button.c
 *
 *  Created on: Aug 9, 2025
 *      Author: Laptop
 */
#include "button.h"
#include "stm32g0xx_hal.h"

#define PIN_BTN_LEFT      GPIOA, GPIO_PIN_2
#define PIN_BTN_RIGHT     GPIOA, GPIO_PIN_4

bool button_leftPressed()
{
	return (HAL_GPIO_ReadPin (PIN_BTN_LEFT) == GPIO_PIN_RESET);
}

bool button_rightPressed()
{
	return (HAL_GPIO_ReadPin (PIN_BTN_RIGHT) == GPIO_PIN_RESET);
}

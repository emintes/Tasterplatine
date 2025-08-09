/*
 * servo.c
 *
 *  Created on: Aug 9, 2025
 *      Author: Laptop
 */
#include "servo.h"
#include "stm32g0xx_hal.h"

extern TIM_HandleTypeDef htim3;

void servo_init()
{
	servo_setPosition(SERVO_POS_MIDDLE);
	HAL_TIM_PWM_Start(&htim3, TIM_CHANNEL_1);
}

void servo_setPosition(uint32_t position)
{
	TIM3->CCR1 = position;
}

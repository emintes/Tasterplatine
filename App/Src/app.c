/*
 * app.c
 *
 *  Created on: Aug 9, 2025
 *      Author: Laptop
 */
#include "app.h"
#include "button.h"
#include "led.h"
#include "servo.h"

void app_init()
{
	servo_init();
}

void app_run()
{
	if(button_leftPressed())
	{
		led_on();
		servo_setPosition(SERVO_POS_LEFT);
	}
	else if(button_rightPressed())
	{
		led_on();
		servo_setPosition(SERVO_POS_RIGHT);
	}
	else  //if no button is pressed
	{
		led_off();
		servo_setPosition(SERVO_POS_MIDDLE);
	}
}

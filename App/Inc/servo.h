/*
 * servo.h
 *
 *  Created on: Aug 9, 2025
 *      Author: Laptop
 */

#define SERVO_POS_LEFT 		1900
#define SERVO_POS_MIDDLE 	1400
#define SERVO_POS_RIGHT 	900

#include <stdint.h>

void servo_init();
void servo_setPosition(uint32_t position);

/*
 * servo.h
 *
 *  Created on: Feb 20, 2026
 *      Author: Laptop
 */

#define SERVO_POS_LEFT 		1900
#define SERVO_POS_MIDDLE 	1400
#define SERVO_POS_RIGHT 	900

#include <stdint.h>

void servo_init();
void servo_setPosition(uint32_t position);

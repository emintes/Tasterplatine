from testframework import *
from Tests.Util import *

enableIOSupply(LEVEL_5V)
moveServoUp(LEFT)
moveServoUp(RIGHT)

async def downloadFirmware():
    enableExternalSupply()
    await sleep_ms(800)
    abortTestOnFailure(True)
    res = await executeCommand(1, "")
    report.checkValue("Download Firmware to Device", res, 0)
    abortTestOnFailure(False)
    await sleep_ms(500)
    disableExternalSupply()

    await sleep_ms(1000)


async def powerSupply():
    #analyze the 3,3V regulator switch on behavior:
    supplyTraceSwitchOn = trace.TraceData(PIN_3V3_SUPPLY,2000, "3,3V Supply in mV")
    trace.start(supplyTraceSwitchOn,5)  #2000 values * 5us = 10ms recording time
    enableExternalSupply()
    await sleep_ms(50)
    supplyOvershootValue = max(supplyTraceSwitchOn.getData(0, supplyTraceSwitchOn.len()))
    report.checkValueMinMax("Switch On overshoot voltage", supplyOvershootValue/1000.0, 3.2, 3.6, "V")
    report.appendTrace("Power Supply - Switch On behavior", supplyTraceSwitchOn)

    #measure the 3,3V supply voltage:
    voltage3V3 = getInputVoltage(PIN_3V3_SUPPLY)
    report.checkValueTollerance("Check 3,3V supply voltage", voltage3V3, 3.3, 0.03, "V")

    #analyze supply voltage noise:
    supplyTrace = trace.TraceData(PIN_3V3_SUPPLY,1000, "3,3V Supply in mV")
    trace.start(supplyTrace,2)  #1000 values * 2us = 2ms recording time
    await sleep_ms(50)
    supplyData = supplyTrace.getData(0, supplyTrace.len())
    noise = max(supplyData) - min(supplyData)
    report.checkValueMinMax("Power Supply Noise", noise, 0, 100, "mVpp", 0)
    report.appendTrace("Power Supply - Noise", supplyTrace)


async def idleConditions():
    report.checkBool("Is signal of button left high?", getInput(PIN_BUTTON_LEFT) == HIGH)
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output frequency", pwmOut.frequency, 50, 0.2, "Hz")
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 7.0, 0.05, "%")
    report.checkValueMinMax("Check LED voltage (should be off)", getInputVoltage(PIN_LED), 3.0, 5.0, "V")


async def buttonLeftManuel():
    freeServos()
    await getUserInputBool("Press Button left")
    report.putInfo("Button left pressed")
    
    report.checkBool("Is signal of button left low?", getInput(PIN_BUTTON_LEFT) == LOW)
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 9.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")

    await getUserInputBool("Release Button left")
    report.putInfo("Button left released")


async def buttonLeft():
    moveServoDown(LEFT)
    await sleep_ms(200)
    report.putInfo("Button left pressed")
    
    report.checkBool("Is signal of button left low?", getInput(PIN_BUTTON_LEFT) == LOW)
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 9.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")

    moveServoUp(LEFT)
    await sleep_ms(200)
    setOutputHigh(PIN_SERVO_LEFT)
    report.putInfo("Button left released")


async def buttonRightManuel():
    freeServos()
    await getUserInputBool("Press Button right")
    report.putInfo("Button right pressed")
    
    report.checkBool("Is signal of button right low?", getInput(PIN_BUTTON_RIGHT) == LOW)
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 4.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")
    
    await getUserInputBool("Release Button right")
    report.putInfo("Button right released")


async def buttonRight():
    moveServoDown(RIGHT)
    await sleep_ms(200)
    report.putInfo("Button right pressed")
    
    report.checkBool("Is signal of button right low?", getInput(PIN_BUTTON_RIGHT) == LOW)
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 4.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")

    moveServoUp(RIGHT)
    await sleep_ms(200)
    setOutputHigh(PIN_SERVO_RIGHT)
    report.putInfo("Button right released")
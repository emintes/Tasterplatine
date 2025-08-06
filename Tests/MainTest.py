from testframework import *
from Tests.Util import *

enableIOSupply(LEVEL_3V3)

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

async def powerUp():
    enableExternalSupply()
    setOutputHigh(PIN_BUTTON_LEFT)
    setOutputHigh(PIN_BUTTON_RIGHT)
    await sleep_ms(200)


async def idleConditions():
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output frequency", pwmOut.frequency, 50, 0.2, "Hz")
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 7.0, 0.05, "%")
    report.checkValueMinMax("Check LED voltage (should be off)", getInputVoltage(PIN_LED), 3.0, 5.5, "V")


async def buttonLeft():
    setOutputLow(PIN_BUTTON_LEFT)
    await sleep_ms(100)
    report.putInfo("Button left pressed")
    
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output frequency", pwmOut.frequency, 50, 0.2, "Hz")
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 9.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")

    setOutputHigh(PIN_BUTTON_LEFT)
    await sleep_ms(200)
    report.putInfo("Button left released")

    await idleConditions()  #check if after releasing the button, the idle conditions are restored


async def buttonRight():
    setOutputLow(PIN_BUTTON_RIGHT)
    await sleep_ms(100)
    report.putInfo("Button right pressed")
    
    pwmOut = await getPwm(PIN_PWM_OUT, 200)
    report.checkValueTollerance("Check PWM output frequency", pwmOut.frequency, 50, 0.2, "Hz")
    report.checkValueTollerance("Check PWM output duty cycle", pwmOut.dutyCycle, 4.5, 0.05, "%")
    report.checkValueTollerance("Check LED voltage (should be on)", getInputVoltage(PIN_LED), 2.0, 0.1, "V")

    setOutputHigh(PIN_BUTTON_RIGHT)
    await sleep_ms(200)
    report.putInfo("Button right released")

    await idleConditions()  #check if after releasing the button, the idle conditions are restored
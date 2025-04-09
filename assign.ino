#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // Change 0x27 to 0x3F if needed

void setup() {
    Serial.begin(9600);  // Start Serial Monitor
    lcd.init();          // Initialize LCD
    lcd.backlight();     // Turn on backlight
    lcd.setCursor(0, 0);
    lcd.print("Sensor Value:");
}

void loop() {
    int sensorValue = analogRead(A0);  // Read the MQ-135 sensor

    lcd.setCursor(0, 1);
    lcd.print("      ");  // Clears old numbers (important)
    lcd.setCursor(0, 1);
    lcd.print(sensorValue);

    Serial.print("Sensor Value: ");  
    Serial.println(sensorValue);  

    delay(5000);  // Update every second
}


#include <FastLED.h>

#define LED_PIN     10
#define NUM_LEDS    166
#define SPEAKER_PIN 9

CRGB leds[NUM_LEDS];
CRGB currentColor;

int melody[] = {
  262,
  294,
  330,
  349,
  392,
  440,
  494,
  523
};

int noteDurations[] = {
  8, 8, 8, 8, 8, 8, 8, 8
};

void setup() {
  FastLED.addLeds<NEOPIXEL, LED_PIN>(leds, NUM_LEDS);
  playMelody();
  rainbowShow();
  delay(5000);
  transitionToWarmYellow();
  currentColor = CRGB(255, 221, 51);
}

void loop() {
  if (Serial.available()) {
    String emotion = Serial.readStringUntil('\n');
    CRGB targetColor;
    if (emotion == "angry") {
      targetColor = CRGB::Red;
    } else if (emotion == "sad") {
      targetColor = CRGB::Blue;
    } else {
      targetColor = CRGB(255, 221, 51);
    }

    transitionToColor(targetColor);
  }
}

void transitionToColor(CRGB targetColor) {
  const int transitionTime = 1000;
  const int steps = transitionTime / 20;

  for(int t = 0; t <= steps; t++) {
    for(int i = 0; i < NUM_LEDS; i++) {
      leds[i] = currentColor.lerp8(targetColor, t * 255 / steps);
    }
    FastLED.show();
    delay(20);
  }

  currentColor = targetColor;
}

void setLEDs(CRGB color) {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = color;
  }
  FastLED.show();
}


void rainbowShow() {
  const int cycles = 5;

  const int stepsPerCycle = 256;

  const int delayPerStep = 5000 / (cycles * stepsPerCycle);

  for(int cycle = 0; cycle < cycles; cycle++) {
    for(int step = 0; step < stepsPerCycle; step++) {
      for(int i = 0; i < NUM_LEDS; i++) {
        uint8_t hue = (step + (i * 256 / NUM_LEDS)) % 256;

        leds[i] = CHSV(hue, 255, 255);
      }

      FastLED.show();
      delay(delayPerStep);
    }
  }
}

void transitionToWarmYellow() {
  const int transitionTime = 5000;
  const int steps = transitionTime / 20;
  CRGB warmYellow = CRGB(255, 221, 51);

  for(int t = 0; t <= steps; t++) {
    for(int i = 0; i < NUM_LEDS; i++) {
      leds[i] = leds[i].lerp8(warmYellow, t * 255 / steps);
    }
    FastLED.show();
    delay(20);
  }
}

void warmYellow() {
  for(int i=0; i<NUM_LEDS; i++) {
    leds[i] = CRGB(255, 221, 51);
  }
  FastLED.show();
}

void playMelody() {
  for (int thisNote = 0; thisNote < sizeof(melody)/sizeof(int); thisNote++) {
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(SPEAKER_PIN, melody[thisNote], noteDuration);
    int pauseBetweenNotes = noteDuration * 1.3;
    delay(pauseBetweenNotes);
    noTone(SPEAKER_PIN);
  }
}

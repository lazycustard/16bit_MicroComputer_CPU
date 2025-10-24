; LED Demo for 16-bit CPU
; Human readable version for your assembler

; Turn on LED 0 (bit 0)
LOADA_IN 1
OUTA

; Turn on LED 1 (bit 1)  
LOADA_IN 2
OUTA

; Turn on LED 2 (bit 2)
LOADA_IN 4
OUTA

; Turn on LED 3 (bit 3)
LOADA_IN 8
OUTA

; Turn on LED 4 (bit 4)
LOADA_IN 16
OUTA

; Turn on LED 5 (bit 5)
LOADA_IN 32
OUTA

; Turn on LED 6 (bit 6)
LOADA_IN 64
OUTA

; Turn on LED 7 (bit 7)
LOADA_IN 128
OUTA

; Turn on LED 8 (bit 8)
LOADA_IN 256
OUTA

; Turn on LED 9 (bit 9)
LOADA_IN 512
OUTA

; Turn all LEDs off
LOADA_IN 0
OUTA

; Stop the program
HALT
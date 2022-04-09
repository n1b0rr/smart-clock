#include "lcd/lcd.h"

void LCD::clear() const {

	clearBehavior->perform_clear(SPI_pin,A0_pin);

}

void LCD::print(const std::string& text) const{

 	cursor = printBehavior->perform_print(SPI_pin, A0_pin, cursor, text);

}

int LCD::set_cursor(int location) const {

	return set_cursorBehavior->perform_set_cursor(SPI_pin, location);

}

void LCD::set_clock(int hh, int mm) const {

	set_clockBehavior->perform_set_clock(SPI_pin, hh, mm);

}

void LCD::print_clock_mode(const std::string& text) const {

	print_clock_modeBehavior->perform_print_clock_mode(SPI_pin, text);

}

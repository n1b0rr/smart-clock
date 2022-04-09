#ifndef ST7565R_H
#define ST7565R_H

#include <bcm2835.h>

#include "lcd/lcd.h"

class ST7565R_Display: public LCD{

	public:
		ST7565R_Display(uint8_t SPI_pin, uint8_t A0_pin, uint8_t reset_pin);
		virtual void init() const override;
		virtual void brightness(float) const override;
	
		~ST7565R_Display() override = default;


};

class Clear_ST7565R: public ClearBehavior{

	void perform_clear(uint8_t, uint8_t) const override;

};

class Print_ST7565R: public PrintBehavior{

	int perform_print(uint8_t, uint8_t, int,const std::string&) const override;

};

class Set_cursor_ST7565R: public Set_cursorBehavior{


};

class Set_clock_ST7565R: public Set_clockBehavior{


};

class Print_clock_mode_ST7565R: public Print_clock_modeBehavior{


};

namespace function_ST7565R{
	
	void lcd_set_page(unsigned int, unsigned int);

};

#endif //ST7565R_H

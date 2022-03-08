#ifndef ST7565R_H
#define ST7565R_H

#include <bcm2835.h>

#include "lcd/lcd.h"

class ST7565R_Display: public LCD{

	public:
		ST7565R_Display() = default;
		virtual void init() const override;
		virtual void brightness(float) const override;
	
		~ST7565R_Display() override = default;


};

class Clear_ST7565R: public ClearBehavior{


};

class Print_ST7565R: public PrintBehavior{


};

class Set_cursor_ST7565R: public Set_cursorBehavior{


};

class Set_clock_ST7565R: public Set_clockBehavior{


};

class Print_clock_mode_ST7565R: public Print_clock_modeBehavior{


};


#endif //ST7565R_H

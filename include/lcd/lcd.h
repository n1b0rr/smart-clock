#ifndef LCD_H
#define LCD_H

#include <string>
#include <cstdint>
#include <memory>

class ClearBehavior;
class PrintBehavior;
class Set_cursorBehavior;
class Set_clockBehavior;
class Print_clock_modeBehavior;

class LCD {

	public:
		LCD() = default;
		
		void clear() const;
		void print(std::string) const;
		int set_cursor(int) const;
		void set_clock(int, int) const;
		void print_clock_mode(std::string) const;
		virtual void init() const = 0;
		virtual void brightness(float) const = 0;
	
		virtual ~LCD() = default;
	
	protected:
		uint8_t SPI_pin;
		uint8_t pwm_channel;
		uint8_t reset_pin;
		uint8_t A0_pin;
	
	private:
		std::unique_ptr<ClearBehavior> clearBehavior;
		std::unique_ptr<PrintBehavior> printBehavior;
		std::unique_ptr<Set_cursorBehavior> set_cursorBehavior;
		std::unique_ptr<Set_clockBehavior> set_clockBehavior;
		std::unique_ptr<Print_clock_modeBehavior> print_clock_modeBehavior;

};

class ClearBehavior {

	public:
		virtual void perform_clear(uint8_t) const = 0;

};

class PrintBehavior {
	public:
		virtual void perform_print(uint8_t, std::string) const = 0;
		
};

class Set_cursorBehavior {

	public:
		virtual int perform_set_cursor(uint8_t, int) const = 0;

};

class Set_clockBehavior {

	public:
		virtual void perform_set_clock(uint8_t, int, int) const = 0;
};

class Print_clock_modeBehavior {
	public:
		virtual void perform_print_clock_mode(uint8_t, std::string) const;
};

#endif //LCD_H

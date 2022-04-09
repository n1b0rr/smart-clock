#include <cstring>

#include <iostream>

#include "lcd/st7565r.h"
#include "lcd/font.h"

#define MAX_LETTERS_PER_LINE 20

ST7565R_Display::ST7565R_Display(uint8_t SPI_pin, uint8_t A0_pin, uint8_t reset_pin) {


		this->SPI_pin = SPI_pin;
		this->reset_pin = reset_pin;
		this->A0_pin = A0_pin;
		clearBehavior.reset(new Clear_ST7565R);
		printBehavior.reset(new Print_ST7565R);
		
		init();
		
//		set_cursorBehavior;
//		set_clockBehavior;
//		print_clock_modeBehavior;


}

void ST7565R_Display::init() const {


	//init SPI hardware
	bcm2835_spi_chipSelect(SPI_pin);
	bcm2835_spi_set_speed_hz(9600);
	bcm2835_spi_setChipSelectPolarity(SPI_pin, LOW);
	bcm2835_spi_setDataMode(BCM2835_SPI_MODE3);

	//init output ports
	bcm2835_gpio_fsel(A0_pin, BCM2835_GPIO_FSEL_OUTP);
	bcm2835_gpio_fsel(reset_pin, BCM2835_GPIO_FSEL_OUTP);

	//display reset and disable A0
	bcm2835_gpio_write(A0_pin, LOW);
	bcm2835_gpio_write(reset_pin, LOW);
	bcm2835_delay(500);
	bcm2835_gpio_write(reset_pin, HIGH);
	bcm2835_delay(500);

	//configure display
	bcm2835_spi_transfer(0xA2);		//LCD bias select
	bcm2835_spi_transfer(0xA0);		//ram address seg
	bcm2835_spi_transfer(0xCF);		//COM output
	bcm2835_spi_transfer(0xA4);		//LCD display all points on/off
	bcm2835_spi_transfer(0xA6);		//lcd display --> normal mode

	bcm2835_spi_transfer(0x28 | 0x4);		//turn on voltage converter
	bcm2835_delay(50);
	bcm2835_spi_transfer(0x28 | 0x6);		//turn on voltage regulator
	bcm2835_delay(50);
	bcm2835_spi_transfer(0x28 | 0x7);		//turn on voltage follower
	bcm2835_delay(10);
	bcm2835_spi_transfer(0x20 | 0x7);		//set lcd operating voltage
	bcm2835_spi_transfer(0x81);		//electronic volume mode set
	bcm2835_spi_transfer(0x10);		//electronic volume register set contrast
	bcm2835_spi_transfer(0x40);

	clear();				//clear the display
	cursor = 0;
	
	bcm2835_spi_transfer(0xAF);        //display on

}

void ST7565R_Display::brightness(float value) const{


}

void Clear_ST7565R::perform_clear(uint8_t SPI_pin, uint8_t A0_pin) const {

	for(unsigned int i = 0; i < 8; ++i)
	{
		function_ST7565R::lcd_set_page(i, 0);
		bcm2835_gpio_write(A0_pin, HIGH);
		for(unsigned int j = 0; j < 129; j++)
		{
			bcm2835_spi_transfer(0x00);
		}
		bcm2835_gpio_write(A0_pin, LOW);
	}

	std::cout << "Screen has been cleared!" << std::endl;

}


int Print_ST7565R::perform_print(uint8_t SPI_pin, uint8_t A0_pin, int cursor, const std::string& text) const {
	
	int xPos, yPos;
	
	
	//berekeningen na kijken!
	yPos = cursor/MAX_LETTERS_PER_LINE;
	xPos = cursor%MAX_LETTERS_PER_LINE;
	
	cursor = xPos + (yPos * MAX_LETTERS_PER_LINE);
	
	if(text.c_str())
	{
		for(int i = 0; i < std::strlen(text.c_str()) - 1; i++)
		{
			//lcd_ascii5x7(xPos, yPos + (i * 6), text.c_str()[i]);
		}
	}
	
	
	std::cout << "Text has been written" << std::endl;
	
	return cursor;
}


void function_ST7565R::lcd_set_page(unsigned int page, unsigned int column) {

	uint8_t lsb = column & 0x0f;
	uint8_t msb = column & 0xf0;
	msb = msb >> 4;
	msb = msb | 0x10;
	page = page | 0xb0;

	bcm2835_spi_transfer(page);
	bcm2835_spi_transfer(msb);
	bcm2835_spi_transfer(lsb);

}

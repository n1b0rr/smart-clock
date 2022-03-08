#include "lcd/st7565r.h"

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
	
	bcm2835_spi_transfer(0xAF);        //display on

}

void ST7565R_Display::brightness(float value) const{


}

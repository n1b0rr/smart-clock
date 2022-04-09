#include <iostream>
#include "lcd/st7565r.h"

int main() {

	std::cout << "Hello world!\nCompiled via CMAKE on X86!\n";

	if(!bcm2835_init())
	{
		printf("Couldn't initialize bcm2835 library!\n");
		exit(-1);
	}

	 if(!bcm2835_spi_begin())
	{
		printf("Couldn't initialize the SPI hardware...\nAre you running root?\n");
		bcm2835_close();
		exit(-1);
	}

	ST7565R_Display lcd(1,2,3);
	lcd.print("test123");

	while(true)
	{
	
	}


	return 0;
}

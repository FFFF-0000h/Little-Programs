#include <stdio.h>
/* print Fahrenheit-Celsius table        for fahr = 0, 20, ..., 300; floating-point version */
#define LOWER 0 /*define the "magic" numbers 0, 300, 20*/
#define UPPER 300
#define STEP 20
main()
{
	int fahr;
	for (fahr = UPPER; fahr >= LOWER; fahr = fahr - STEP)
	{
		printf("%3d %6.1f\n", fahr, (5.0 / 9.0) * (fahr - 32));
	}
}

/*
main()
{
	float fahr, celsius;
	float lower, upper, step;
	lower = 0;
upper = 300; 
step = 20;	
fahr = upper;
while (fahr >= lower)
{
	celsius = (5.0 / 9.0) * (fahr - 32.0);
	printf("%3.0f %6.1f\n", fahr, celsius);
	fahr = fahr - step;
}
}
*/
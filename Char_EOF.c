#include <stdio.h>
/* copy input to output; 1st version  */
main()
{
	int c;
	while (c = getchar() != EOF)
	{
		printf("%d\n", c);
	}

	printf("%d", EOF);
}
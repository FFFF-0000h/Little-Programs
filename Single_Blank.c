#include <stdio.h>
/* copy input to output, replacing one or more blanks by a single blank */
main()
{
	int c;

	newBlank = 0;
	for (; (c = getchar()) != EOF;)
	{
		if (c == ' ')
		{
			while ((c = getchar()) == ' ')
				;
			putchar(' ');
		}
		putchar(c);
	}
}
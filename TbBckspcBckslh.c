#include <stdio.h>
/* copy input to output, replacing one or more blanks by a single blank */
main()
{
	int c;
	for (; (c = getchar()) != EOF;)
	{
		if (c == '\t')
		{
			while ((c = getchar()) == '\t')
				;
			putchar('\t');
		}
		
			if (c == '\b')
		{
			while ((c = getchar()) == '\b')
				;
			putchar('\b');
		}
		
			if (c == '\\')
		{
			while ((c = getchar()) == '\\')
				;
			putchar('\\');
		}
		
		putchar(c);
	}
}
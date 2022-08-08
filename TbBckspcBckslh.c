#include <stdio.h>
/* copy its input to its output, replacing each tab by \t, each backspace by \b, and each backslash by \\. */
main()
{
	int c;
	for (; (c = getchar()) != EOF;)
	{
		if (c == '\t')
		{
			while ((c = getchar()) == '\t')
				;
			putchar('\\');
			putchar('t');
		}
		
			if (c == '\b')
		{
			while ((c = getchar()) == '\b')
				;
			putchar('\\');
			putchar('b');
		}
		
			if (c == '\\')
		{
			while ((c = getchar()) == '\\')
				;
			putchar('\\');
			putchar('\\');
		}
		
		putchar(c);
	}
}
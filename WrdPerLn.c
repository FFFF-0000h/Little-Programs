// Write a program that prints its input one word per line

#include <stdio.h>
#define IN 1
#define OUT 0
/* count lines, words, and characters in input */
main()
{
	int c, newWord, state;
	state = OUT;
	newWord = 0;
	for (; (c = getchar()) != EOF;)
	{
		if (c == ' ' || c == '\n' || c == '\t')
		{
			state = OUT;
		}
		else if (state == OUT)
		{
			state = IN;
			++newWord;
			putchar('\n');
		}
		putchar(c);
	}
	printf("%d\n", newWord);
}

//TODO: Make the first word appear on first line instead of newline '\n'

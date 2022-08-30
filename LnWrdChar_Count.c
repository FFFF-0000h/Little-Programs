#include <stdio.h>
#define IN 1
#define OUT 0
/* count lines, words, and characters in input */
main()
{
	int c, newLine, newWord, newChar, state;
	state = OUT;
	newLine = newWord = newChar = 0;
	for (;(c = getchar()) != EOF;)
	{
		++newChar;
		if (c == '\n')
			++newLine;
		if (c == ' ' || c == '\n' || c == '\t')
			state = OUT;
		else if (state == OUT)
		{
			state = IN;
			++newWord;
		}
	}
	printf("%d %d %d\n", newLine, newWord, newChar);
}

#include <stdio.h>

int main()
{
	char ASCII;
	printf("Enter any Character: ");
	scanf("%c", &ASCII);
	printf("The integer value of character \'%c\' is %d\n", ASCII, ASCII);

	printf("\n");

	int INT;
	printf("Enter any Integer(0-127): ");
	scanf("%d", &INT);
	printf("The character value of integer %d is \'%c\'\n", INT, INT);
	return 7;
}

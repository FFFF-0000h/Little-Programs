#include <stdio.h>
/* count characters in input; 2nd version */
main()
{
	double nc;
	for (nc = 0; getchar() != EOF; ++nc)
		;
		// float construct is used for both float and double
	printf("%.0f\n", nc);
}
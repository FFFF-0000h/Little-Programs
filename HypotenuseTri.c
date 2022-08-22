#include <stdio.h>
#include <math.h>

int main()
{
	double a;
	double b;

	printf("Enter side a: ");
	scanf("%lf", &a);

	printf("Enter side b: ");
	scanf("%lf", &b);

	double c = sqrt((a*a)+(b*b));
	printf("The Hypotenuse of side %f and %f is %f\n", a, b, c);
	return 7;
}

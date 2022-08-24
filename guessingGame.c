#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h> //rand() function access
#include <time.h> //time() function access

int main()
{
	int maxNum;
	printf("Enter the maximum range for your guesses: ");
	scanf("%d", &maxNum);

	srand(time(NULL)); //the time function works without passing in any arg, hence why we pass in NULL.			   //We generate the random num seed from the computer because of the randomness speed

	int randomNum = rand() % maxNum + 1; //the reason for modulo operator is because that would allow for a remainder of "0 - maxNum". It takes that huge number divides it by "maxNum + 1" and whatever is left over, using int division, is going to be assigned to "randomNum"

	int input;
	printf("Enter your guess(0-%d): ", maxNum);
	scanf("%d", &input);

	if (randomNum == input)
	{
		printf("You guessed correctly!\n");
		return 7;
	}else
	{
		printf("Wrong, try again\n");
		printf("Random number is %d\n", randomNum);
	}
}

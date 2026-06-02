#include <stdio.h>
#include <string.h>
#include <ctype.h>

int Luhn_Algorithm()
{
	int i, k, digit, value=0, len;
	char num[17];
	printf("Enter the number:");
	scanf("%16s", num);
	len=strlen(num);
	// Length Check
	if(len!=16)
	{
		printf("Enter a valid 16-digit number.");
		return 0;
	}
	// Check for Invalid Characters
	for(i=0;i<=(len-1);i++)
	{
		if((isdigit(num[i]))==0)
		{
			printf("Invalid Character %c. Enter a valid 16-digit number only.", num[i]);
			return 0;
		}
	}
	// Main Logic
	for(i=0;i<=15;i++)
	{
		digit=(num[i]-'0');
		if(i%2 == 0)
		{
			k = digit*2;
			if(k>9)
		    {
			  k -= 9;
		    }
		}
		else 
		{
			k = digit;
		}
		value=value+k;
	}
	
	if((value%10)==0)
	{
		printf("%s passes Luhn's Algorithm :)\n", num);
	}
	else
	{
		printf("%s does not pass Luhn's Algorithm :(\n", num);
	}
	return 0;
}

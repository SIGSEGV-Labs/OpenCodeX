/** Armstrong Number Identifier **/
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int n, no =0, k , s=0, t,d;
	
	printf("Enter any number:");
	scanf("%d", &n);
	t = n;
	
	if(n<0)
	{
		printf("Please enter a positive number.");
		return 0;
	}
		
	while(t!=0)
		{
			t/=10;
			no++;
		}
     t = n;
	
	if(t<=99999)
	{
		while(t!=0)
		{
			k=t%10;
			d = k;
			for(int i=1; i<no; i++)
				{
					k*=d;
				}
			s+=k;
			t=t/10;
		}
	}
		
	else
	{
		printf("Come on, why are you even checking for that big of a number ;(");
	}
	
	if(n == s)
	{
		printf("%d is an armstrong number.", n);
	}
	
	else
	{
		printf("%d is not an armstrong number.", n);
	}

	return 0;
}

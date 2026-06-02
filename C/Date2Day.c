/** Date2Day **/

#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main()
{
	int q, m = 0, y, k, j, h ,ty;
	char month[12];
	/* Date*/
	printf("\n\tEnter the date:");
	scanf("%d", &q);
	/* Year */
	printf("\n\tEnter the year:");
	scanf("%d", &y);
	/* Month */
	printf("\n\tEnter the month name:");
	scanf("%s", month);
	char *months[] = {
		"March", "April", "May", "June", "July", 
		"August", "September", "October", "November", "December", 
		"January", "February"
	};

	for (int i = 0; i < 12; i++) 
	{
			if (strcmp(month, months[i]) == 0) {
				m = i+3;
				break;
			}
		}

	if (m == 0) 
	{
			printf("\n\tInvalid Month Name! Try again.\n");
			return 0;
	}
	if(m==13 || m==14)
	{
		y--;
	}
	
	k=y%100;
	j=y/100;
	
	/** Zeller's Formula **/
	h = (q + ((13*(m+1))/5) + k + (k/4) + (j/4) - 2*j + 700) % 7;
	// system("cls");
    
	if(m==13 || m==14)
	{
		y++;
	}
	
	switch(h)
	{
		case 0:
			printf("%d %s %d is Saturday",q, month, y);
				break;
		case 1:
			printf("%d %s %d is Sunday",q, month, y);
				break;
		case 2:
			printf("%d %s %d is Monday",q, month, y);
				break;
		case 3:
			printf("%d %s %d is Tuesday",q, month, y);
				break;
		case 4:
			printf("%d %s %d is Wednesday",q, month, y);
				break;
		case 5:
			printf("%d %s %d is Thursday",q, month, y);
				break;
		case 6:
			printf("%d %s %d is Friday",q, month, y);
				break;
	}
	return 0;
}

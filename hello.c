# include<stdio.h>

int main() {
    int number = 25;
    char star = '*';
    float pi = 3.14f;
    int a=20;
    int A=40;
    printf("Number: %d\n", number);
    printf("Character: %c\n", star);
    printf("Float: %f\n", pi);
    printf("Lowercase a: %d\n", a);
    printf("Uppercase A: %d\n", A);

    int len = 15;
    int bread=7;
    int area=len*bread;
    printf("Area of rectangle: %d\n", area);
    printf("value of pi is %f\n", pi);
    return 0;

    int l,b;
    printf("Enter length and breadth of rectangle: "); 
    scanf("%d",&l);
    scanf("%d",&b);
    int ar = l + b;
    printf("Area of rectangle: %d\n", ar);
    return 0;
}

#include<stdio.h>
#include<math.h>
int main(){
    int a,b,area;
    printf("Enter length and breadth of rectangle: ");
    scanf("%d",&a);
    scanf("%d",&b);
    area=a*b;
    printf("Area of rectangle: %d\n",area);
    return 0;

    int c,d;
    c=2;
    d=3;
    int f=c+d;
    int power=pow(c,d);
    printf("Sum is %d and power is %d\n",f,power);
    return 0;
}

#include<stdio.h>
int main(){
    int a;
    printf("Enter a number: ");
    scanf("%d",&a);
    if(a%2==0){
        printf("The number is even\n");
    }
    else{
        printf("The number is odd\n");
    }
    return 0;
}
int main(){
    int isSunday=1;
    
}



#include<stdio.h>
int main(){
    int x;
    printf("Enter a number: ");
    scanf("%d",&x);
    if (x>9&&x<100){
        printf("The number is a two-digit number\n");
    }
    else{
        printf("The number is not a two-digit number\n");
    }
    return 0;
}

#include<stdio.h>
int main(){
    int a,b,c;
    printf("Enter three numbers: ");
    scanf("%d%d%d",&a,&b,&c);
    int avg;
    avg=(a+b+c)/3;
    printf("The average of three numbers is %d\n",avg);

}
int main(){
    char ch;
    printf("Enter a character: ");
    scanf("%c",&ch);
    if(("ch">='a'&&ch<='z')|| (ch>='A'&&ch<='Z')){
        printf("The character is an alphabet\n");
    }
    else{
        printf("The character is not an alphabet\n");
    }
}

int main(){
    int i;
    scanf("%d",&i);
    for(int j=1.00;j<=10.00;++j){
        printf("%f x %f = %f\n",i,j,i*j);
    }
    return 0;
}

#include<stdio.h>
int main(){
    int n;
    printf("Enter the number of rows: ");
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        for (int j=i;j<=n;j++){
            printf("*");
        }
        printf("\n");   
    }
    return 0;
}

#include<stdio.h>
int main(){
    int n;
    printf("Enter the number of rows: ");
    scanf("%d",&n);
    for (int i=1;i<=n;i++){
        for (int j=1;j<=i;j++){
            printf(" ");
        }
        printf("*\n");
    }
    return 0;
}





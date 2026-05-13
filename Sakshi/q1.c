#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>
int main(){
    pid_t c1,c2;
    c1= fork();
    if ( c1 == 0 ){
         printf("CHild 1: PID=%d, PPID= %d\n",getpid(), getppid());
         return 0;
    }
    else{
        c2=fork();
        if ( c2 ==0 ){
             printf("Child2: PID= %d, PPID= %d\n",getpid(),getppid());
             return 0;
             }
        else {
             wait ( NULL );
             wait ( NULL );
             printf("Parent:PID=%d,both children finished.\n",getpid());
       }
    }
    return 0;
} 
             

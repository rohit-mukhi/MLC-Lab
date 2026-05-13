#include<stdio.h>
#include<unistd.h>
#include<sys/types.h>
int main(void)
{
    pid_t pid;
    pid = fork();
    if ( pid < 0 ) {
         perror("Fork");
         return 0;
    }
    if ( pid == 0 ){
         while(1){
             printf("Child: PID= %d, PPID  = %d\n", getpid(), getppid());
             fflush(stdout);
             sleep(1);
        }
    } else {
         while(1){
             printf("Parent: PID = %d, Child PID = %d\n", getpid(), pid);
             fflush(stdout);
             sleep(1);
        }
    }
    return 0;
}


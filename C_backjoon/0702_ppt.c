#define _POSIX_C_SOURCE 200809L  // POSIX 기능 사용을 명시

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>

void handler(int sig) {
    printf("Received signal: %d\n", sig);
}

int main() {
    signal(SIGUSR1, handler);  // 사용자 정의 시그널 핸들러 등록

    pid_t pid = fork();

    if (pid == 0) {
        // 자식 프로세스
        printf("Child PID: %d\n", getpid());
        pause();  // 시그널 대기
    } else {
        // 부모 프로세스
        sleep(1);
        kill(pid, SIGUSR1);  // 자식에게 시그널 전송
    }
    return 0;
}

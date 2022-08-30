#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main(int argc, char *argv[])
{
    int sockfd, portno, n;
    struct sockaddr_in serv_addr;
    struct hostent *server;

    char buffer[1024];
    if (argc < 3) {
       fprintf(stderr,"usage %s hostname port\n", argv[0]);
       exit(0);
    }
    portno = atoi(argv[2]);
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) 
        error("ERROR opening socket");
    server = gethostbyname(argv[1]);
    if (server == NULL) {
        fprintf(stderr,"ERROR, no such host\n");
        exit(0);
    }
    bzero((char *) &serv_addr, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    bcopy((char *)server->h_addr, 
         (char *)&serv_addr.sin_addr.s_addr,
         server->h_length);
    serv_addr.sin_port = htons(portno);
    // if (connect(sockfd,(struct sockaddr *) &serv_addr,sizeof(serv_addr)) < 0) 
    //     error("ERROR connecting");
    struct sockaddr from;
    socklen_t serv_len = sizeof(serv_addr), from_len = sizeof(from);
    while(1){
        printf("Please enter the message: ");
        bzero(buffer,1024);
        fgets(buffer,1023,stdin);
        n = sendto(sockfd, buffer, sizeof(buffer), 0, (struct sockaddr *)&serv_addr, serv_len);
        if (n < 0) {
            error("ERROR sendto");
        }
            
        bzero(buffer,1024);
        n = recvfrom(sockfd, buffer, sizeof(buffer), 0, &from, &from_len);
        if (n < 0) {
            error("ERROR recvfrom");
        }
        printf("Client received a response: %s\n\n",buffer);
    }
    close(sockfd);
    return 0;
}

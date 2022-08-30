/* A simple server in the internet domain using TCP
   The port number is passed as an argument */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h> 
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

// void *SigCatcher(int n) 
// { 
//  wait3(NULL,WNOHANG,NULL); 
// } 

void dostuff(int newsockfd){
    char buffer[256];
    while(1){
        bzero(buffer,256);
        int n = read(newsockfd,buffer,255);
        if (n < 0) error("ERROR reading from socket");
        if (n == 0){
            close(newsockfd);
            return;
        }
        printf("Here is the message: %s\n",buffer);
        n = write(newsockfd,"I got your message",18);
        if (n < 0) error("ERROR writing to socket");     
    }
    close(newsockfd);
}


int main(int argc, char *argv[])
{
    int sockfd, portno;
    socklen_t clilen;
    char buffer[1024];
    struct sockaddr_in serv_addr, cli_addr;
    int n;
    if (argc < 2) {
        fprintf(stderr,"ERROR, no port provided\n");
        exit(1);
    }
    sockfd = socket(AF_INET, SOCK_DGRAM, 0);
    if (sockfd < 0) 
    error("ERROR opening socket");
    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);
    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0) 
            error("ERROR on binding");
    struct sockaddr from;
    socklen_t fromlen = sizeof(from); 
    while (1) 
    { 
        bzero(buffer, sizeof(buffer));
        n = recvfrom(sockfd,buffer,sizeof(buffer)-1,0,&from, &fromlen); 
        if (n < 0){
            error("ERROR recvfrom");
        }
        printf("Here is the message: %s\n",buffer);
        n = sendto(sockfd,"Got your message ",17, 0,&from, fromlen); 
        if (n < 0) {
            error("ERROR sendto"); 
        }
        
    }
    close(sockfd);
    return 0; 
}
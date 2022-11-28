#include <iostream>
#include <string>
#include <vector>

typedef unsigned char uint8_t;

void convert2char(float num, std::vector<uint8_t> &arr, int decimals = 4){
    std::string str = std::to_string(num);
    arr.clear();

    int counter = -1;

    for(auto iter = str.begin(); iter!= str.end(); iter++){
        if(counter == -1){
            arr.push_back(*iter);

            if(*iter == '.'){
                counter++;
            }
        }else{
            arr.push_back(*iter);
            counter++;

            if(counter >= decimals){
                break;
            }
        }
    }
}

int main(){
    float num =-3.1415926;
    std::vector<uint8_t> res;
    convert2char(num, res, 4);
    return 0;
}
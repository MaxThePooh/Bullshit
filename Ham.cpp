
#include <iostream>
#include <map>

int diff(std::string in,std::string cl)
{
    int differ=0;
    for(int i=0;i<cl.size();++i)
        if(in[i]!=cl[i])
            ++differ;
    return differ;
}

int main()
{
    std::map<char,std::string> ham={{'0',"0000000"}, {'1',"0001111"}, {'2',"0010110"},{'3',"0011001"}, {'4',"0100101"}, {'5',"0101010"},
    {'6',"0110011"}, {'7',"0111100"}, {'8',"1000011"}, {'9',"1001100"}};
    
    std::string in;
    std::cin>>in;
    int min=diff(in,ham['0']);
    std::map<char,std::string>::iterator imin=ham.begin();
    for(std::map<char,std::string>::iterator i=ham.begin();i!=ham.end();++i)
    {
        int d=diff(in,i->second);
        if(d<min)
        {
            min=d;
            imin=i;
        }
    }
    if(min<=1)
    std::cout<<imin->first;
    else
    std::cout<<"Wrong code";
    return 0;
}

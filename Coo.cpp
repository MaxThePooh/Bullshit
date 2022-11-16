#include <iostream>
#include <vector>
#include <map>
#include <cmath>

enum Task{
    inf, sound, vid
};

void inpm(long long int& value)
{
      std::string mult;
                std::cin>>mult;
                if(mult=="Byte")
                    value*=8;
                else if(mult=="Kb")
                    value*=8*1024;
                else if(mult=="Mb")
                    value=value*pow(2,23);
                else if(mult=="Gb")
                    value=value*pow(2,33);
}

int main(int argc,char** argv)
{
    std::cout<<"Type of task:"<<std::endl
    <<"1 Information"<<std::endl
    <<"2 Sound"<<std::endl
    <<"3 Video"<<std::endl;
    
    int choice;
    std::cin>>choice;
    if(choice>3 || choice<1)
        return 1;
        
    system("clear");
    std::cout<<"Unknown value: ";
    constexpr long long int nan=-1;
    if((Task)choice-1==Task::inf) //n i I N
    {
        std::string unk;
        std::map<std::string,long long int> values={{"n",nan},{"i",nan},{"I",nan},{"N",nan}};
        std::cin>>unk;
        values.erase(unk);
        
        std::cout<<"Known values (with Bit,Byte,Kb,Mb,Gb; separate with space; leave with q):"<<std::endl;
        
        std::string name;
        long long int value;
        while(name!="q")
        {
            std::cin>>name;
            if(name!="q")
            {
            std::cin.ignore(2,'=');
            std::cin>>value;
            if(name=="i" || name=="I")
                inpm(value);
            values[name]=value;
            }
        }
        system("clear");
        if(unk=="n")
        {
            if(values["i"]!=nan && values["I"]!=nan)
                std::cout<<"n="<<values["I"]/values["i"];
        }else if(0)
        {
            
        }
    }
    if((Task)choice-1==Task::sound)//
    {
        
    }
    if((Task)choice-1==Task::vid)
    {
        
    }
    return 0;
}

#include <iostream>
#include <vector>
#include <map>

enum Task{
    inf, sound, vid
};


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
    if((Task)choice-1==Task::inf) //n i I
    {
        std::string unk;
        std::map<std::string,int> values={{"n",0},{"i",0},{"I",0}};
        std::cin>>unk;
        values.erase(unk);
        for(std::map<std::string,int>::iterator it=values.begin();it!=values.end();++it)
        {
            int val;
            std::cout<<it->first<<"=";
            std::cin>>val;
            it->second=val;
        }
        if(unk=="I")
        {
            std::cout<<"I="<<values["n"]*values["i"]<<"Bit";
        }
    }
    if((Task)choice-1==Task::sound)
    {
        
    }
    if((Task)choice-1==Task::vid)
    {
        
    }
    return 0;
}


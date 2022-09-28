
#include <iostream>


int main()
{
    int n;
    int base;
    std::cin>>n>>base;
    int k=1;
    int res=0;
    do{
        res+=n%base*k;
        k*=10;
        n/=base;
    }while(n!=0);
    std::cout<<res;
    return 0;
}

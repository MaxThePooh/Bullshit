
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n;
    int base;
    std::cin>>base>>n;
    int result=0;
    int count=0;
    while(n!=0)
    {
        result+=(n%10)*pow(base,count);
        n/=10;
        ++count;
    }
    std::cout<<result;
    return 0;
}

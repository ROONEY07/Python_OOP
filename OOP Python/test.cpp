#include<bits/stdc++.h>
using namespace std;
int main()
{
    string str = "hello world";

    stringstream ss(str);
    string word;
    while (ss >> word)
    {
        cout<<word<<endl;
        for (char i = 0; i < word.length(); i++)
        {
            cout<<word[i]<<endl;
        }
    }
    
}
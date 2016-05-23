#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>



using namespace std;

int main(int argc, char* argv[])
{
    int s = 0;
    int s_max = -1;
    int n = atoi(argv[1]);
    int perms [n];
    for (int i = 0; i < n; i++) 
    {
        perms[i] = i+1;
    }
    int global_ans = 0;
    int count = 0;
    do 
    {
        ++count;
        for (int i = 0; i < n; i++) 
        {
            for (int j = i+1; j < n; j++)
            {
                if (abs(perms[i]-perms[j]) == j-i)
                {
                    goto end_of_nested_loops;
                }
            }
        }
        global_ans++;
        for (int j = 0; j < n; j++) 
        {
            cout << perms[j] << " ";
        }
        cout << "-> " << count;
        cout << endl;
        // s = 0;
        // for (int j = 0; j < n-1; j++) 
        // {
        //     cout << abs(perms[j]-perms[j+1]) << " ";
        //     s += abs(perms[j]-perms[j+1]);
        // }
        // cout << "Ans: " << s;
        // cout << endl;
        end_of_nested_loops:
        int k = 0;
    } while (next_permutation(perms,perms+sizeof(perms)/sizeof(perms[0])));
    cout << global_ans << endl;
    //cout << s_max << endl;
    return 0;
}
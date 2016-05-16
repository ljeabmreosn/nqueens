#include <iostream>
#include <algorithm>
#include <string>
#include <stdio.h>



using namespace std;

int main(int argc, char* argv[])
{
    int n = atoi(argv[1]);
    int perms [n];
    for (int i = 0; i < n; i++) 
    {
        perms[i] = i;
    }
    int global_ans = 0;
    do 
    {
        for (int i = 0; i < n; i++)
        {
            int index = 0;
            for (int r = -i; r < n-i; r++)
            {
                if (r != 0 && (perms[index] == perms[i] + r || perms[index] == perms[i] - r))
                {
                    goto end_of_nested_loops;
                }
                index++;
            }
        }
        global_ans++;
        for (int j = 0; j < n; j++) 
        {
            cout << perms[j] << " ";
        }
        cout << endl;
        end_of_nested_loops:
        int k = 0;
    } while (next_permutation(perms,perms+sizeof(perms)/sizeof(perms[0])));
    cout << global_ans;
    return 0;
}
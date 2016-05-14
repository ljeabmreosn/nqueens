#include <iostream>
#include <algorithm>
#include <string>

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
        // cout << perms[0] << ' ' << perms[1] << ' ' << perms[2] << '\n';
        int ans = 0;
        for (int i = 0; i < n; i++)
        {
            int index = 0;
            for (int r = -i; r < n-i; r++)
            {
                if (r != 0 && (perms[index] == perms[i] + r || perms[index] == perms[i] - r))
                {
                    break;
                }
                index++;
                if (index == n)
                {
                    ans++;
                }
            }
        }
        if (ans == n)
        {
            global_ans++;
        }
    } while (next_permutation(perms,perms+sizeof(perms)/sizeof(perms[0])));
    cout << global_ans;
    return 0;
}
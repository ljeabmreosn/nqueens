#include <iostream>
#include <stdlib.h>
using namespace std;
int s = 0;
int cond(int p[], int i)
{
    for (int r = 0; r < i; r++)
    {
        if (abs(p[i]-p[r])==abs(i-r))
        {
            return 0;
        }
    }
    return 1;
}
void level(int p[], int a[], int alen, int i, int n)
{
    if (i >= n)
    {
        ++s;
    }
    else
    {
        for (int x = 0; x < alen; x++)
        {
            p[i] = a[x];
            if (cond(p, i))
            {
                int b[alen-1];
                for (int k = 0; k < x; k++)
                {
                    b[k] = a[k];
                }
                for (int k = x+1; k < alen; k++)
                {
                    b[k-1] = a[k];
                }
                level(p, b, alen-1, i+1, n);
            }
        }
    }
}
int perms(int n)
{
    int p[n];
    for (int i = 0; i < n; i++)
    {
        p[i] = 0;
    }
    int a[n];
    for (int i = 0; i < n; i++)
    {
        a[i] = i+1;
    }
    level(p, a, n, 0, n);
    return s;
}
int main(int argc, char* argv[])
{
    cout << perms(atoi(argv[1]));
}
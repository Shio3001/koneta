#include <bits/stdc++.h>
using namespace std;

int main()
{
    cout << "開始!" << endl;

    int now_num;

    now_num = 1;

    while (now_num < 100)
    {
        now_num++;

        long double heiho = round(sqrtl(now_num)); // C++17 から *

        bool flag = false;

        for (int i = 2; i <= heiho; i++)
        {
            int mod = now_num % i;
            if (mod == 0)
            {

                flag = true;
                continue;
            }
        }

        if (flag == false)
        {
            cout << now_num << endl;
        }
    }
    return 0;
}
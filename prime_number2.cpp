#include <bits/stdc++.h>
using namespace std;

int limit = 100;

int calculation(vector<int> array)
{
    int length = 100;

    for (int i = 2; i <= length; i++)
    {
        long double heiho = round(sqrtl(array[i])); // C++17 から *
        for (int j = 2; j <= heiho; j++)
        {
            if (array[i] % j == 0)
            {
                array[i] = false;
            }
        }
    }

    /*素数出力*/

    for (int p = 0; p <= length - 1; p++)
    {
        if (array[p] != false)
        {
            cout << array[p] << endl;
        }
    }

    return 0;
}

int main()
{
    std::vector<int> array;

    cout << "開始!" << endl;
    for (int i = 2; i <= limit; i++)
    {
        array.push_back(i);
    }
    calculation(array);

    return 0;
}
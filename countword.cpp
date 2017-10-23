#include <iostream>
#include <set>
#include <map>
#include <string>

using namespace std;

int main(void)
{
  std::map<string, int> M;
  std::map<string, int>::iterator it;
  string str;

  ifstream ifs("~/bible.txt");
  
  while (ifs >> str)
    {
      //    std:vector<string> v = str.split
      it = M.find(str);
      if (it != M.end())
	{
	  it->second += 1;
	}
      else
	{
	  M.insert(std::make_pair(str, 1));
	}
    }

  for (it=M.begin(); it!=M.end(); it++)
    {
      cout << it->first << it->second << endl;
    }

  return 0;
}

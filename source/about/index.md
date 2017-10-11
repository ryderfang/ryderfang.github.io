---
title: about
layout: page
date: 2017-09-26 20:11:37
---

### *☛ Whoami*

> Life is too short to be proficient in C plus plus. —— [Bjarne Stroustrup](http://www.stroustrup.com)

``` c++ 
#include <map>
#include <string>
#incldue <time.h>
#include <vector>
class FongRay {
private:
    enum class _Gender:uchar_t {Male, Female};
    using _Tvs = std::vector<std::string>;
    using _Tmss = std::unordered_map<std::string, std::string>;
public
    static std::string name = "Fang Rui";
    static std::string birthday = "1991-06-06";
    static _Gender gender = Male;
    uint32_t static age {
        time_t t;
        time(&t);
        tm *ltm = localtime(&t);
        return ltm->tm_year + 1900 - 1991;
    }
    static _Tvs languages{"C/C++", "Objective-C", "Python", "Go"};
    static _Tmss works({{"2345.com", "2014.07~2016.04"},
                       {"bilibili.com", "2016.04~2017.10"}
                      });

    // I'm the unique one, 'Constructors' are illegal.
    FongRay(const FongRay& fr) = delete;
    FongRay & operator=(const FongRay& fr) = delete;
private:
    FongRay();
    ~FongRay();
};
```

### *☛ Links*

* [Gayhub](https://github.com/FongRay)

---
[*Json Editor*](../jsoneditor)
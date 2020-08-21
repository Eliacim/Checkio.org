'''
https://py.checkio.org/en/mission/sort-by-extension/

You are given a list of files. You need to sort this list by the file
extension. The files with the same extension should be sorted by name.

Some possible cases:

Filename cannot be an empty string;
Files without the extension should go before the files with one;
Filename ".config" has an empty extension and a name ".config";
Filename "config." has an empty extension and a name "config.";
Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
Filename ".imp.xls" has an extension "xls" and a name ".imp". Input: A list of
filenames.

Output: A list of filenames.
'''


from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    dic = {}
    lis = []
    for file in files:
        k, v = file.rsplit('.', 1)
        dic[v+k] = file
    dic = [d[1] for d in sorted(dic.items())]
    for i, d in enumerate(dic):
        if d[0] == '.' and d.count('.') <= 1:
            dic.pop(i)
            lis.append(d)
        if d[-1] == '.':
            dic.pop(i)
            lis.append(d)
    return lis + dic


if __name__ == '__main__':
    print("Example:")
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']))
    # print(sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']))
    print(sort_by_ext([".config", "my.doc", "1.exe", "345.bin", "green.bat",
                       "format.c", "no.name.", "best.test.exe"]))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa']) ==\
    #     ['1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) ==\
    #     ['1.aa', '1.bat', '2.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) ==\
    #     ['.bat', '1.aa', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) ==\
    #     ['.aa', '.bat', '1.bat', '1.cad']
    # assert sort_by_ext(['1.cad', '1.', '1.aa']) ==\
    #     ['1.', '1.aa', '1.cad']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) ==\
    #     ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    # assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) ==\
    #     ['1.aa', '1.bat', '1.cad', '.aa.doc']
    assert sort_by_ext([".config", "my.doc", "1.exe", "345.bin", "green.bat",
                        "format.c", "no.name.", "best.test.exe"]) ==\
        [".config", "no.name.", "green.bat", "345.bin", "format.c", "my.doc",
         "1.exe", "best.test.exe"]

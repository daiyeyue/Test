def triangle(n):
    '''
    *           
   * *
  * * *
 * * * * 
* * * * *
    :param n: 等边三角形的行数
    :return: 
    '''
    if n <= 1:
        print("一行*无法成为等边三角形")
    else:
        for i in range(n,0,-1):
            print(" " * (i - 1) + "*" + " *" * (n-i))


triangle(20)
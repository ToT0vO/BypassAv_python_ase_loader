一个简单的Shellcode loader

![image-20230405200634334](C:\Users\zz\AppData\Roaming\Typora\typora-user-images\image-20230405200634334.png)

使用md5生成hash作为key

![image-20230405200716358](C:\Users\zz\AppData\Roaming\Typora\typora-user-images\image-20230405200716358.png)

再shellcodedecrypt.py中填入生成的key，运行生成密文

![image-20230405200818669](C:\Users\zz\AppData\Roaming\Typora\typora-user-images\image-20230405200818669.png)

在avxc.py中写入刚刚生成hash所用的密钥，并修改vdfbsxcy中的变量为密文

```
pyinstaller -F -w -i 98B8596E39.ico python_ase.py
```

目前可以过360和火绒

![image-20230405201424679](C:\Users\zz\AppData\Roaming\Typora\typora-user-images\image-20230405201424679.png)

![image-20230405201515709](C:\Users\zz\AppData\Roaming\Typora\typora-user-images\image-20230405201515709.png)



本项目修改自

[https://github.com/anx0ing/Python_BypassAV_demo]: 

感谢anx0ing师傅
一个简单的Shellcode loader

![image-20230405200634334](https://user-images.githubusercontent.com/129960499/230082153-980d4862-90bb-4e5f-8567-17449215c3ed.png)

使用md5生成hash作为key

![image-20230405200716358](https://user-images.githubusercontent.com/129960499/230082260-959a1342-0414-45cb-b862-adac3292d7db.png)

再shellcodedecrypt.py中填入生成的key，运行生成密文

![image-20230405200818669](https://user-images.githubusercontent.com/129960499/230082476-7be8ad97-a3ac-458f-9c26-b0cc7afce5c2.png)

在avxc.py中写入刚刚生成hash所用的密钥，并修改vdfbsxcy中的变量为密文

```
pyinstaller -F -w -i 98B8596E39.ico python_ase.py
```

目前可以过360和火绒

![image-20230405201424679](https://user-images.githubusercontent.com/129960499/230082603-9800609d-9b3c-4e25-bccf-619c37e7b5ec.png)

![image-20230405201515709](https://user-images.githubusercontent.com/129960499/230082633-be21e6d7-295b-46b0-b178-fb8b9327724e.png)



本项目修改自

[https://github.com/anx0ing/Python_BypassAV_demo]: 

感谢anx0ing师傅

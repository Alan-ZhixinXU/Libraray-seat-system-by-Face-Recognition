# Libraray-seat-system
A system contain Face Recognition and student's seat preference.
This system contains 3 parts, and some additional functions.

1  The first part is pictures. In this part, I need to manipulate the  based on OPEN-CV, who intend to use this pip need to download opencv.

2  The second part is based on 百度云智能 Face Recognition API 
   
   Problems:

2.1  matplotlib installation: when install it, it is easy to offline : “Read time out”, so we need adjust the offline time as 1000,
     namely : 【pip --default-timeout=100 install -U matplotlib///任意包】

2.2  JSON : 
     After completed the matplotlib, we find A type error 'TypeError: Object of type bytes is not JSON serializable', so we could do this:
     namely: 

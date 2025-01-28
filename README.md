# Application Load Balancer

## Step1:  Create security group for alb

## Step2:  Launch 3 instances

![image](https://github.com/user-attachments/assets/306787b5-6513-416f-a634-dac1b9dfff90)

## login into instances and change their hostnames

## install httpd web server on all 3 servers using following script

### 1. Server Home 
````
sudo -i
````

```bash
yum update
yum install httpd -y
systemctl start httpd
systemctl enable httpd
```
```
cd /var/www/html
```

**Home**
- Download home template
```
wget https://www.free-css.com/assets/files/free-css-templates/download/page289/foodfinda.zip
```
````
unzip foodfinda.zip
````
![image](https://github.com/user-attachments/assets/c0bd3e40-7dea-4b5b-85a0-ba0eaac4d286)

---

2. Server Coffee

````
sudo -i
````
```bash
yum update
yum install httpd -y
systemctl start httpd
systemctl enable httpd
```
```
cd /var/www/html
```
````
mkdir coffee
````
**Coffee**
- Download Coffee template
````
wget https://www.free-css.com/assets/files/free-css-templates/download/page292/grandcoffee.zip
````
````
unzip grandcoffee.zip
````
**move all files to coffee dir**
![image](https://github.com/user-attachments/assets/95b35bf6-9b42-4fd2-bee9-e97fac84b2fa)
---

3. Server Tea

````
sudo -i
````
```bash
yum update
yum install httpd -y
systemctl start httpd
systemctl enable httpd
```
```
cd /var/www/html
```
````
mkdir tea
````
**Coffee**
- Download Tea template
````
wget https://www.free-css.com/assets/files/free-css-templates/download/page272/tea-flower.zip
````
````
unzip tea-flower.zip
````
**move all files to tea dir**
![image](https://github.com/user-attachments/assets/090c5616-7699-46d7-9090-49a053d57d9d)

---
## Step3: Create Target Group and add respective instances

![image](https://github.com/user-attachments/assets/8913f29b-729b-4a64-a399-cf2fcdad412c)

## Step4: Create Load Balancer
- select ALB
- create load balancer
- change security group 
- add listener
- select target group as tg-home(default page)

![image](https://github.com/user-attachments/assets/ed7b6ec4-34a4-423e-9d82-733e514cbde8)
![image](https://github.com/user-attachments/assets/cc4440aa-bd59-497f-887e-52199ed06e72)

- Now we will add rule for path based routing
- click on rule -> add rule -> give tag -> next
- add condition
![image](https://github.com/user-attachments/assets/2a6c8b76-7b19-4485-8495-27b429499bb2)
![image](https://github.com/user-attachments/assets/dc41bed1-481a-438c-a5cd-6326969752ce)

- wait for few minutes till load balancer is active then copy dns name
![image](https://github.com/user-attachments/assets/08420906-0511-4b2b-b2f4-32d9841c8d5d)

## Step5: Final Output
![image](https://github.com/user-attachments/assets/f7990673-bec3-4ff1-9216-dea954cf671e)

![image](https://github.com/user-attachments/assets/5eb0c6ea-91d7-43ec-b466-75b18ece1c0b)

![image](https://github.com/user-attachments/assets/62f4666a-1358-4b47-8e7e-2619e6e89e1a)






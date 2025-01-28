

## create security group for alb
## Launch 3 instances

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

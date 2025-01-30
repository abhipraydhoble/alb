## Launch an ec2 instance with amzon linux (ami)

## Connect to ec2 instance

![image](https://github.com/user-attachments/assets/f265d6f1-8525-4952-9ce0-c6c98c1a132c)

![image](https://github.com/user-attachments/assets/8bd0cfdc-2ebc-41d4-b4aa-2230bcaa10f1)

![image](https://github.com/user-attachments/assets/30a4b5d8-1836-466b-99fb-3f7596c5656e)


### HTTPD Installation Script for Amazon Linux
```bash
sudo -i
```
````
yum update -y
````
````
yum install httpd -y
````
````
systemctl start httpd
````
````
systemctl enable httpd
````
````
systemctl status httpd
````
````
curl localhost
````
### Go to instance setting -> Security -> Click On Security Group -> Edit inbound rule

![image](https://github.com/user-attachments/assets/79c04feb-ef63-4212-8399-bef4c237c776)

- allow port http: 80
![image](https://github.com/user-attachments/assets/d8a355a2-4590-4af1-9c49-4567ec10f796)

### Host Static Website 
````
cd /var/www/html/
````
![image](https://github.com/user-attachments/assets/8fcc6456-fd4d-4d4b-b7b3-999ebfafdf46)

````
wget https://www.free-css.com/assets/files/free-css-templates/download/page296/mediplus-lite.zip
````
````
unzip mediplus-lite.zip
````
````
cd mediplus-lite
````
````
mv * /var/www/html/
````
### copy instance public ip and paste into browser

![image](https://github.com/user-attachments/assets/6deff05c-47cc-4a3d-9723-eec863a15ab1)

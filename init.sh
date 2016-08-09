cp instance.json old.json
aws ec2 run-instances --image-id ami-4d883350 --instance-type t2.micro --key-name kadoo --region sa-east-1 --associate-public-ip-address --subnet-id subnet-2412b041 > instance.json

#after all
python destroy-old.py
python set-public-ip.py

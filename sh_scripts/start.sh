echo 'Hello world!'

if [ -z "$1" ]
then
	echo "Argument required: Name"
	exit
else
	user=$1
fi

echo $user is ${#user} 'characters long'
variable=user

echo $variable 'stores' ${!variable}

subjects=('Eng','Urdu','Maths','Physics','Chemistry')
echo ${#subjects[@]}

for item in "${subjects}"; do
	echo "$item"
done

echo $? $$ $# $@ $1

echo "Runs Command $(pwd)"
echo "Prints variable $PWD"

echo "Should I exit ? Y/N"
read Name
if [ -z "$Name" ]
then 
	exit
else
	echo "Got it"
fi
clear

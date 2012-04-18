#!/bin/sh

if [ ! $1 ]
then
	echo "usage: autorun.sh <branch name> <make option>"
	exit
fi

branchName=$1
makeOpt=$2

# ��ƃf�B���N�g���i�Փ˂��Ȃ����O�Ɂj
workDir=autorun
# �ݒ�f�B���N�g���i�Փ˂��Ȃ����O�Ɂj
settingDir=.autorun

rm -rf $workDir
mkdir -p $workDir
mkdir -p $settingDir

# ���branch�́@�Ȃ���΍쐬 ����� checkout
git branch | grep $branchName > ${settingDir}/${branchName}
if [ ! -s $branchName ]
then
	git branch ${branchName}
fi

git checkout $branchName
if [ $? -ne 0 ]
then
	echo "working branch create error -> $$branchName "
	exit
fi

echo "continuous build start!"
while [ 1 -eq 1 ]
do
	isMake=0

	# �X�V�m�F����t�@�C�����Ain �̂��Ƃɕ��ׂ�
	for file in *.cpp *.hpp Makefile tmp/*.cpp
	do
		backup=${workDir}/${file}
		if [ ! -e $backup -o $file -nt $backup ] ; then
			mkdir --parents ${workDir}/`dirname $file`
			touch ${workDir}/$file
			isMake=1
		fi
	done

	if [ $isMake -eq 1 ] ; then
		make $makeOpt
		if [ $? -eq 0 ]
		then
			echo success!

			# �������̏����������ɏ���

			# add �� �R�~�b�g
			git add ./
			git commit -m "test succeeded `date` -> `git diff --cached --name-only`"

		else
			echo failed!
			# ���s���̏����������ɏ���
		fi
	fi

	sleep 1
done


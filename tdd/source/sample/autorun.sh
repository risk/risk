#!/bin/sh

if [ ! $1 ]
then
	echo "usage: autorun.sh <branch name> <make option>"
	exit
fi

branchName=$1
makeOpt=$2

# 作業ディレクトリ（衝突しない名前に）
workDir=autorun
# 設定ディレクトリ（衝突しない名前に）
settingDir=.autorun

rm -rf $workDir
mkdir -p $workDir
mkdir -p $settingDir

# 作業branchの　なければ作成 あれば checkout
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

	# 更新確認するファイルを、in のあとに並べる
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

			# 成功時の処理をここに書く

			# add と コミット
			git add ./
			git commit -m "test succeeded `date` -> `git diff --cached --name-only`"

		else
			echo failed!
			# 失敗時の処理をここに書く
		fi
	fi

	sleep 1
done


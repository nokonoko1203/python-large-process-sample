# 旧名と新名を引数から取得
oldname=$1
newname=$2

# ファイル名・フォルダ名の変更
mv ./src/$oldname ./src/$newname
mv $oldname.code-workspace $newname.code-workspace

# pyproject.toml内の名前を変更
sed -i "" "s/$oldname/$newname/g" pyproject.toml
sed -i "" "s/$oldname/$newname/g" README.md
sed -i "" "s/$oldname/$newname/g" .vscode/launch.json

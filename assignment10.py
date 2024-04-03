#!/bin/bash

# 邮件接收者
recipient="public@example.com"

# 邮件主题
subject="邮件主题"

# 邮件正文内容
body="这是邮件的正文内容。"

# 发送邮件
echo -e "Subject: $subject\n\n$body" | msmtp --from=default -t "$recipient"
#!/bin/bash

# 文件总数
total_files=1000 # 示例，根据需要调整
# 每个目录中的文件数
files_per_dir=100
# 每个上级目录中的目录数
dirs_per_parent=100

# 创建文件和目录
for ((i=1; i<=total_files; i++)); do
  # 计算目录结构
  parent_dir=$(( (i-1) / (files_per_dir*dirs_per_parent) ))
  subdir=$(( (i-1) / files_per_dir % dirs_per_parent ))
  file_name=$(printf "%03d" $(( (i-1) % files_per_dir )))

  # 创建目录路径
  dir_path="./$parent_dir/$subdir"
  mkdir -p "$dir_path"

  # 创建示例文件
  touch "$dir_path/file_$file_name"
done

echo "文件创建完成。"

#!/bin/bash

# 输入文件路径
input_file="bigdata_econ_2023/data/assignment_cml/pubnr_cn.txt"

# 每个目录中的文件数
files_per_dir=100
# 每个上级目录中的目录数
dirs_per_parent=100

# 读取文件中的每一行（每个专利号）
i=0
while IFS= read -r line; do
  ((i++))
  # 计算目录结构
  parent_dir=$(( (i-1) / (files_per_dir*dirs_per_parent) ))
  subdir=$(( (i-1) / files_per_dir % dirs_per_parent ))
  file_name=$(printf "%03d" $(( (i-1) % files_per_dir )))

  # 创建目录路径
  dir_path="./$parent_dir/$subdir"
  mkdir -p "$dir_path"

  # 根据专利号创建文件
  touch "$dir_path/$line.txt"
done < "$input_file"

echo "专利号文件创建完成。"


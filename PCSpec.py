import re
import sys
import subprocess
import os

def parse_dxdiag(file_path):
    with open(file_path, 'r') as file:
        dxdiag_content = file.read()

    # 初始化規格表
    specs = {
        "Computer Model": "",
        "CPU": "",
        "Memory": "",
        "Graphics Card": "",
        "Storage": 0
    }

    # 使用正則表達式提取資訊
    model_match = re.search(r"System Model:\s+(.+)", dxdiag_content)
    cpu_match = re.search(r"Processor:\s+(.+)", dxdiag_content)
    memory_match = re.search(r"Memory:\s+(.+)", dxdiag_content)
    gpu_match = re.findall(r"Card name:\s+(.+)", dxdiag_content)
    
    # 儲存空間總量的提取可能較複雜，這裡假設是從驅動器列表中提取第一個驅動器的資訊
    storage_match = re.findall(r"Total Space:\s+(.+?)\s+", dxdiag_content)

    # 更新規格表
    if model_match:
        specs["Computer Model"] = model_match.group(1).strip()
    if cpu_match:
        specs["CPU"] = cpu_match.group(1).strip()
    if memory_match:
        specs["Memory"] = memory_match.group(1).strip()
    if gpu_match:
        specs["Graphics Card"] = "\n"
        for gpu in gpu_match:
            specs["Graphics Card"] += f"- {gpu}\n"
    if storage_match:
        for storage_size in storage_match:
            specs["Storage"] += int(float(storage_size))
        specs["Storage"] = str(specs["Storage"])+" Gb(Total)"

    return specs

def run_dxdiag(output_file):
    try:
        # 使用 subprocess.run 执行命令
        subprocess.run(['dxdiag', '/t', output_file], check=True)
        print(f"dxdiag output saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running dxdiag: {e}")
        sys.exit(1)


if len(sys.argv) > 1:
    custom_file = sys.argv[1]
else:
    print("Checking Pc Spec...")
    run_dxdiag("DxDiag.txt")
    custom_file = os.path.join(os.getcwd(),"DxDiag.txt")
    

# 解析 dxdiag 文件並輸出規格表
specifications = parse_dxdiag(custom_file)
result =""

print("\n=============================")
for key, value in specifications.items():
    print(f"{key}: {value}")
    result += f"{key}: {value}\n"
print("=============================")

with open("Output.txt",'w+', encoding="utf-8") as f:
    f.writelines(result)

os.system("Pause")
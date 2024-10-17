import os  
import subprocess  
import xml.etree.ElementTree as ET  
  
# 定义APK文件路径和反编译后的输出目录  
apk_path = 'app/base.apk'  
output_dir = 'source/'  
  
# 使用APKTool反编译APK文件  
def decompile_apk(apk_path, output_dir):  
    subprocess.run(['D:\\apktool\\apktool.bat', 'd', apk_path, '-o', output_dir], check=True)  
  
# 解析AndroidManifest.xml文件  
def parse_manifest(manifest_path):  
    tree = ET.parse(manifest_path)  
    root = tree.getroot()  
      
    # 打印所有活动的名称  
    for activity in root.findall('application/activity'):  
        name = activity.get('android:name')  
        print(f'Activity: {name}')  
      
    # 打印所有服务的名称  
    for service in root.findall('application/service'):  
        name = service.get('android:name')  
        print(f'Service: {name}')  
  
# 主函数  
def main():  
    # 反编译APK文件  
    decompile_apk(apk_path, output_dir)  
      
    # 构造AndroidManifest.xml的路径  
    manifest_path = os.path.join(output_dir, 'AndroidManifest.xml')  
      
    # 解析并打印信息  
    parse_manifest(manifest_path)  
  
if __name__ == '__main__':  
    main()



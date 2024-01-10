print('please, wait...')
import requests
import os
import zipfile
import io

def download_and_save(url,path):
    if os.path.exists(path):
        return
    print("downloading",path)
    response = requests.get(url)
    open(path,"wb").write(response.content)
    print(path,"downloaded")
    
def download_DinoViT_model():
    download_and_save("https://www.agentspace.org/download/dino_deits8-224-final.onnx","dino_deits8-224-final.onnx")

def download_LaMini_model():
    if not os.path.exists("LaMini/"):
        os.mkdir("LaMini")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/README.md","LaMini/README.md")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/config.json","LaMini/config.json")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/generation_config.json","LaMini/generation_config.json")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/pytorch_model.bin","LaMini/pytorch_model.bin")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/special_tokens_map.json","LaMini/special_tokens_map.json")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/spiece.model","LaMini/spiece.model")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/tokenizer.json","LaMini/tokenizer.json")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/tokenizer_config.json","LaMini/tokenizer_config.json")
    download_and_save("https://huggingface.co/MBZUAI/LaMini-Flan-T5-248M/resolve/main/training_args.bin","LaMini/training_args.bin")

def download_robot_config():
    download_and_save("https://www.agentspace.org/download/nico_humanoid_upper_rh7d_ukba.json","nico_humanoid_upper_rh7d_ukba.json")

def download_and_unzip(path,url):
    if os.path.exists(path):
        return
    print("downloading",path)
    response = requests.get(url)
    if response.ok:
        file_like_object = io.BytesIO(response.content)
        zipfile_object = zipfile.ZipFile(file_like_object)    
        zipfile_object.extractall(".")

def download_v4l2():
    download_and_unzip("v4l2-ctl.exe","https://www.agentspace.org/download/v4l2-ctl.zip")  

def download_face():
    download_and_unzip("face/labels.txt","https://www.agentspace.org/download/face.zip")  

def download_all():
    download_DinoViT_model()
    download_LaMini_model()
    download_robot_config()
    download_v4l2()
    download_face()

if __name__ == "__main__":
    download_all()
    print("done")


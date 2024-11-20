#@title Setup
import os
import shutil
from google.colab import files
openai_key = input("OpenAI Key: ")
os.environ['OPENAI_API_KEY'] = openai_key
folder_name = "JOB"
print("\n Upload the job post please")
os.makedirs(folder_name, exist_ok=True)
uploaded = files.upload()
file_name = next(iter(uploaded))
file_path = os.path.join(folder_name, file_name)
shutil.move(file_name, file_path)
# !pip install llama_index == 0.6.13
# !pip install pypdf
#sk-Ye68KAua24oRHrlojUxTT3B1bkFJIVj5jgE8HjViWfTTWuhI
from llama_index.llms import LlamaCPP
from llama_index.llms.llama_utils import (
    messages_to_prompt,
    completion_to_prompt,
)

from fpdf import FPDF


model_url = 'llama-2-7b-chat.Q3_K_M.gguf'


# LOAD MODEL 
llm = LlamaCPP(
    # You can pass in the URL to a GGML model to download it automatically
    model_path=model_url,
    # optionally, you can set the path to a pre-downloaded model instead of model_url
    # model_url=None,
    temperature=0.1,
    # max_new_tokens=256,
    # llama2 has a context window of 4096 tokens, but we set it lower to allow for some wiggle room
    # context_window=4096,
    # kwargs to pass to __call__()
    generate_kwargs={},
    # kwargs to pass to __init__()
    # set to at least 1 to use GPU
    # model_kwargs={"n_gpu_layers": 1},
    # transform inputs into Llama2 format
    messages_to_prompt=messages_to_prompt,
    completion_to_prompt=completion_to_prompt,
    verbose=True,
)


prompt ='''
Rewrite the user's accomplishment for a resume in the following format with full sentences. 

I accomplished X by the measure Y that resulted in Z


accomplishment: {}
'''


basic_experience = '''
    As a Junior Developer at Norconsult, I've played a key role in enhancing our business intelligence app, implementing diverse visualizations using CraftJS, ChartJS, Leaflet, and React libraries. I improved data accessibility by designing a system to access various sources and storing data in PostgreSQL. Strengthening data analysis capabilities, I utilized CubeJS for querying, measures, and dimensions. Additionally, I developed a robust REST API using Node.js, Express, middleware, and Winston to enhance application functionality and reliability. I also contributed to AI and machine learning advancements through research and prototyping.

    My recent project, the Heads-Up Display Smart Helmet, received the "Best Safety Analysis" award, showcasing my innovation. I developed and tested it using Raspberry Pi 4 and Pi Camera for real-time video stream processing. Implementing object detection using TensorFlow lite models, I optimized performance with a transition from Python to C++. Demonstrating expertise in embedded systems design, I addressed task management through multiprocessing and multithreading.
'''
accomplishment=input("what did u achieve")

# joing to form final prompt string
final_question = prompt.join((accomplishment))


# get response and iterate in terminal
response_iter = llm.stream_complete(final_question)
str_res = ""
for response in response_iter:
    str_res += response.delta
    print(response.delta, end="", flush=True)